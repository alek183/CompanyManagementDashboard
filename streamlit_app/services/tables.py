import streamlit as st
from .task_service import fetch_tasks
from .employee_service import fetch_employees
from .client_service import fetch_clients

# ------------------ TASKS ------------------
def tasks_table():
    tasks = fetch_tasks()
    if tasks:
        st.table(tasks)
    else:
        st.info("No tasks available.")

# ------------------ EMPLOYEES ------------------
def employees_table():
    employees = fetch_employees()
    if employees:
        st.table(employees)
    else:
        st.info("No employees available.")

# ------------------ CLIENTS ------------------
def clients_table():
    clients = fetch_clients()
    if clients:
        st.table(clients)
    else:
        st.info("No clients available.")
