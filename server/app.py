from flask import Flask, jsonify
import os

app = Flask(__name__)  # this creates the web application

SERVER_ID = os.getenv("SERVER_ID", "Unknown")  # this gets the server ID from the environment variable, default is unknown

@app.route("/home", methods=["GET"])  # this is the route for the home page
def home():
    return jsonify({
        "message": f"Hello From Server: {SERVER_ID}",
        "status": "successful"
        }), 200  # this returns a JSON response

@app.route("/heartbeat", methods=["GET"]) 
def heartbeat():
    return "", 200

if __name__ == "__main__":
    print("Starting Flask Server...")
    app.run(host="0.0.0.0", port=5000, debug=True)  # this starts the web server

