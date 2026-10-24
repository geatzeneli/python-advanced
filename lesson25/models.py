from pydantic import BaseModel

class MovieBase(BaseModel):
    title:str
    director:str
    genre:str
    year_of_release:int

class Movie(MovieBase):
    id: int

