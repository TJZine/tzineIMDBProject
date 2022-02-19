import sys
import requests
import secrets
import sqlite3
from typing import Tuple


def get_top_250_tv_data() -> list[dict]:
    top_250_tv_query = f"https://imdb-api.com/en/API/Top250TVs/{secrets.secret_key}"
    response = requests.get(top_250_tv_query)
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    # json_response is a kinda useless dictionary, but the item's element has what we need
    json_response = response.json()
    show_list = json_response["items"]
    return show_list


def get_top_250_movie_data() -> list[dict]:
    api_query = f"https://imdb-api.com/en/API/Top250Movies/{secrets.secret_key}"
    response = requests.get(api_query)
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    # json_response is a kinda useless dictionary, but the item's element has what we need
    json_response = response.json()
    show_list = json_response["items"]
    return show_list


def get_most_popular_tv_shows() -> list[dict]:
    api_query = f"https://imdb-api.com/en/API/MostPopularTVs/{secrets.secret_key}"
    response = requests.get(api_query)
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    # json_response is a kinda useless dictionary, but the item's element has what we need
    json_response = response.json()
    show_list = json_response["items"]
    return show_list


def get_most_popular_movies() -> list[dict]:
    api_query = f"https://imdb-api.com/en/API/MostPopularMovies/{secrets.secret_key}"
    response = requests.get(api_query)
    if response.status_code != 200:  # if we don't get an ok response we have trouble
        print(f"Failed to get data, response code:{response.status_code} and error message: {response.reason} ")
        sys.exit(-1)
    # json_response is a kinda useless dictionary, but the item's element has what we need
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


def open_db(filename) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
    db_connection = sqlite3.connect(filename)
    cursor = db_connection.cursor()
    return db_connection, cursor


def close_db(connection: sqlite3.Connection):
    connection.commit()
    connection.close()


#  loop that writes the top 250 shows to the database specified.
def top_250_to_db(cursor: sqlite3.Cursor, show_dict, name):
    for entry in show_dict:
        cursor.execute(f'''INSERT INTO {name} (id, title, full_title, year, crew, imdb_rating,
                                    imdb_rating_count) VALUES (?,?,?,?,?,?,?);''',
                       (entry['id'], entry['title'], entry['fullTitle'],
                        entry['year'], entry['crew'], entry['imDbRating'], entry['imDbRatingCount']))


def most_popular_to_db(cursor: sqlite3.Cursor, show_dict, name):
    for entry in show_dict:
        cursor.execute(f'''INSERT INTO {name} (id, rank, rank_up_down, title, full_title, year, crew, imdb_rating,
                                    imdb_rating_count) VALUES (?,?,?,?,?,?,?,?,?);''',
                       (entry['id'], entry['rank'], entry['rankUpDown'], entry['title'], entry['fullTitle'],
                        entry['year'], entry['crew'], entry['imDbRating'], entry['imDbRatingCount']))


#  make work for any column of the db entries using function input
def find_min_max(ratings_dict) -> list[int]:
    min_rating = 0
    max1 = 0
    max2 = 0
    max3 = 0
    for entry in ratings_dict:
        entry['rankUpDown'] = ''.join(c for c in entry['rankUpDown'] if (c.isnumeric() or c == '-'))
        entry['rankUpDown'] = int(entry['rankUpDown'])
        if entry['rankUpDown'] < min_rating:
            min_rating = entry['rankUpDown']
        elif entry['rankUpDown'] > max1:
            max1 = entry['rankUpDown']
        elif entry['rankUpDown'] > max2:
            max2 = entry['rankUpDown']
        elif entry['rankUpDown'] > max3:
            max3 = entry['rankUpDown']
    min_max_list = [min_rating, max1, max2, max3]
    return min_max_list


def min_max_to_db(cursor: sqlite3.Cursor, ratings_dict, min_max_list, name):
    for entry in ratings_dict:
        if (min_max_list[0] == entry['rankUpDown'] or min_max_list[1] == entry['rankUpDown']
                or min_max_list[2] == entry['rankUpDown'] or min_max_list[3] == entry['rankUpDown']):
            cursor.execute(f'''INSERT INTO {name} (id, rank, rank_up_down, title, full_title, year, crew, imdb_rating,
                                                imdb_rating_count) VALUES (?,?,?,?,?,?,?,?,?);''',
                           (entry['id'], entry['rank'], entry['rankUpDown'], entry['title'], entry['fullTitle'],
                            entry['year'], entry['crew'], entry['imDbRating'], entry['imDbRatingCount']))


def put_in_wheel_of_time(db_cursor: sqlite3.Cursor):
    db_cursor.execute("""INSERT INTO top_250_tv_shows(id, title, full_title, year, crew, imdb_rating, imdb_rating_count)
    VALUES('tt7462410','The Wheel of Time','The Wheel of Time (TV Series 2021– )',2021,'Rosamund Pike, Daniel Henney',
    7.2,85286)""")


