import streamlit as st
import streamlit.components.v1 as components
import pandas as pd


def company_data(company_salary_data):

    html_table = """
    <style>
    table {
        //border-collapse: collapse;
        width: 100%;
        border: 1px solid #B2BEB5;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 12px;
        text-align: left;
    }
    th {
        background-color: #4682B4;
        color: white;
    }
    tr:nth-child(even) {
        background-color: #f2f2f2;
    }
    </style>
    """

    top_5_companies = company_salary_data.head(5)

    top_5_companies = pd.DataFrame({
        'Company': top_5_companies.company,
        'Salary': top_5_companies.salary
    })

    top_5_companies['Salary'] = top_5_companies['Salary'].apply(
        lambda x: f"${x:.2f}k")

    html_table += top_5_companies.to_html(index=False)
    components.html(html_table, height=300)

    # st.markdown(html_table_companies, unsafe_allow_html=True)
