import requests

BASE_URL = "http://localhost:8000"

def get(endpoint):
    return requests.get(f"{BASE_URL}{endpoint}").json()

def post(endpoint, data):
    return requests.post(f"{BASE_URL}{endpoint}", json=data)

def put(endpoint, data):
    return requests.put(f"{BASE_URL}{endpoint}", json=data)

def delete(endpoint):
    return requests.delete(f"{BASE_URL}{endpoint}")
