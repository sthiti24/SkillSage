import streamlit as st


def sidebar():
    st.sidebar.title("Enter job details")
    job_title = st.sidebar.selectbox("Select role:", [
        "Software Developer", "Software Engineer", "Cyber security", "Data analyst", "Data scientist"])
    country = st.sidebar.selectbox("Select country:", ["United Kingdom", "United States", "Austria", "Australia", "Belgium", "Brazil", "Canada",
                                                       "Switzerland", "Germany", "Spain", "France", "India", "Italy", "Mexico", "Netherlands", "New Zealand", "Poland", "South Africa", "Singapore"])
    data = [job_title, country]
    return data
