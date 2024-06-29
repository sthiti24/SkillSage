import streamlit as st
from utils.data_fetcher import data_fetcher
from utils.extract_skills import extract_skills
from utils.plot_skill_trends import plot_skill_trends

languages = [
    "Java", "HTML", "CSS", "JavaScript", "Python", "C++", "SQL", "C", "C#",
    "Assembly language", "PHP", "R", "GO", "MATLAB", "Swift", "Delphi",
    "Ruby", "Perl", "Rust", "Scratch", "SAS", "Kotlin", "Julia", "Lua",
    "Fortran", "COBOL", "Lisp", "Ada", "Dart", "Scala", "Prolog", "D",
    "PL/SQL", "Bash", "PowerShell", "Haskell", "Logo",
    "TypeScript", "Objective-C", "VB.NET", "F#", "Groovy", "Erlang",
    "Clojure", "OCaml", "Racket", "Scheme", "VHDL", "Verilog", "Elixir",
    "CoffeeScript", "Apex", "ABAP", "Elm", "Crystal", "Pascal", "Smalltalk",
    "Nim", "Tcl", "ActionScript", "Forth", "LabVIEW", "Awk", "VBScript",
    "Rebol", "Hack", "Solidity", "Clarion", "Eiffel", "OpenCL", "CUDA"
]

software_tools = [
    "Git", "Gitlab", "Tableau", "Power BI", "Docker", "NetBeans", "Selenium",
    "Collaborator", "Visual Studio Code", "AWS", "Azure", "GCP", "Jira",
    "IntelliJ IDEA", "Apache", "Dreamweaver", "Jenkins", "Trello", "Eclipse",
    "GitHub", "Bitbucket", "Kubernetes", "Slack", "Microsoft Teams",
    "Confluence", "Postman", "SonarQube", "Grafana", "Prometheus",
    "Elasticsearch", "Kibana", "Logstash", "Terraform", "Ansible",
    "VMware", "VirtualBox", "Wireshark", "Fiddler", "Notepad++",
    "Sublime Text", "Atom", "PyCharm", "WebStorm", "Android Studio",
    "Xcode", "Unity", "Blender", "Adobe Photoshop", "Adobe Illustrator",
    "MATLAB", "R Studio", "Jupyter Notebook", "Anaconda", "MongoDB Compass"
]

packages = [
    "React.js", "Angular", "Vue.js", "Express.js", "Django", "Ruby on Rails",
    "ASP.NET Core", "Spring Boot", "Laravel", "Flask", "React Native",
    "Flutter", "Xamarin", "Ionic", "Cordova", "Bootstrap", "Tailwind CSS",
    "Material-UI", "Semantic UI", "Foundation", "Redux", "MobX", "Vuex",
    "NgRx", "Jest", "Mocha", "Jasmine", "Selenium", "Cypress", "TensorFlow",
    "PyTorch", "Scikit-learn", "Pandas", "NumPy", "Docker", "Kubernetes",
    "Ansible", "Terraform", "Jenkins", "Hibernate", "Entity Framework",
    "Sequelize", "SQLAlchemy", "GraphQL", "FastAPI", "Swagger", "Unity",
    "Unreal Engine", "Godot"
]


def prop_charts(jobs_description):

    if len(jobs_description) == 0:
        st.write("No job listings found.")
        return

    languages_counter = extract_skills(jobs_description, languages)
    tools_counter = extract_skills(jobs_description, software_tools)
    packages_counter = extract_skills(jobs_description, packages)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("###### Languages Proportion")
        plot_skill_trends(languages_counter)

    with col2:
        st.markdown("###### Software Tools Proportion")
        plot_skill_trends(tools_counter)

    with col3:
        st.markdown("###### Libraries Proportion")
        plot_skill_trends(packages_counter)
