from fastapi import FastAPI
import sqlite3
from models import Movie,MovieBase
from typing import Any

app=FastAPI()

def create_connection()->Any:
    '''
    Create the connection between the server and the database
    :return: Connection variable
    '''
    conn=sqlite3.connect('pyadvanced24.db')
    conn.row_factory=sqlite3.Row
    return conn


def create_table():
    connection=create_connection()
    cursor=connection.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS movies(
        ID integer primary key autoincrement
        title text not null,
        director text not null,
        genre text not null,
        year_of_release INTEGER not null
    );
    ''')
    connection.commit()
    connection.close()

@app.post()
def create_movie(movie:MovieBase):
    """
    Stores a new movie to the database
    :param movie: A pydantic model containing the title, director, genre and the year of release of the movie to be created
    :return: int: The ID of the newly created movie stored in the database
    """
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("INSERT INTO movies(title,director,genre,year_of_release) VALUES (?,?,?,?)",
                   (movie.title,movie.director,movie.genre,movie.year_of_release))
    connection.commit()
    movie_id=cursor.lastrowid
    connection.close()
    return movie_id

@app.get("/movies/", response_model=List[models.Movie])
def read_movies()->List[Movie]:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM movies")
    rows=cursor.fetchall()
    connection.close()
    movies=[Movie(id=row[0], title=row[1], director=row[2],genre=row[3],year_of_release=row[4]) for row in rows]
    return movies

@app.get("/movie/{movie_id}",response_model=models.Movie)
def read_movie(movie_id:int)->Movie|None:
    """
    Retrieves a single movie from the database by its ID.
    :param: movie_id The ID of the movie that want to retrieve.
    :return: A movie Model representing the retrieved movie.
    Returns None, if no movies correspond to the id.
    """

    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM movies WHERE id=?",(movie_id,))
    row=cursor.fetchone()
    connection.close()
    if row is None:
        return None
    else:
        return Movie(id=row['ID'],title=row['title'],director=row['director']
                     ,genre=row['genre'],year_of_release=row['year_of_release'])

def update_movie(movie_id:int,movie:Movie)->str:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("update movies set title=?,director=?,genre=?,year_of_release=? where ID=?",
                   (movie.title,movie.director,movie.genre,movie.year_of_release,movie_id))
    connection.commit()
    updated=cursor.rowcount
    connection.close()
    if updated==1:
        return f'One record updated with id: {movie_id}'
    return 'No movies affected!'

def delete_movie(movie_id:int)->str:
    connection = create_connection()
    cursor = connection.cursor()
    cursor.execute("delete from movies where ID=?",(movie_id,))
    connection.commit()
    updated = cursor.rowcount
    connection.close()
    if updated == 1:
        return f'One record updated with id: {movie_id}'
    return 'No movies affected!'



def main():
    create_table()
    movie1=MovieBase(title='Odyssey',director='Nolan',genre='Epik',year_of_release=2026)
    movies=read_movies()
    for movie in movies:
        print(f"{movie.id}.{movie.title} - {movie.year_of_release} directed by {movie.director} with genre: {movie.genre}")
    print(read_movie(movie_id=1))



if __name__=="__main__":
    main()