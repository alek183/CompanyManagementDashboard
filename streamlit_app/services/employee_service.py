from .api import get, post, put, delete

def fetch_employees():
    return get("/employees")

def create_employee(emp_data):
    post("/employees", emp_data)

def update_employee(emp_id, emp_data):
    put(f"/employees/{emp_id}", emp_data)

def delete_employee(emp_id):
    delete(f"/employees/{emp_id}")
