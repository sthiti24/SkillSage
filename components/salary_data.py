import streamlit as st
import pandas as pd
import streamlit.components.v1 as components


def salary_data(sal_data):
    highest_salary = sal_data.max()
    lowest_salary = sal_data.min()
    mean_salary = sal_data.mean()
    median_salary = sal_data.median()

    sal_data_table = pd.DataFrame({
        'Metric': ['Highest Salary', 'Lowest Salary', 'Average Salary', 'Median Salary'],
        'Value': [f"${highest_salary:.2f}k", f"${lowest_salary:.2f}k",
                  f"${mean_salary:.2f}k", f"${median_salary:.2f}k"]
    })

    html_table = """
    <style>
    table {
        //border-collapse: collapse;
        border: 1px solid #B2BEB5;
        width: 100%;
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

    html_table += sal_data_table.to_html(index=False)
    components.html(html_table, height=250)
    # st.write(html_table, unsafe_allow_html=True)
