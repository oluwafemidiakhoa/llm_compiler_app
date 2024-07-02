from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return jsonify({"message": "Hello, World!"}), 200

@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Test successful"}), 200

if __name__ == '__main__':
    print("Starting Flask server...")
    app.run(host='0.0.0.0', port=5000, debug=True)