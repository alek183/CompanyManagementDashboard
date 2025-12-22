import streamlit as st
from .task_service import fetch_tasks
from .employee_service import fetch_employees
from .client_service import fetch_clients
from .forms import task_update_form, employee_update_form, client_update_form


# TASKS

def tasks_table():
    tasks = fetch_tasks()
    if tasks:
        for task in tasks:
            with st.expander(f"#{task['id']} - {task['title']} ({task['status']})"):
                task_update_form(task)
    else:
        st.info("No tasks available.")

# EMPLOYEES

def employees_table():
    employees = fetch_employees()

    if not employees:
        st.info("No employees available.")
        return

    for emp in employees:
        with st.expander(f"#{emp['id']} - {emp['first_name']} {emp['last_name']}"):
            employee_update_form(emp)

# CLIENTS

def clients_table():
    clients = fetch_clients()

    if clients:
        for client in clients:
            with st.expander(f"#{client['id']} - {client['name']}"):
                client_update_form(client)
    else:
        st.info("No clients available.")
