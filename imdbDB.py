import sys
import requests
import secrets
import sqlite3
from typing import Tuple


def get_top_250_data() -> list[dict]:
    api_query = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    response = requests.get(api_query)
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    # json_response is a kinda useless dictionary, but the items element has what we need
    json_response = response.json()
    show_list = json_response["items"]
    return show_list


def report_results(data_to_write: list[dict]):
    with open("output/Output.txt", mode='a') as outputFile:  # open the output file for appending
        for show in data_to_write:
            print(show, file=outputFile)  # write each data item to file
            print("\n", file=outputFile)
            print("===================================================================", file=outputFile)


def get_ratings(top_show_data: list[dict]) -> list[dict]:
    results = []
    api_queries = []
    base_query = f"https://imdb-api.com/en/API/UserRatings/{secrets.secret_key}/"
    wheel_of_time_query = f"{base_query}tt7462410"
    api_queries.append(wheel_of_time_query)
    first_query = f"{base_query}{top_show_data[0]['id']}"
    api_queries.append(first_query)
    fifty_query = f"{base_query}{top_show_data[49]['id']}"
    api_queries.append(fifty_query)
    hundred_query = f"{base_query}{top_show_data[99]['id']}"
    api_queries.append(hundred_query)
    two_hundred = f"{base_query}{top_show_data[199]['id']}"
    api_queries.append(two_hundred)
    for query in api_queries:
        response = requests.get(query)
        if response.status_code != 200:  # if we don't get an ok response we have trouble, skip it
            print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
            continue
        rating_data = response.json()
        results.append(rating_data)
    return results


def open_db(filename: str)->Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


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


def main():
    top_show_data = get_top_250_data()
    ratings_data = get_ratings(top_show_data)
    report_results(ratings_data)
    report_results(top_show_data)
    conn, cur = open_db('output/imdb_db.sqlite')
    setup_db(cur)
    close_db(conn)


if __name__ == '__main__':
    main()
