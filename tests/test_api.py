import sqlite3
import imdbDBSprint3


#  tests retrieval of top 250 tv shows data, tests length of the returned result is 250.


def test_top_250_tv():
    result = imdbDBSprint3.get_top_250_tv_data()
    assert len(result) == 250


def dict_test() -> list[dict]:
    show_test_dict = [{'id': 'tt0707077', 'rank': '2222', 'title': 'test_show_title',
                       'fullTitle': 'full_show_title (2000)', 'year': '2000',
                       'image': 'www.testURL.com', 'crew': 'actor 1, actor 2, actor 3',
                       'imDbRating': 6.7, 'imDbRatingCount': 22222},
                      {'id': 'tt2278757', 'rank': '2223', 'title': 'show_title_2',
                       'fullTitle': 'full_show_title_2 (2011)', 'year': '2011',
                       'image': 'www.testURL2.com', 'crew': 'actor 1, actor 2, actor 3',
                       'imDbRating': 6.5, 'imDbRatingCount': 17052}]
    return show_test_dict


#  creates new database db_test and tests setup database and top_250_tv_db methods from imdbDB.py.
def test_db():
    entry = dict_test()
    conn = sqlite3.connect('db_test.sqlite')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS TEST_DB')
    imdbDBSprint3.setup_top_250_db(cur, 'test_db')
    imdbDBSprint3.top_250_to_db(cur, entry, 'test_db')
    cur.execute('SELECT * FROM test_db')
    data = cur.fetchone()
    imdbDBSprint3.close_db(conn)
    assert (data['id'] == entry[0]['id'] and data['title'] == entry[0]['title'] and
            data['full_title'] == entry[0]['fullTitle'] and data['year'] == entry[0]['year'] and
            data['crew'] == entry[0]['crew'] and data['imdb_rating'] == entry[0]['imDbRating'] and
            data['imdb_rating_count'] == entry[0]['imDbRatingCount'])
