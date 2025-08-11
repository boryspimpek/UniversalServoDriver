from flask import Flask, render_template, jsonify
import servo  # Twój istniejący plik servo.py

app = Flask(__name__)

# Słownik mapujący nazwy akcji na funkcje ruchu
ACTIONS = {
    'walk': servo.walk,
    "test_function": servo.test_function
    # Dodaj nowe akcje tutaj: 'nazwa': servo.funkcja
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/move/<action>')
def move_robot(action):
    try:
        if action in ACTIONS:
            ACTIONS[action]()
            return jsonify({
                'status': 'success', 
                'action': action,
                'message': f'Wykonano akcję: {action}'
            })
        else:
            return jsonify({
                'status': 'error',
                'message': f'Nieznana akcja: {action}'
            }), 400
    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Błąd wykonania: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)