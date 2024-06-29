import streamlit as st
import pandas as pd
from components.salary_data import salary_data
from components.company_data import company_data


def salary_stats(job_title, country, csData):

    if (len(csData) == 0):
        st.markdown("##### No data for salary and companies are available for " +
                    job_title+" role in "+country)
        return

    def is_not_null_object(obj):
        return obj is not None and obj != {} and obj != [] and obj != ''

    filtered_df = csData[csData['company'].apply(is_not_null_object)]
    if (len(filtered_df) == 0):
        st.markdown("##### No data for salary and companies are available for " +
                    job_title+" role in "+country)
        return
    clean_df = filtered_df.dropna(subset=['salary_max'])

    n = len(clean_df)

    if (n < 5):
        st.markdown("##### No data for salary and companies are available for " +
                    job_title+" role in "+country)
        return
    else:
        company_names = []
        for c in clean_df.company:
            company_names.append(c['display_name'])

        company_salary_data = pd.DataFrame({
            "salary": clean_df.salary_max,
            "company": company_names
        })

    company_salary_data = company_salary_data.sort_values(
        by='salary', ascending=False)

    sal_data = company_salary_data.salary

    salary_data_clean = pd.to_numeric(sal_data.dropna(), errors='coerce')

    if len(salary_data_clean) == 0:
        st.markdown(
            f"##### No valid salary data available for {job_title} role in {country}")
        return

    st.markdown("##### Salary statistics for "+job_title+" role in "+country)
    salary_data(salary_data_clean)
    st.markdown("##### Top high paying companies")
    company_data(company_salary_data)
