from utils.get_country_code import get_country_code
import pandas as pd
import os
from dotenv import load_dotenv
import requests
# import streamlit as st

load_dotenv()

ADZUNA_API_ID = os.getenv('ADZUNA_API_ID')
ADZUNA_API_KEY = os.getenv('ADZUNA_API_KEY')


def data_fetcher(job_title, country):
    country_code = get_country_code(country)
    url = f"https://api.adzuna.com/v1/api/jobs/{country_code}/search/1"
    params = {
        'app_id': ADZUNA_API_ID,
        'app_key': ADZUNA_API_KEY,
        'results_per_page': 1000,
        'what': job_title
    }
    response = requests.get(url, params=params)
    data = response.json()
    jobs = data.get('results', [])
    df = pd.DataFrame(jobs)
    loc_data = pd.DataFrame({
        'latitude': df.latitude,
        'longitude': df.longitude
    })
    # st.write(df.columns)
    if 'salary_max' in df.columns and 'company' in df.columns:
        csData = df[['salary_max', 'company']]
    else:
        csData = pd.DataFrame(columns=['salary_max', 'company'])

    return [df.description, loc_data, csData]
