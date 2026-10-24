import sqlite3
from models import Movie,MovieBase
from typing import Any

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



def main():
    movie1=MovieBase(title='Odyssey',director='Nolan',genre='Epik',year_of_release=2026)
    print(create_movie(movie1))
if __name__=="__main__":
    main()