#  filter that takes a list of values. used to avoid repeat code in user_ratings_to_db function.
def user_ratings_filter(cursor: sqlite3.Cursor, val_list):
    cursor.execute('''INSERT INTO USER_RATINGS (imdb_id, total_rating, total_rating_votes, ten_rating_percent,
                             ten_rating_votes, nine_rating_percent, nine_rating_votes, eight_rating_percent,
                             eight_rating_votes, seven_rating_percent, seven_rating_votes, six_rating_percent,
                             six_rating_votes, five_rating_percent, five_rating_votes, four_rating_percent,
                             four_rating_votes, three_rating_percent, three_rating_votes, two_rating_percent,
                             two_rating_votes, one_rating_percent, one_rating_votes) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,
                             ?,?,?,?,?,?,?,?,?,?);''', val_list)


#  writes user ratings data to database, if there are no entries for ratings replace with 0's.
def user_ratings_to_db(cursor: sqlite3.Cursor, ratings_dict):
    for entry in ratings_dict:
        if not entry['ratings']:
            user_ratings_filter(cursor, (
                entry['imDbId'], entry['totalRating'], entry['totalRatingVotes'], 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
        else:
            user_ratings_filter(cursor,
                                (entry['imDbId'], entry['totalRating'], entry['totalRatingVotes'],
                                 entry['ratings'][0]['percent'], entry['ratings'][0]['votes'],
                                 entry['ratings'][1]['percent'], entry['ratings'][1]['votes'],
                                 entry['ratings'][2]['percent'], entry['ratings'][2]['votes'],
                                 entry['ratings'][3]['percent'], entry['ratings'][3]['votes'],
                                 entry['ratings'][4]['percent'], entry['ratings'][4]['votes'],
                                 entry['ratings'][5]['percent'], entry['ratings'][5]['votes'],
                                 entry['ratings'][6]['percent'], entry['ratings'][6]['votes'],
                                 entry['ratings'][7]['percent'], entry['ratings'][7]['votes'],
                                 entry['ratings'][8]['percent'], entry['ratings'][8]['votes'],
                                 entry['ratings'][9]['percent'], entry['ratings'][9]['votes']))


#  creates the table in the database for the top 250 shows with the name specified.
def setup_top_250_db(cursor: sqlite3.Cursor, name):
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name}(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    full_title TEXT NOT NULL,
    year TEXT NOT NULL,
    crew TEXT NOT NULL,
    imdb_rating REAL DEFAULT 0,
    imdb_rating_count INTEGER DEFAULT 0
    );''')


def setup_most_popular_db(cursor: sqlite3.Cursor, name):
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name}(
    id TEXT PRIMARY KEY,
    rank INTEGER DEFAULT 0,
    rank_up_down INTEGER DEFAULT 0,
    title TEXT NOT NULL,
    full_title TEXT NOT NULL,
    year TEXT NOT NULL,
    crew TEXT NOT NULL,
    imdb_rating REAL DEFAULT 0,
    imdb_rating_count INTEGER DEFAULT 0
    );''')


#  creates table in database for user ratings data.
def setup_user_ratings_db(cursor: sqlite3.Cursor):
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


#  clears any current tables in the database to avoid unique key errors.
def clear_db(cursor: sqlite3.Cursor):
    cursor.execute("DROP TABLE IF EXISTS TOP_250_TV_SHOWS")
    cursor.execute("DROP TABLE IF EXISTS USER_RATINGS")
    cursor.execute("DROP TABLE IF EXISTS TOP_250_MOVIES")
    cursor.execute("DROP TABLE IF EXISTS MOST_POPULAR_MOVIES")
    cursor.execute("DROP TABLE IF EXISTS MOST_POPULAR_TV_SHOWS")
    cursor.execute("DROP TABLE IF EXISTS min_max_most_popular_movies")


def main():
    erase_file = open("output/Output.txt", "w")  # erases any previous text in the file
    erase_file.close()

    top_show_data = get_top_250_tv_data()
    popular_show_data = get_most_popular_tv_shows()
    top_movie_data = get_top_250_movie_data()
    popular_movie_data = get_most_popular_movies()
    ratings_data = get_ratings(top_show_data)
    min_max_list = find_min_max(popular_movie_data)

    report_results(ratings_data)
    report_results(top_show_data)
    report_results(popular_show_data)
    report_results(popular_movie_data)

    conn, cur = open_db('output/imdb_db.sqlite')
    clear_db(cur)

    setup_top_250_db(cur, 'top_250_tv_shows')
    setup_most_popular_db(cur, 'most_popular_tv_shows')
    setup_top_250_db(cur, 'top_250_movies')
    setup_most_popular_db(cur, 'most_popular_movies')
    setup_user_ratings_db(cur)
    setup_most_popular_db(cur, 'min_max_most_popular_movies')

    top_250_to_db(cur, top_show_data, 'top_250_tv_shows')
    put_in_wheel_of_time(cur)
    most_popular_to_db(cur, popular_show_data, 'most_popular_tv_shows')
    top_250_to_db(cur, top_movie_data, 'top_250_movies')
    most_popular_to_db(cur, popular_movie_data, 'most_popular_movies')
    user_ratings_to_db(cur, ratings_data)
    min_max_to_db(cur, popular_movie_data, min_max_list, 'min_max_most_popular_movies')

    close_db(conn)


if __name__ == '__main__':
    main()
