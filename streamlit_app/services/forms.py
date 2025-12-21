import streamlit as st
from .task_service import create_task
from .employee_service import create_employee
from .client_service import create_client
import datetime

# ------------------ TASKS ------------------
def task_create_form():
    with st.form("task_create", clear_on_submit=True):
        title = st.text_input("Task title")
        status = st.selectbox("Status", ["Pending", "Done"])
        due_date = st.date_input("Due date", datetime.date.today())
        if st.form_submit_button("Add task") and title:
            create_task({
                "title": title,
                "status": status,
                "creation_date": str(datetime.date.today()),
                "due_date": str(due_date)
            })
            st.success("Task added ✅")
            st.rerun()

# ------------------ EMPLOYEES ------------------
def employee_create_form():
    with st.form("emp_create", clear_on_submit=True):
        first = st.text_input("First name")
        last = st.text_input("Last name")
        if st.form_submit_button("Add employee") and first and last:
            create_employee({"first_name": first, "last_name": last})
            st.success("Employee added ✅")
            st.rerun()

# ------------------ CLIENTS ------------------
def client_create_form():
    with st.form("client_create", clear_on_submit=True):
        name = st.text_input("Client name")
        mail = st.text_input("Client email")
        contact = st.text_input("Contact number")
        if st.form_submit_button("Add client") and name and mail and contact:
            create_client({
                "name": name,
                "mail": mail,
                "contact_number": contact
            })
            st.success("Client added ✅")
            st.rerun()
