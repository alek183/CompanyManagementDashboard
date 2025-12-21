import streamlit as st
from .tables import clients_table
from .forms import client_create_form

def app():
    st.title("Clients")
    clients_table()
    st.divider()
    client_create_form()
