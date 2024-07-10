import streamlit as st

def render_welcome():
    st.markdown("<div class='fullscreen-bg'>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-container'>", unsafe_allow_html=True)
    st.markdown("<div class='logo-container'><img src='logo.png' width='150'></div>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-header'>Do You Know How Many Employees Are Going to Leave Your Company?</div>", unsafe_allow_html=True)
    st.markdown("<div class='welcome-subheader'>Find it out in just a few clicks!</div>", unsafe_allow_html=True)
    st.text_input("Name", key='name')
    st.text_input("Email", key='email')
    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

def render_result(num_employees, industry, employees_considering_leaving, employees_leaving_due_to_work_life_balance, estimated_turnover_cost):
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
    st.subheader("Enter the details below to calculate the impact:")
    num_employees = st.number_input("Number of Employees:", min_value=0, step=1, key='input_num_employees')
    industry = st.selectbox("Industry:", options=["Manufacturing", "Social Work/Healthcare", "Luxury Retail", "Hospitality"], key='input_industry')
    return num_employees, industry

def show_popup():
    st.warning("Worried about losing employees? Book a call or recalculate.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("[Book a Discovery Call](https://tidycal.com/janet/discovery-call)", unsafe_allow_html=True)
    with col2:
        if st.button("Recalculate"):
            reset_state()
