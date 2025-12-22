import streamlit as st
from .tables import employees_table
from .forms import employee_create_form

def app():
    st.title("👨‍💼 Employees")
    employees_table()
    st.divider()
    employee_create_form()
