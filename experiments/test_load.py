import requests
from collections import Counter

counter = Counter()

for i in range(10000):

    response = requests.get(
        f"http://localhost:8000/home/{i}"
    )

    server = response.json()["message"]

    counter[server] += 1

print(counter)