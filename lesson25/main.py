from fastapi import FastAPI
from database import read_movie,read_movies,create_movie,delete_movie,update_movie

app=FastAPI()

@app.get("/")
def read_root():
    return{"message":"Welcome to the movies CRUD API."}