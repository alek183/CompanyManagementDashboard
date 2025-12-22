import streamlit as st
from .employee_service import fetch_employees
from .client_service import fetch_clients
from .task_service import fetch_tasks

def app():
    st.title("📊 Overview")

    employees = fetch_employees() or []
    clients = fetch_clients() or []
    tasks = fetch_tasks() or []

    employees_count = len(employees)
    clients_count = len(clients)
    tasks_count = len(tasks)

    pending_tasks = sum(1 for t in tasks if t.get("status") == "Pending")
    in_progress_tasks = sum(1 for t in tasks if t.get("status") == "In Progress")
    done_tasks = sum(1 for t in tasks if t.get("status") == "Done")

    st.markdown("### Overview Metrics", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    col1.metric("👨‍💼 Employees", employees_count)
    col2.metric("💼 Clients", clients_count)
    col3.metric("📝 Tasks", tasks_count)

    st.divider()
    st.markdown("### Task Status", unsafe_allow_html=True)
    col4, col5, col6 = st.columns(3)
    col4.metric("⏳ Pending", pending_tasks)
    col5.metric("🚧 In Progress", in_progress_tasks)
    col6.metric("✅ Done", done_tasks)
