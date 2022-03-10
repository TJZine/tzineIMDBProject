from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QHBoxLayout, QVBoxLayout
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
        id_display = QLineEdit(curr_entry['id'], self)
        label.move(65, 60)
        label = QLabel("title:", self)
        title = QLineEdit(str(curr_entry["title"]), self)
        label.move(205, 60)
        label = QLabel("fullTitle:", self)
        full_title = QLineEdit(str(curr_entry["full_title"]), self)
        label.move(335, 60)
        label = QLabel("year:", self)
        year = QLineEdit(str(curr_entry["year"]), self)
        label.move(485, 60)
        label = QLabel("crew:", self)
        crew = QLineEdit(str(curr_entry["crew"]), self)
        label.move(625, 60)
        label = QLabel("imDbRating:", self)
        rating = QLineEdit(str(curr_entry["imdb_rating"]), self)
        label.move(745, 60)
        label = QLabel("imDbRatingCount:", self)
        rating_count = QLineEdit(str(curr_entry["imdb_rating_count"]), self)
        label.move(865, 60)
        layout = QHBoxLayout()
        layout.stretch(1)
        layout.addWidget(id_display)
        layout.addWidget(title)
        layout.addWidget(full_title)
        layout.addWidget(year)
        layout.addWidget(crew)
        layout.addWidget(rating)
        layout.addWidget(rating_count)
        v_layout = QVBoxLayout()
        v_layout.stretch(1)
        v_layout.addLayout(layout)
        self.setLayout(v_layout)


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
        id_display = QLineEdit(curr_entry['id'], self)
        label.move(65, 60)
        label = QLabel("title:", self)
        title = QLineEdit(str(curr_entry["title"]), self)
        label.move(205, 60)
        label = QLabel("fullTitle:", self)
        full_title = QLineEdit(str(curr_entry["full_title"]), self)
        label.move(335, 60)
        label = QLabel("year:", self)
        year = QLineEdit(str(curr_entry["year"]), self)
        label.move(485, 60)
        label = QLabel("crew:", self)
        crew = QLineEdit(str(curr_entry["crew"]), self)
        label.move(625, 60)
        label = QLabel("imDbRating:", self)
        rating = QLineEdit(str(curr_entry["imdb_rating"]), self)
        label.move(745, 60)
        label = QLabel("imDbRatingCount:", self)
        rating_count = QLineEdit(str(curr_entry["imdb_rating_count"]), self)
        label.move(865, 60)
        layout = QHBoxLayout()
        layout.stretch(1)
        layout.addWidget(id_display)
        layout.addWidget(title)
        layout.addWidget(full_title)
        layout.addWidget(year)
        layout.addWidget(crew)
        layout.addWidget(rating)
        layout.addWidget(rating_count)
        v_layout = QVBoxLayout()
        v_layout.stretch(1)
        v_layout.addLayout(layout)
        self.setLayout(v_layout)
