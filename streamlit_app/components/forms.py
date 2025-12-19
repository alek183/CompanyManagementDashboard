import streamlit as st

def task_form():
    with st.form("task_form"):
        title = st.text_input("Task title")
        submitted = st.form_submit_button("Create task")
        if submitted:
            st.success("Task created")

def employee_form():
    with st.form("employee_form"):
        first = st.text_input("First name")
        last = st.text_input("Last name")
        submitted = st.form_submit_button("Add employee")
        if submitted:
            st.success("Employee added")

def client_form():
    with st.form("client_form"):
        name = st.text_input("Client name")
        submitted = st.form_submit_button("Add client")
        if submitted:
            st.success("Client added")