import requests
import secrets
import sqlite3
from typing import Tuple

def api_connect():  # connects to the IMDB top 250TV shows api
    return requests.get('https://imdb-api.com/API/Top250TVs/' + secrets.api_key)


def get_user_data(movie_id):  # takes imdbID and returns user rating data
    return requests.get('https://imdb-api.com/en/API/UserRatings/' + secrets.api_key + '/' + movie_id)


def write_to_file(top_shows_list):
    with open("output/shows.txt", "a") as writeFile:
        writeFile.write(top_shows_list)  # open shows.txt to write to file


def open_db(filename: str)->Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


def test_db():
    connection, cursor = open_db('demo_db.sqlite')
    print(type(connection))
    close_db(connection)


def setup_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS top_250_tv_shows(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    full_title TEXT NOT NULL,
    year TEXT NOT NULL,
    crew TEXT NOT NULL,
    imdb_rating REAL DEFAULT 0,
    imdb_rating_count INTEGER DEFAULT 0
    );''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_ratings(
    imdb_id TEXT PRIMARY KEY,
    total_rating INTEGER DEFAULT 0,
    total_rating_votes INTEGER DEFAULT 0,
    ten_rating_percent REAL DEFAULT 0,
    ten_rating_votes INTEGER DEFAULT 0,
    nine_rating_percent REAL DEFAULT 0,
    nine_rating_votes INTEGER DEFAULT 0,
    eight_rating_percent REAL DEFAULT 0,
    eight_rating_votes INTEGER DEFAULT 0,
    seven_rating_percent REAL DEFAULT 0,
    seven_rating_votes INTEGER DEFAULT 0,
    six_rating_percent REAL DEFAULT 0,
    six_rating_votes INTEGER DEFAULT 0,
    five_rating_percent REAL DEFAULT 0,
    five_rating_votes INTEGER DEFAULT 0,
    four_rating_percent REAL DEFAULT 0,
    four_rating_votes INTEGER DEFAULT 0,
    three_rating_percent REAL DEFAULT 0,
    three_rating_votes INTEGER DEFAULT 0,
    two_rating_percent REAL DEFAULT 0,
    two_rating_votes INTEGER DEFAULT 0,
    one_rating_percent REAL DEFAULT 0,
    one_rating_votes INTEGER DEFAULT 0,
    FOREIGN KEY (imdb_id) REFERENCES top_250_tv_shows (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
    );''')


if __name__ == '__main__':
    eraseFile = open("output/shows.txt", "w")  # erases any previous text in the file
    eraseFile.close()

    imdb_API = api_connect()  # connect to imdb API
    print(imdb_API.status_code)

    # prints rank 1,50,100,200 and wheels of time user ratings to shows.txt and console for testing
    write_to_file("User Ratings:" + "\n")
    rank1_rated_show = get_user_data('tt5491994')
    write_to_file(str(rank1_rated_show.json()) + "\n")  # convert dictionary entry to string to write to shows.txt
    rank50_rated_show = get_user_data('tt2297757')
    write_to_file(str(rank50_rated_show.json()) + "\n")
    rank100_rated_show = get_user_data('tt0286486')
    write_to_file(str(rank100_rated_show.json()) + "\n")
    rank200_rated_show = get_user_data('tt1492966')
    write_to_file(str(rank200_rated_show.json()) + "\n")
    wheel_of_time_rating = get_user_data('tt7462410')
    write_to_file(str(wheel_of_time_rating.json()) + "\n")


    # writing top 250 shows to console and shows.txt
    write_to_file("Top 250 Shows:" + "\n")
    text_value = imdb_API.text
    value_list = text_value.split('},{')
    value_list[0] = value_list[0][11:]
    for n in value_list:
        write_to_file(n + "\n")
    conn, cur = open_db('imdb_db.sqlite')
    setup_db(cur)
    close_db(conn)
