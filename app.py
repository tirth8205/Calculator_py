import streamlit as st
from calculations import calculate_turnover
from ui import render_result, render_inputs, render_welcome, show_popup
from utils import save_user_data, is_valid_email, reset_state  # Import the necessary functions

# Streamlit UI
st.set_page_config(page_title="Employee Impact Calculator", page_icon=":briefcase:")

# Load custom HTML and CSS
with open('index.html', 'r') as f:
    custom_html = f.read()
st.markdown(custom_html, unsafe_allow_html=True)

# Load custom CSS
with open('styles.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Initialize session state variables
if 'show_welcome' not in st.session_state:
    st.session_state.show_welcome = True
if 'show_inputs' not in st.session_state:
    st.session_state.show_inputs = False
if 'show_result' not in st.session_state:
    st.session_state.show_result = False
if 'name' not in st.session_state:
    st.session_state.name = ''
if 'email' not in st.session_state:
    st.session_state.email = ''
if 'num_employees' not in st.session_state:
    st.session_state.num_employees = 0
if 'industry' not in st.session_state:
    st.session_state.industry = 'Manufacturing'
if 'show_popup' not in st.session_state:
    st.session_state.show_popup = False

if st.session_state.show_welcome:
    render_welcome()
elif st.session_state.show_inputs:
    render_inputs()
elif st.session_state.show_result:
    employees_considering_leaving, employees_leaving_due_to_work_life_balance, estimated_turnover_cost = calculate_turnover(st.session_state.num_employees, st.session_state.industry)
    render_result(st.session_state.num_employees, st.session_state.industry, employees_considering_leaving, employees_leaving_due_to_work_life_balance, estimated_turnover_cost)
elif st.session_state.show_popup:
    show_popup()
