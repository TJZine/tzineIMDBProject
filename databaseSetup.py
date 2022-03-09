import sqlite3


#  creates the tables in the database for the top 250 shows and movies with the name specified.
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


#  creates the tables in the database for the most popular shows and movies with the name specified.
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


#  creates table for top 3 positive changes in popularity and biggest negative change for most pop movies.
def setup_min_max_db(cursor: sqlite3.Cursor, name):
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {name}(
    min_max_key INTEGER PRIMARY KEY,
    ttid TEXT NOT NULL,
    rank INTEGER DEFAULT 0,
    rank_up_down INTEGER DEFAULT 0,
    title TEXT NOT NULL,
    full_title TEXT NOT NULL,
    year TEXT NOT NULL,
    crew TEXT NOT NULL,
    imdb_rating REAL DEFAULT 0,
    imdb_rating_count INTEGER DEFAULT 0,
    FOREIGN KEY (ttid) REFERENCES most_popular_movies (id)
    ON DELETE CASCADE ON UPDATE NO ACTION
    );''')


#  creates table in database for user ratings data.
def setup_user_ratings_db(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS user_ratings(
    ratings_key INTEGER PRIMARY KEY,
    imdb_id TEXT NOT NULL,
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
