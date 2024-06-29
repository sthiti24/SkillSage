import streamlit as st
from components.prop_charts import prop_charts


def skills_stats(job_title, country, job_descriptions):
    st.markdown("##### Showing skill details for " +
                job_title+" roles in "+country)
    st.markdown("<br><br>", unsafe_allow_html=True)
    prop_charts(job_descriptions)
