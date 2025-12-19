import streamlit as st
import pandas as pd

def tasks_table():
    df = pd.DataFrame(columns=["Title", "Status"])
    st.dataframe(df, use_container_width=True)

def employees_table():
    df = pd.DataFrame(columns=["First name", "Last name"])
    st.dataframe(df, use_container_width=True)

def clients_table():
    df = pd.DataFrame(columns=["Client name"])
    st.dataframe(df, use_container_width=True)
