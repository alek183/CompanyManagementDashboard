import streamlit as st
from components.tables import tasks_table
from components.forms import task_form

st.title("Tasks")

tasks_table()
st.divider()
task_form()
