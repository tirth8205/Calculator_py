import streamlit as st
import csv
import os
import re

# Function to validate email
def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

# Function to save user data
def save_user_data():
    data_exists = os.path.isfile('data.csv')
    with open('data.csv', mode='a', newline='') as file:
        writer = csv.writer(file)
        if not data_exists:
            writer.writerow(['Name', 'Email', 'Number of Employees', 'Industry'])
        writer.writerow([st.session_state.name, st.session_state.email, st.session_state.num_employees, st.session_state.industry])

# Function to reset session state and clear cache files
def reset_state():
    st.session_state.clear()
    st.session_state.show_welcome = True
    st.experimental_rerun()
