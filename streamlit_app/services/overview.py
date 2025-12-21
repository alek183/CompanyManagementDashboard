import streamlit as st

def overview_cards():
    c1, c2, c3 = st.columns(3)
    c1.metric("Employees", 0)
    c2.metric("Clients", 0)
    c3.metric("Pending Tasks", 0)

def app():
    st.title("Overview")
    overview_cards()
