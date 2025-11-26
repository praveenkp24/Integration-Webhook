from flask import Flask, request, jsonify
from flask_cors import CORS  # allows frontend hosted elsewhere to fetch data

app = Flask(__name__)
CORS(app)  # enable CORS for all domains

latest_payload = {}

@app.route("/data", methods=["GET"])
def get_payload():
    return jsonify(latest_payload)

@app.route("/update", methods=["GET", "POST"])
def update_payload():
    global latest_payload

    if request.method == "GET":
        latest_payload = request.args.to_dict()
    elif request.method == "POST":
        if request.is_json:
            latest_payload = request.get_json()
        else:
            latest_payload = request.form.to_dict()

    return jsonify({"status": "ok", "received": latest_payload})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
