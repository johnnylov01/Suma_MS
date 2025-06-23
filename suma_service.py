from flask import Flask, request, jsonify
import os

app = Flask(__name__)

def sumar(a, b):
    try:
        return float(a) + float(b)
    except (ValueError, TypeError):
        raise ValueError("Los valores deben ser válidos")

@app.route('/sumar', methods=['GET'])
def sumar_endpoint():
    a = request.args.get('a')
    b = request.args.get('b')

    if not a or not b:
        return jsonify({'error': 'Parámetros a y b son requeridos'}), 400

    try:
        return jsonify({'resultado': sumar(a, b)}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 80))
    app.run(host='0.0.0.0', port=port)
