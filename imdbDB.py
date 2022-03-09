import sqlite3
import getAPIData
import databaseSetup
from typing import Tuple


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


#  writes the most popular shows/movies to the database.
def most_popular_to_db(cursor: sqlite3.Cursor, show_dict, name):
    for entry in show_dict:
        cursor.execute(f'''INSERT INTO {name} (id, rank, rank_up_down, title, full_title, year, crew, imdb_rating,
                                    imdb_rating_count) VALUES (?,?,?,?,?,?,?,?,?);''',
                       (entry['id'], entry['rank'], entry['rankUpDown'], entry['title'], entry['fullTitle'],
                        entry['year'], entry['crew'], entry['imDbRating'], entry['imDbRatingCount']))


#  make work for any column of the db entries using function input
def find_min_max(ratings_dict) -> list[int]:
    rank_change_array = []
    min_max_list = []
    for entry in ratings_dict:
        entry['rankUpDown'] = ''.join(c for c in entry['rankUpDown'] if (c.isnumeric() or c == '-'))
        entry['rankUpDown'] = int(entry['rankUpDown'])
        rank_change_array.append(entry['rankUpDown'])
    rank_change_array.sort(reverse=True)
    min_max_list.append(rank_change_array[len(rank_change_array) - 1])
    for i in range(3):
        min_max_list.append(rank_change_array[i])
    return min_max_list


def min_max_to_db(cursor: sqlite3.Cursor, ratings_dict, min_max_list, name):
    for entry in ratings_dict:
        if (min_max_list[0] == entry['rankUpDown'] or min_max_list[1] == entry['rankUpDown']
                or min_max_list[2] == entry['rankUpDown'] or min_max_list[3] == entry['rankUpDown']):
            cursor.execute(f'''INSERT INTO {name} (ttid, rank, rank_up_down, title, full_title, year, crew, imdb_rating,
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


def main():
    #  query data is a list of dictionaries for the queried data.
    query_data = getAPIData.get_movie_and_show_data()
    top_show_data = query_data[0]  # top 250 show data
    top_movie_data = query_data[1]  # top 250 movie data
    popular_show_data = query_data[2]  # most popular show data
    popular_movie_data = query_data[3]  # most popular movie data
    ratings_data = getAPIData.get_ratings(top_show_data)  # user ratings data for specified shows
    min_max_list = find_min_max(popular_movie_data)

    conn, cur = open_db('output/imdb_db.sqlite')
    databaseSetup.clear_db(cur)

    databaseSetup.setup_top_250_db(cur, 'top_250_tv_shows')
    databaseSetup.setup_most_popular_db(cur, 'most_popular_tv_shows')
    databaseSetup.setup_top_250_db(cur, 'top_250_movies')
    databaseSetup.setup_most_popular_db(cur, 'most_popular_movies')
    databaseSetup.setup_user_ratings_db(cur)
    databaseSetup.setup_min_max_db(cur, 'min_max_most_popular_movies')

    top_250_to_db(cur, top_show_data, 'top_250_tv_shows')
    put_in_wheel_of_time(cur)
    most_popular_to_db(cur, popular_show_data, 'most_popular_tv_shows')
    top_250_to_db(cur, top_movie_data, 'top_250_movies')
    most_popular_to_db(cur, popular_movie_data, 'most_popular_movies')
    user_ratings_to_db(cur, ratings_data)
    min_max_to_db(cur, popular_movie_data, min_max_list, 'min_max_most_popular_movies')

    cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS')
    most_popular_tv_data = cur.fetchall()
    print(type(most_popular_tv_data))
    for i in range(len(most_popular_tv_data)):
        print(most_popular_tv_data[i][0], most_popular_tv_data[i][1], most_popular_tv_data[i][2],
              most_popular_tv_data[i][3], most_popular_tv_data[i][4], most_popular_tv_data[i][5],
              most_popular_tv_data[i][6], most_popular_tv_data[i][7], most_popular_tv_data[i][8])
        print(type(most_popular_tv_data[i][1]))
        print(type(most_popular_tv_data[i][2]))
    close_db(conn)

    print("ROW FACTORY:")

    conn = sqlite3.connect('output/imdb_db.sqlite')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS')
    most_popular_tv_data = cur.fetchall()
    for data in most_popular_tv_data:
        print(data['id'], data['rank'], data['rank_up_down'], data['title'], data['full_title'], data['year'],
              data['crew'], data['imdb_rating'], data['imdb_rating_count'])
        print(type(data['rank']))
        print(type(data['rank_up_down']))


if __name__ == '__main__':
    main()
