import streamlit as st
from .tables import tasks_table
from .forms import task_create_form

def app():
    st.title("Tasks")
    tasks_table()
    st.divider()
    task_create_form()
