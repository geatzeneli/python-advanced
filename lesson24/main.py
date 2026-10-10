from fastapi import FastAPI
from models import Project,Developer

app=FastAPI()
@app.post('/developer')
def create_developer(developer:Developer):
    return{"message":"Developer created successfully", "developer":developer}

@app.post("/project")
def create_project(project:Project):
    return{"message":"Project created successfully!","project":project}

@app.get("/project")
def get_projects():
    developer=Developer(name="Artiol", experience=2)
    sample_project:Project=Project(title="HR management system", description="This is a sample project",
                                   languages=["Python","Javascript","SQL"],lead_developer=developer)

    return {"projects":[sample_project]}