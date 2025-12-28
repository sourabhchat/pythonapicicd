from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, Kubernetes! change 10th on 28-dec-2025'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=21000) 