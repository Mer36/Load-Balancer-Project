from flask import Flask
from consistent_hash import ConsistentHash
import requests

app = Flask(__name__)

servers = [
    "http://host.docker.internal:5000",
    "http://host.docker.internal:5001",
    "http://host.docker.internal:5002"
]

hash_ring = ConsistentHash(servers)

@app.route("/home/<client_id>")
def home(client_id):

    server = hash_ring.get_server(client_id)

    try:
        response = requests.get(
            f"{server}/home",
            timeout=2
        )

        return response.json()

    except requests.exceptions.RequestException:

        return {
            "status": "failed",
            "message": f"{server} is unavailable"
        }, 503


if __name__ == "__main__":
    
    app.run(host="0.0.0.0", port=8000)