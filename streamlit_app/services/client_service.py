from .api import get, post, put, delete

def fetch_clients():
    return get("/clients")

def create_client(client_data):
    post("/clients", client_data)

def update_client(client_id, client_data):
    put(f"/clients/{client_id}", client_data)

def delete_client(client_id):
    delete(f"/clients/{client_id}")
