import streamlit as st
from components.bubblemap import bubblemap


def location_stats(job_title, country, loc_data):
    print("1 2 3")
    st.markdown("##### Displays bubbles indicating cities in the " +
                country+" with "+job_title+" job postings")
    bubblemap(loc_data, country)
