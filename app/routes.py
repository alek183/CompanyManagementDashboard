from fastapi import APIRouter, HTTPException, Depends
from typing import List
import sqlite3
from models import Employee, EmployeeCreate
from models import Client, ClientCreate
from models import Task, TaskCreate
from database import db_connection

router = APIRouter()

# EMPLOYEES CRUD

# CREATE

@router.post("/employees/", response_model=Employee)
def create_employee(employee: EmployeeCreate, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO employees (first_name, last_name) VALUES (?, ?)",
        (employee.first_name, employee.last_name)
    )
    db.commit()
    return {**employee.model_dump(), "id": cursor.lastrowid}

# READ ALL

@router.get("/employees/", response_model=List[Employee])
def get_employees(db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees")
    rows = cursor.fetchall()
    return [Employee(**row) for row in rows]

# READ ONE

@router.get("/employees/{employee_id}", response_model=Employee)
def get_employee(employee_id: int, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM employees WHERE id = ?", (employee_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Employee not found")
    return Employee(**row)

# UPDATE

@router.put("/employees/{employee_id}", response_model=Employee)
def update_employee(employee_id: int, employee: EmployeeCreate, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE employees SET first_name = ?, last_name = ? WHERE id = ?",
        (employee.first_name, employee.last_name, employee_id)
    )
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {**employee.model_dump(), "id": employee_id}

# DELETE

@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted"}

# CLIENTS CRUD

# CREATE

@router.post("/clients/", response_model=Client)
def create_client(client: ClientCreate, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute(
        "INSERT INTO clients (name, mail, contact_number) VALUES (?, ?, ?)",
        (client.name, client.mail, client.contact_number)
    )
    db.commit()
    return {**client.model_dump(), "id": cursor.lastrowid}

# READ ALL

@router.get("/clients/", response_model=List[Client])
def get_clients(db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clients")
    rows = cursor.fetchall()
    return [Client(**row) for row in rows]

# READ ONE

@router.get("/clients/{client_id}", response_model=Client)
def get_client(client_id: int, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM clients WHERE id = ?", (client_id,))
    row = cursor.fetchone()
    if not row:
        raise HTTPException(status_code=404, detail="Client not found")
    return Client(**row)

# UPDATE

@router.put("/clients/{client_id}", response_model=Client)
def update_client(client_id: int, client: ClientCreate, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE clients SET name = ?, mail = ?, contact_number = ? WHERE id = ?",
        (client.name, client.mail, client.contact_number, client_id)
    )
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Client not found")
    return {**client.model_dump(), "id": client_id}

# DELETE

@router.delete("/clients/{client_id}")
def delete_client(client_id: int, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM clients WHERE id = ?", (client_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Client not found")
    return {"detail": "Client deleted"}

# TASKS CRUD

# CREATE

@router.post("/tasks/", response_model=Task)
def create_task(
    task: TaskCreate,
    db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()

    # FK validation
    if task.employee_id is not None:
        cursor.execute("SELECT id FROM employees WHERE id = ?", (task.employee_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=400, detail="Employee does not exist")

    if task.client_id is not None:
        cursor.execute("SELECT id FROM clients WHERE id = ?", (task.client_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=400, detail="Client does not exist")

    cursor.execute("""
        INSERT INTO tasks (
            title, description, status,
            employee_id, client_id,
            creation_date, due_date
        )
        VALUES (?, ?, ?, ?, ?, ?, ?)
        """,
        (
            task.title,
            task.description,
            task.status,
            task.employee_id,
            task.client_id,
            task.creation_date,
            task.due_date
        )
    )
    db.commit()

    return {**task.model_dump(), "id": cursor.lastrowid}

# READ ALL

@router.get("/tasks/", response_model=List[Task])
def get_tasks(db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks")
    rows = cursor.fetchall()
    return [Task(**row) for row in rows]

# READ ONE

@router.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
    row = cursor.fetchone()

    if not row:
        raise HTTPException(status_code=404, detail="Task not found")

    return Task(**row)

# UPDATE

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task: TaskCreate,
    db: sqlite3.Connection = Depends(db_connection)
):
    cursor = db.cursor()

    # FK validation
    if task.employee_id is not None:
        cursor.execute("SELECT id FROM employees WHERE id = ?", (task.employee_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=400, detail="Employee does not exist")

    if task.client_id is not None:
        cursor.execute("SELECT id FROM clients WHERE id = ?", (task.client_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=400, detail="Client does not exist")

    cursor.execute("""
        UPDATE tasks
        SET title = ?, description = ?, status = ?,
            employee_id = ?, client_id = ?,
            creation_date = ?, due_date = ?
        WHERE id = ?
        """,
        (
            task.title,
            task.description,
            task.status,
            task.employee_id,
            task.client_id,
            task.creation_date,
            task.due_date,
            task_id
        )
    )
    db.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {**task.model_dump(), "id": task_id}

# DELETE

@router.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted"}