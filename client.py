import json
from os import getenv

import requests

url = getenv("URL", "http://127.0.0.1:6502/api")

status = {
    "200s": 0,
    "300s": 0,
    "400s": 0,
    "500s": 0,
    "total": 0,
}

while True:
    req = requests.get(url)
    if req.status_code <= 299:
        status["200s"] += 1
    elif req.status_code <= 399:
        status["300s"] += 1
    elif req.status_code <= 499:
        status["400s"] += 1
    elif req.status_code <= 599:
        status["500s"] += 1
    status["total"] += 1
    print(json.dumps(status))
