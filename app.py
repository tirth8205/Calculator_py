import streamlit as st
from calculations import calculate_turnover
from ui import render_result, render_inputs, render_welcome, show_popup, reset_state
import csv
import os
import re

# Streamlit UI
st.set_page_config(page_title="Employee Impact Calculator", page_icon=":briefcase:")

# Load custom CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state variables
if 'name' not in st.session_state:
    st.session_state.name = ''
if 'email' not in st.session_state:
    st.session_state.email = ''
if 'num_employees' not in st.session_state:
    st.session_state.num_employees = 0
if 'industry' not in st.session_state:
    st.session_state.industry = 'Manufacturing'
if 'show_result' not in st.session_state:
    st.session_state.show_result = False
if 'show_welcome' not in st.session_state:
    st.session_state.show_welcome = True
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False

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

if st.session_state.show_welcome:
    render_welcome()
    if st.button("Start"):
        if st.session_state.name and is_valid_email(st.session_state.email):
            st.session_state.show_welcome = False
            st.rerun()
        else:
            st.warning("Please enter a valid name and email address.")
elif st.session_state.show_result:
    employees_considering_leaving, employees_leaving_due_to_work_life_balance, estimated_turnover_cost = calculate_turnover(st.session_state.num_employees, st.session_state.industry)
    render_result(st.session_state.num_employees, st.session_state.industry, employees_considering_leaving, employees_leaving_due_to_work_life_balance, estimated_turnover_cost)
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[Book a Discovery Call](https://tidycal.com/janet/discovery-call)", unsafe_allow_html=True)
    with col2:
        if st.button("Calculate Again"):
            st.session_state.show_popup = True
            st.rerun()
elif st.session_state.show_popup:
    show_popup()
else:
    num_employees, industry = render_inputs()
    if st.button("Calculate"):
        st.session_state.num_employees = num_employees
        st.session_state.industry = industry
        st.session_state.show_result = True
        save_user_data()
        st.rerun()
