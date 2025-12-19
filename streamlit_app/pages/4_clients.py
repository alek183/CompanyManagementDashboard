import streamlit as st
from components.tables import clients_table
from components.forms import client_form

st.title("Clients")

clients_table()
st.divider()
client_form()
