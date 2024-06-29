
from components.sidebar import sidebar
from utils.data_fetcher import data_fetcher
from page.skills_stats import skills_stats
from page.location_stats import location_stats
from page.salary_stats import salary_stats
from page.about import about
import streamlit as st
import pandas as pd
import pydeck as pdk
import os
from dotenv import load_dotenv
load_dotenv()

MAP_BOX_API_KEY = os.getenv('MAP_BOX_API_KEY')
pdk.settings.mapbox_api_key = MAP_BOX_API_KEY

st.set_page_config(layout="wide")

st.title("SkillSage")

job_title, country = sidebar()


choices = ["Skills Stats", "Location Stats",
           "Salary Stats", "About"]

# Define the active choice
if 'active_choice' not in st.session_state:
    st.session_state['active_choice'] = choices[0]

active_choice = st.session_state['active_choice']

st.markdown("""
    <style>
    .custom-button {
        cursor: pointer;
        display: inline-block;
        padding: 10px 20px;
        margin: 0 2px; /* Reduced margin on left and right to decrease the gap */
        border: 1px solid #ccc;
        border-radius: 5px;
        background-color: white;
        color: black;
        transition: background-color 0.3s, color 0.3s, border-color 0.3s;
        text-align: center;
        width: auto; /* Adjust width automatically based on content */
    }
    .custom-button:hover {
        background-color: #eee;
    }
    .custom-button-active {
        background-color: #007bff;
        color: white;
        border-color: #007bff;
    }
    </style>
""", unsafe_allow_html=True)

# Render the buttons in a horizontal line with decreased gap
cols = st.columns([1, 1, 1, 1])  # Adjust the list to control the spacing
for idx, choice in enumerate(choices):
    button_class = "custom-button"
    if choice == active_choice:
        button_class += " custom-button-active"

    with cols[idx]:
        if st.button(choice, key=choice, help=f"Click to view {choice} stats"):
            st.session_state['active_choice'] = choice
            active_choice = choice

st.markdown("<hr style='height:2px;border-width:0;color:#4682B4;background-color:#4682B4'>",
            unsafe_allow_html=True)

job_descriptions, loc_data, csData = data_fetcher(
    job_title, country)


# Display the selected page
if active_choice == "Skills Stats":
    skills_stats(job_title, country, job_descriptions)
elif active_choice == "Location Stats":
    location_stats(job_title, country, loc_data)
elif active_choice == "Salary Stats":
    salary_stats(job_title, country, csData)
elif active_choice == "About":
    about()
