from fastapi import APIRouter, HTTPException, Depends
from typing import List
import sqlite3
from models import Employee, EmployeeCreate
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
    return {**employee.dict(), "id": cursor.lastrowid}

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
    return {**employee.dict(), "id": employee_id}

# DELETE
@router.delete("/employees/{employee_id}")
def delete_employee(employee_id: int, db: sqlite3.Connection = Depends(db_connection)):
    cursor = db.cursor()
    cursor.execute("DELETE FROM employees WHERE id = ?", (employee_id,))
    db.commit()
    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"detail": "Employee deleted"}
