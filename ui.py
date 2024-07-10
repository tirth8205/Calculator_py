import streamlit as st

def render_header():
    st.markdown("<div class='header'>", unsafe_allow_html=True)
    st.image('logo.png', width=150)
    st.markdown("</div>", unsafe_allow_html=True)

def render_welcome():
    render_header()
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.markdown("<h2>Do You Know How Many Employees Are Going to Leave Your Company?</h2>", unsafe_allow_html=True)
    st.markdown("<p>Find it out in just a few clicks!</p>", unsafe_allow_html=True)
    st.text_input("Name", key='name')
    st.text_input("Email", key='email')
    st.markdown("</div>", unsafe_allow_html=True)

def render_result(num_employees, industry, employees_considering_leaving, employees_leaving_due_to_work_life_balance, estimated_turnover_cost):
    render_header()
    result_sentence = f"""
        <div class='result-card'>
            <h2>Impact Analysis</h2>
            <p style='font-size:18px;'>
                With <strong>{num_employees}</strong> employees in the <strong>{industry}</strong> industry:
                <ul>
                    <li><strong>{employees_considering_leaving}</strong> employees are likely to consider leaving.</li>
                    <li>Among them, <strong>{employees_leaving_due_to_work_life_balance}</strong> employees may leave due to work-life balance issues.</li>
                    <li>This could cost your company an estimated <strong>£{estimated_turnover_cost:,.2f}</strong>.</li>
                </ul>
            </p>
        </div>
    """

    note = """
        <div class='result-note'>
            <p>
                Note: The turnover cost is based on data from various reports: Labour Turnover Report 2024, Kings Fund report on social care workforce, Strathprints report on UK hospitality sector, and ILC report on retail staff.
                The calculation assumes that 1/3 of frontline employees considering quitting cite work-life balance as the main reason.
            </p>
        </div>
    """

    st.markdown(result_sentence, unsafe_allow_html=True)
    st.markdown(note, unsafe_allow_html=True)

def render_inputs():
    render_header()
    st.markdown("<div class='container'>", unsafe_allow_html=True)
    st.subheader("Enter the details below to calculate the impact:")
    num_employees = st.number_input("Number of Employees:", min_value=0, step=1, key='input_num_employees')
    industry = st.selectbox("Industry:", options=["Manufacturing", "Social Work/Healthcare", "Luxury Retail", "Hospitality"], key='input_industry')
    st.markdown("</div>", unsafe_allow_html=True)
    return num_employees, industry

def show_popup():
    render_header()
    st.warning("Worried about losing employees? Book a call or recalculate.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("<a href='https://tidycal.com/janet/discovery-call' class='button-link' target='_blank'>Book a Discovery Call</a>", unsafe_allow_html=True)
    with col2:
        if st.button("Recalculate"):
            reset_state()

# Function to reset session state and clear cache files
def reset_state():
    for key in st.session_state.keys():
        del st.session_state[key]
    # Clear any cache files if necessary
    if os.path.exists('__pycache__'):
        import shutil
        shutil.rmtree('__pycache__')
    st.experimental_rerun()
