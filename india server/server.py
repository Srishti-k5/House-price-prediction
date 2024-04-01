from flask import Flask, request, jsonify
import util

app = Flask(__name__)

@app.route('/get_features')
def get_features():
    response = jsonify({
        'features' : util.get_features()
    })
    response.headers.add('Access-Control-Allow-Origin', '+')
    return response

if __name__ == '__main__':
    app.run()
