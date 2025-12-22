import streamlit as st
from .task_service import create_task
from .employee_service import create_employee, delete_employee
from .client_service import create_client
from .employee_service import fetch_employees, update_employee
from .client_service import fetch_clients, update_client, delete_client
import datetime

# TASKS

def task_create_form():
    employees = fetch_employees()
    clients = fetch_clients()

    emp_map = {f"{e['first_name']} {e['last_name']}": e['id'] for e in employees}
    client_map = {c['name']: c['id'] for c in clients}

    with st.form("task_create", clear_on_submit=True):
        title = st.text_input("Task title")
        description = st.text_area("Description")
        status = st.selectbox("Status", ["Pending", "In Progress", "Done"])
        employee = st.selectbox("Employee", ["None"] + list(emp_map.keys()))
        client = st.selectbox("Client", ["None"] + list(client_map.keys()))
        due_date = st.date_input("Due date", datetime.date.today())

        if st.form_submit_button("Add task") and title:
            create_task({
                "title": title,
                "description": description,
                "status": status,
                "employee_id": emp_map.get(employee),
                "client_id": client_map.get(client),
                "creation_date": str(datetime.date.today()),
                "due_date": str(due_date)
            })
            st.success("Task added ✅")
            st.rerun()


def task_update_form(task):
    from .task_service import update_task, delete_task
    task_id = task["id"]
    employees = fetch_employees()
    clients = fetch_clients()

    emp_map = {f"{e['first_name']} {e['last_name']}": e['id'] for e in employees}
    client_map = {c['name']: c['id'] for c in clients}

    st.markdown("")
    with st.form(f"update_task_{task_id}"):
        title = st.text_input("Title", task["title"])
        description = st.text_area("Description", task.get("description", ""))
        status = st.selectbox("Status", ["Pending", "In Progress", "Done"], index=["Pending", "In Progress", "Done"].index(task["status"]))
        employee = st.selectbox("Employee", ["None"] + list(emp_map.keys()), index=(list(emp_map.keys()).index(next((k for k,v in emp_map.items() if v==task["employee_id"]), "None")) if task.get("employee_id") else 0))
        client = st.selectbox("Client", ["None"] + list(client_map.keys()), index=(list(client_map.keys()).index(next((k for k,v in client_map.items() if v==task["client_id"]), "None")) if task.get("client_id") else 0))
        due_date = st.date_input("Due date", datetime.date.fromisoformat(task["due_date"]) if task.get("due_date") else datetime.date.today())

        col1, col2 = st.columns(2)
        if col1.form_submit_button("💾 Update"):
            update_task(task_id, {
                "title": title,
                "description": description,
                "status": status,
                "employee_id": emp_map.get(employee),
                "client_id": client_map.get(client),
                "creation_date": task["creation_date"],
                "due_date": str(due_date)
            })
            st.success("Task updated ✅")
            st.rerun()

        if col2.form_submit_button("🗑️ Delete"):
            delete_task(task_id)
            st.success("Task deleted ❌")
            st.rerun()

# EMPLOYEES

def employee_create_form():
    with st.form("emp_create", clear_on_submit=True):
        first = st.text_input("First name")
        last = st.text_input("Last name")

        if st.form_submit_button("Add employee") and first and last:
            create_employee({
                "first_name": first,
                "last_name": last
            })
            st.success("Employee added ✅")
            st.rerun()

def employee_update_form(employee):
    with st.form(f"emp_update_{employee['id']}"):
        first = st.text_input(
            "First name",
            employee["first_name"]
        )
        last = st.text_input(
            "Last name",
            employee["last_name"]
        )

        col1, col2 = st.columns(2)

        with col1:
            update = st.form_submit_button("💾 Update")

        with col2:
            delete = st.form_submit_button("🗑️ Delete")

        if update:
            update_employee(
                employee["id"],
                {
                    "first_name": first,
                    "last_name": last
                }
            )
            st.success("Employee updated ✅")
            st.rerun()

        if delete:
            delete_employee(employee["id"])
            st.warning("Employee deleted ❌")
            st.rerun()

# CLIENTS

def client_create_form():
    with st.form("client_create", clear_on_submit=True):
        name = st.text_input("Client name")
        mail = st.text_input("Email")
        contact = st.text_input("Contact number")

        if st.form_submit_button("Add client") and name and mail:
            create_client({
                "name": name,
                "mail": mail,
                "contact_number": contact
            })
            st.success("Client added ✅")
            st.rerun()

def client_update_form(client):
    with st.form(f"client_update_{client['id']}"):
        name = st.text_input("Client name", client["name"])
        mail = st.text_input("Email", client["mail"])
        contact_number = st.text_input("Contact number", client["contact_number"])

        col1, col2 = st.columns(2)

        with col1:
            if st.form_submit_button("💾 Update"):
                update_client(
                    client["id"],
                    {
                        "name": name,
                        "mail": mail,
                        "contact_number": contact_number
                    }
                )
                st.success("Client updated ✅")
                st.rerun()

        with col2:
            if st.form_submit_button("🗑️ Delete"):
                delete_client(client["id"])
                st.warning("Client deleted ❌")
                st.rerun()