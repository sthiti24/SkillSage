import streamlit as st


def about():
    st.subheader("About Project")
    st.write("This application provides comprehensive insights into job market trends, focusing on skills, location, and salary statistics for specific job roles across different countries.")
    st.write(" Leveraging the Adzuna API, a powerful job market data source, it offers up-to-date and accurate information to job seekers, employers, and market analysts.")
    url = "https://github.com/sthiti24/SkillSage"
    st.write("Project repository [link](%s)" % url)

    st.subheader("About Me")
    st.write("I am Sthiti Pragyan Panda, a student at IIIT Bhubaneswar, currently in my 4th year of a BTech degree. I am passionate about web development and machine learning. While searching for an internship, I encountered numerous job roles, each demanding a unique set of skills. The array of requirements was overwhelming and left me quite confused. This experience sparked an idea in me to create a project that consolidates and clarifies the skills needed for different job roles, all in one place.")
    st.write("Connect with me on [Linkedin](%s)" %
             "https://www.linkedin.com/in/sthiti-pragyan-panda-67a349222/")
