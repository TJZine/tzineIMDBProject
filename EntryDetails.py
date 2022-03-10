from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit
import sqlite3
import imdbDB


class EntryDetails(QWidget):

    def __init__(self, data_to_show: dict):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM TOP_250_TV_SHOWS')
        top_tv_data = cur.fetchall()
        imdbDB.close_db(conn)
        curr_entry = None
        for data in top_tv_data:
            if data['id'] == self.data:
                curr_entry = data
        self.setWindowTitle("Top 250 Entry Data")
        self.setGeometry(750, 100, 1000, 200)
        label = QLabel(self)
        label.setText("id:")
        label.move(25, 50)
        id_display = QLineEdit(curr_entry['id'], self)
        id_display.move(60, 50)
        label = QLabel("title:", self)
        label.move(25, 100)
        title = QLineEdit(str(curr_entry["title"]), self)
        title.move(60, 100)
        label = QLabel("fullTitle:", self)
        label.move(230, 50)
        full_title = QLineEdit(str(curr_entry["full_title"]), self)
        full_title.move(280, 50)
        label = QLabel("year:", self)
        label.move(230, 100)
        year = QLineEdit(str(curr_entry["year"]), self)
        year.move(280, 100)
        label = QLabel("crew:", self)
        label.move(460, 50)
        crew = QLineEdit(str(curr_entry["crew"]), self)
        crew.move(540, 50)
        label = QLabel("imDbRating:", self)
        label.move(460, 100)
        rating = QLineEdit(str(curr_entry["imdb_rating"]), self)
        rating.move(540, 100)
        label = QLabel("imDbRatingCount:", self)
        label.move(670, 75)
        rating_count = QLineEdit(str(curr_entry["imdb_rating_count"]), self)
        rating_count.move(780, 75)


class MovieEntryDetails(QWidget):

    def __init__(self, data_to_show: dict):
        super().__init__()
        self.data = data_to_show
        self.setup_window()

    def setup_window(self):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM TOP_250_MOVIES')
        top_movie_data = cur.fetchall()
        imdbDB.close_db(conn)
        curr_entry = None
        for data in top_movie_data:
            if data['id'] == self.data:
                curr_entry = data
        self.setWindowTitle("Top 250 Entry Data")
        self.setGeometry(750, 100, 1000, 200)
        label = QLabel(self)
        label.setText("id:")
        label.move(25, 50)
        id_display = QLineEdit(curr_entry['id'], self)
        id_display.move(60, 50)
        label = QLabel("title:", self)
        label.move(25, 100)
        title = QLineEdit(str(curr_entry["title"]), self)
        title.move(60, 100)
        label = QLabel("fullTitle:", self)
        label.move(230, 50)
        full_title = QLineEdit(str(curr_entry["full_title"]), self)
        full_title.move(280, 50)
        label = QLabel("year:", self)
        label.move(230, 100)
        year = QLineEdit(str(curr_entry["year"]), self)
        year.move(280, 100)
        label = QLabel("crew:", self)
        label.move(460, 50)
        crew = QLineEdit(str(curr_entry["crew"]), self)
        crew.move(540, 50)
        label = QLabel("imDbRating:", self)
        label.move(460, 100)
        rating = QLineEdit(str(curr_entry["imdb_rating"]), self)
        rating.move(540, 100)
        label = QLabel("imDbRatingCount:", self)
        label.move(670, 75)
        rating_count = QLineEdit(str(curr_entry["imdb_rating_count"]), self)
        rating_count.move(780, 75)
