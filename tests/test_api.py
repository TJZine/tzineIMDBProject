import sqlite3
import imdbDB


def test_top_250_tv():
    result = imdbDB.get_top_250_data()
    assert len(result) == 250


def db_test_setup(cursor: sqlite3.Cursor):
    cursor.execute('''CREATE TABLE IF NOT EXISTS test_db(
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    full_title TEXT NOT NULL,
    year TEXT NOT NULL,
    crew TEXT NOT NULL,
    imdb_rating REAL DEFAULT 0,
    imdb_rating_count INTEGER DEFAULT 0
    );''')


def dict_test() -> dict:
    show_test_dict = {'id': 'tt0707077', 'rank': '2222', 'title': 'test_show_title',
                      'fullTitle': 'full_show_title (2000)', 'year': '2000',
                      'image': 'www.testURL.com', 'crew': 'actor 1, actor 2, actor 3',
                      'imDbRating': '6.7', 'imDbRatingCount': '22222'}
    return show_test_dict


def test_db():
    entry = dict_test()
    conn, cur = imdbDB.open_db('output/test_db.sqlite')
    db_test_setup(cur)
    cur.execute('''INSERT INTO TEST_DB (id, title, full_title, year, crew, imdb_rating,
                                        imdb_rating_count) VALUES (?,?,?,?,?,?,?);''',
                (entry['id'], entry['title'], entry['fullTitle'],
                 entry['year'], entry['crew'], entry['imDbRating'], entry['imDbRatingCount']))
    conn.commit()
    cur.execute("SELECT id FROM components WHERE id = ?", ('tt0707077',))
    data = cur.fetchone()
    imdbDB.close_db(conn)
    assert data is not None
