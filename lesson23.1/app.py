import streamlit as st
import requests
import pandas as pd

st.title("Project Management App")
st.header("Add a Developer")
dev_name=st.text_input("Developer Name")
dev_experience=st.number_input("Experience (Years)",min_value=0,max_value=50,value=0,key="ex1")

if st.button("Create Developer"):
    dev_data={"name":dev_name,"experience":dev_experience}
    response=requests.post("http://127.0.0.1:8000/project",json=dev_data)
    st.json({"json":response.json(),"status":response.status_code})

st.header("Add a Project")
proj_title=st.text_input("Project Title")
proj_desc=st.text_area("Project Description")
proj_langs=st.text_input("Languages Used (comma seperated)")
lead_dev_name=st.text_input("Developer Name")
lead_dev_experience=st.number_input("Experience (Years)",min_value=0,max_value=50,value=0,key="ex2")

if st.button("Create Project"):
    lead_dev_data={"name":lead_dev_name,"experience":lead_dev_experience}
    proj_data={"title":proj_title,"description":proj_desc,
               "languages":proj_langs.split(","),
               "lead_developer":lead_dev_data}
    response=requests.post("http://127.0.0.1:8000/project",json=proj_data)
    st.json({"json":response.json(),"status":response.status_code})

st.header("Project Dashboard")
if st.button("Get Projects"):
    response=requests.get("http://127.0.0.1:8000/project")
    projects_data=response.json()['projects']

    if projects_data:
        projects_df=pd.DataFrame(projects_data)
        st.subheader("Projects Overview")
        st.dataframe(projects_df)

        st.subheader("Project Details")
        for project in projects_data:
            st.markdown(f"### {project['title']}")
            st.markdown(f"**Description** {project['description']}")
            st.markdown(f"Languages Used: {", ".join(project['languages'])}")
            st.markdown(f"Developer Name: {project['lead_developer']['name']}")
            st.markdown("----")
        else:
            st.warning("No Projects Found!")


