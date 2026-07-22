import requests
from collections import Counter

counter = Counter()

for i in range(10000):

    response = requests.get(
        f"http://localhost:8000/home/{i}"
    )

    data = response.json()

    server = data["message"].split(":")[-1].strip()

    counter[server] += 1

print(counter)