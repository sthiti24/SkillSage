import streamlit as st
import pandas as pd
import plotly.express as px


def sort_dict_by_value(dictionary):
    return dict(sorted(dictionary.items(), key=lambda x: x[1], reverse=True))


def plot_skill_trends(skills_counter):
    df = pd.DataFrame(list(skills_counter.items()), columns=['Skill', 'Count'])
    total_count = df['Count'].sum()
    df['Percentage'] = (df['Count'] / total_count) * 100
    df = df.sort_values('Percentage', ascending=False)
    top_n = 10
    df = df.head(top_n)
    df['Percentage'] = df['Percentage'].round(0)
    fig = px.bar(df, x='Skill', y='Percentage',
                 color_discrete_sequence=['#4682B4'])

    fig.update_layout(
        xaxis_title=None,
        yaxis_title=None,
        yaxis_ticksuffix="%",
        xaxis_tickangle=-45,
        margin=dict(t=30, b=0, l=0, r=0),
        font=dict(family="Arial", size=12),
        height=300
    )

    st.plotly_chart(fig, use_container_width=False)
