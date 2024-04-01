from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')

def hello():
    return "hii"
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)
    print("Starting Python Flask Server For Home Price Prediction...")
    # util.load_saved_artifacts()
    app.run()