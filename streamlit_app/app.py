import streamlit as st
from services import overview, tasks, employees, clients

st.set_page_config(page_title="Company Management Dashboard", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Overview", "Tasks", "Employees", "Clients"])

if page == "Overview":
    overview.app()
elif page == "Tasks":
    tasks.app()
elif page == "Employees":
    employees.app()
elif page == "Clients":
    clients.app()
