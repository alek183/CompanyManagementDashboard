import streamlit as st
from components.tables import employees_table
from components.forms import employee_form

st.title("Employees")

employees_table()
st.divider()
employee_form()
