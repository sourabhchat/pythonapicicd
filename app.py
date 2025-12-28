from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def home():
    return jsonify({'message': 'Hello, Kubernetes!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=25000) #prod will run on 25k