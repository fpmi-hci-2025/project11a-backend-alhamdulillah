from flask import Flask, jsonify
import os
import time

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        'message': 'Hello World from Makhachkala!',
        'status': 'OK',
        'timestamp': time.time(),
        'environment': os.getenv('ENVIRONMENT', 'development')
    })

@app.route('/api/hello')
def hello():
    name = os.getenv('USER_NAME', 'World')
    return jsonify({
        'message': f'Hello, {name}!',
        'service': 'Makhachkala Backend',
        'version': '1.0.0',
        'shauma_price': '5 рублей'
    })

@app.route('/api/health')
def health():
    return jsonify({
        'status': 'healthy',
        'service': 'makhachkala-backend',
        'database': 'none',
        'timestamp': time.time()
    })

@app.route('/api/echo', methods=['POST'])
def echo():
    from flask import request
    data = request.get_json()
    if data:
        return jsonify({
            'message': 'Received your data!',
            'your_data': data,
            'echo': True
        })
    return jsonify({'message': 'Send me JSON!'}), 400

if __name__ == '__main__':
    port = int(os.getenv('PORT', 8000))
    app.run(host='0.0.0.0', port=port, debug=os.getenv('DEBUG', 'False') == 'True')