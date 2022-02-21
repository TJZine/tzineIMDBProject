import sqlite3
import imdbDBSprint3


def popular_dict_test() -> list[dict]:
    popular_test_dict = [
        {'id': 'tt0707077', 'rank': '2222', 'rankUpDown': '2', 'title': 'test_show_title',
         'fullTitle': 'full_show_title (2000)', 'year': '2000',
         'image': 'www.testURL.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 6.7, 'imDbRatingCount': 22222},
        {'id': 'tt2278757', 'rank': '2223', 'rankUpDown': '74', 'title': 'show_title_2',
         'fullTitle': 'full_show_title_2 (2011)', 'year': '2011',
         'image': 'www.testURL2.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 6.5, 'imDbRatingCount': 17052},
        {'id': 'tt2274527', 'rank': '1001', 'rankUpDown': '51', 'title': 'show_title_3',
         'fullTitle': 'full_show_title_3 (2012)', 'year': '2012',
         'image': 'www.testURL3.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 6.4, 'imDbRatingCount': 18073},
        {'id': 'tt2356557', 'rank': '1003', 'rankUpDown': '11', 'title': 'show_title_4',
         'fullTitle': 'full_show_title_4 (2007)', 'year': '2007',
         'image': 'www.testURL5.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 7.2, 'imDbRatingCount': 15012},
        {'id': 'tt2415755', 'rank': '524', 'rankUpDown': '-322', 'title': 'show_title_7',
         'fullTitle': 'full_show_title_7 (1999)', 'year': '1999',
         'image': 'www.testURL2.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 6.8, 'imDbRatingCount': 10045},
        {'id': 'tt2438224', 'rank': '954', 'rankUpDown': '655', 'title': 'show_title_9',
         'fullTitle': 'full_show_title_9 (2022)', 'year': '2022',
         'image': 'www.testURL2.com', 'crew': 'actor 1, actor 2, actor 3',
         'imDbRating': 7.4, 'imDbRatingCount': 4511}
    ]
    return popular_test_dict


def test_min_max():
    min_max = popular_dict_test()
    min_max_list = imdbDBSprint3.find_min_max(min_max)
    assert (min_max[4]['rankUpDown'] == min_max_list[0] and min_max[5]['rankUpDown'] == min_max_list[1]
            and min_max[1]['rankUpDown'] == min_max_list[2] and min_max[2]['rankUpDown'] == min_max_list[3])


def test_most_popular_db():
    entry = popular_dict_test()
    min_max_list = imdbDBSprint3.find_min_max(entry)
    conn = sqlite3.connect('most_popular_db_test.sqlite')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('DROP TABLE IF EXISTS MOST_POPULAR_DB_TEST')
    imdbDBSprint3.setup_most_popular_db(cur, 'most_popular_db_test')
    imdbDBSprint3.most_popular_to_db(cur, entry, 'most_popular_db_test')
    cur.execute("SELECT tbl_name FROM sqlite_master WHERE type ='table' AND name = 'most_popular_db_test'")
    table_name = cur.fetchone()
    assert table_name[0] == 'most_popular_db_test'
    cur.execute('SELECT * FROM MOST_POPULAR_DB_TEST')
    data = cur.fetchone()
    assert (data['id'] == entry[0]['id'] and data['rank'] == int(entry[0]['rank']) and
            data['rank_up_down'] == int(entry[0]['rankUpDown']) and data['title'] == entry[0]['title'] and
            data['full_title'] == entry[0]['fullTitle'] and data['year'] == entry[0]['year'] and
            data['crew'] == entry[0]['crew'] and data['imdb_rating'] == entry[0]['imDbRating'] and
            data['imdb_rating_count'] == entry[0]['imDbRatingCount'])
    cur.execute('DROP TABLE IF EXISTS MIN_MAX_DB_TEST')
    imdbDBSprint3.setup_min_max_db(cur, 'min_max_db_test')
    imdbDBSprint3.min_max_to_db(cur, entry, min_max_list, 'min_max_db_test')
    cur.execute("SELECT 'most_popular_db_test' AS constraint_table, pragma.'from' AS constraint_column, "
                "pragma.'table' AS referenced_table, pragma.'to' AS referenced_column FROM pragma_foreign_key_list("
                "'most_popular_db_test') AS pragma")
    cur.execute("SELECT sql FROM sqlite_master WHERE name = 'min_max_db_test'")
    foreign_key = cur.fetchone()
    assert "FOREIGN KEY (ttid) REFERENCES most_popular_movies (id)" in foreign_key[0]
    imdbDBSprint3.close_db(conn)