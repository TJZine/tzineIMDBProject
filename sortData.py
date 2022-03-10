import imdbDB
import sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget
import EntryDetails


def get_db_entry(ttid: str):
    conn = sqlite3.connect('output/imdb_db.sqlite')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM TOP_250_TV_SHOWS')
    top_tv_data = cur.fetchall()
    imdbDB.close_db(conn)
    for data in top_tv_data:
        if data['id'] == ttid:
            return data


class RankShowWindow(QTableWidget):
    def __init__(self):
        super(RankShowWindow, self).__init__()
        loadUi("imdbDBTest.ui", self)
        self.setup_window()
        self.get_sorted_pop_tv_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular TV Shows: sorted by rank")
        self.resizeColumnToContents(0)
        self.tableWidget.cellClicked.connect(self.check_top_ratings_data)
        self.show()

    def check_top_ratings_data(self):
        curr_row = self.tableWidget.currentRow()
        curr_col = self.tableWidget.currentColumn()
        print("Row %d and Column %d was clicked" % (curr_row, curr_col))
        cell_val = self.tableWidget.item(curr_row, 0).text()
        print(cell_val)
        full_entry = get_db_entry(cell_val)
        print(full_entry)
        if full_entry is not None:
            self.data_window = EntryDetails.EntryDetails(cell_val)
            self.data_window.show()

    def get_sorted_pop_tv_data(self):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS ORDER BY rank')
        sorted_most_popular_tv_data = cur.fetchall()
        imdbDB.close_db(conn)
        self.tableWidget.setRowCount(len(sorted_most_popular_tv_data))
        row = 0
        for data in sorted_most_popular_tv_data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data['rank'])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data['rank_up_down'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['title']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data['full_title']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(data['year']))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(data['crew']))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data['imdb_rating'])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data['imdb_rating_count'])))
            row = row + 1


class RankUpDownShowWindow(QTableWidget):
    def __init__(self):
        super(RankUpDownShowWindow, self).__init__()
        loadUi("imdbDBTest.ui", self)
        self.setup_window()
        self.get_rank_up_down_pop_tv_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular TV Shows: sorted by rankUpDown")
        self.resizeColumnToContents(0)
        self.tableWidget.cellClicked.connect(self.check_top_ratings_data)
        self.show()

    def check_top_ratings_data(self):
        curr_row = self.tableWidget.currentRow()
        curr_col = self.tableWidget.currentColumn()
        print("Row %d and Column %d was clicked" % (curr_row, curr_col))
        cell_val = self.tableWidget.item(curr_row, 0).text()
        print(cell_val)
        full_entry = self.get_db_entry(cell_val)
        print(full_entry)
        if full_entry is not None:
            self.data_window = EntryDetails.EntryDetails(cell_val)
            self.data_window.show()

    def get_db_entry(self, ttid: str):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM TOP_250_TV_SHOWS')
        top_tv_data = cur.fetchall()
        imdbDB.close_db(conn)
        for data in top_tv_data:
            if data['id'] == ttid:
                return data

    def get_rank_up_down_pop_tv_data(self):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS ORDER BY rank_up_down')
        sorted_most_popular_tv_data = cur.fetchall()
        imdbDB.close_db(conn)
        self.tableWidget.setRowCount(len(sorted_most_popular_tv_data))
        row = 0
        for data in sorted_most_popular_tv_data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data['rank'])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data['rank_up_down'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['title']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data['full_title']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(data['year']))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(data['crew']))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data['imdb_rating'])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data['imdb_rating_count'])))
            row = row + 1


class RankMovieWindow(QTableWidget):
    def __init__(self):
        super(RankMovieWindow, self).__init__()
        loadUi("imdbDBTest.ui", self)
        self.setup_window()
        self.get_sorted_pop_movie_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular Movies: sorted by rank")
        self.resizeColumnToContents(0)
        self.tableWidget.cellClicked.connect(self.check_top_ratings_data)
        self.show()

    def check_top_ratings_data(self):
        curr_row = self.tableWidget.currentRow()
        curr_col = self.tableWidget.currentColumn()
        print("Row %d and Column %d was clicked" % (curr_row, curr_col))
        cell_val = self.tableWidget.item(curr_row, 0).text()
        print(cell_val)
        full_entry = self.get_db_entry(cell_val)
        print(full_entry)
        if full_entry is not None:
            self.data_window = EntryDetails.MovieEntryDetails(cell_val)
            self.data_window.show()

    def get_db_entry(self, ttid: str):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM TOP_250_MOVIES')
        top_movie_data = cur.fetchall()
        imdbDB.close_db(conn)
        for data in top_movie_data:
            if data['id'] == ttid:
                return data

    def get_sorted_pop_movie_data(self):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_MOVIES ORDER BY rank')
        sorted_most_popular_movie_data = cur.fetchall()
        imdbDB.close_db(conn)
        self.tableWidget.setRowCount(len(sorted_most_popular_movie_data))
        row = 0
        for data in sorted_most_popular_movie_data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data['rank'])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data['rank_up_down'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['title']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data['full_title']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(data['year']))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(data['crew']))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data['imdb_rating'])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data['imdb_rating_count'])))
            row = row + 1


class RankUpDownMovieWindow(QTableWidget):
    def __init__(self):
        super(RankUpDownMovieWindow, self).__init__()
        loadUi("imdbDBTest.ui", self)
        self.setup_window()
        self.get_rank_up_down_pop_movie_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular Movies: sorted by rankUpDown")
        self.resizeColumnToContents(0)
        self.tableWidget.cellClicked.connect(self.check_top_ratings_data)
        self.show()

    def check_top_ratings_data(self):
        curr_row = self.tableWidget.currentRow()
        curr_col = self.tableWidget.currentColumn()
        print("Row %d and Column %d was clicked" % (curr_row, curr_col))
        cell_val = self.tableWidget.item(curr_row, 0).text()
        print(cell_val)
        full_entry = self.get_db_entry(cell_val)
        print(full_entry)
        if full_entry is not None:
            self.data_window = EntryDetails.MovieEntryDetails(cell_val)
            self.data_window.show()

    def get_db_entry(self, ttid: str):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM TOP_250_MOVIES')
        top_movie_data = cur.fetchall()
        imdbDB.close_db(conn)
        for data in top_movie_data:
            if data['id'] == ttid:
                return data

    def get_rank_up_down_pop_movie_data(self):
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_MOVIES ORDER BY rank_up_down')
        sorted_most_popular_movie_data = cur.fetchall()
        imdbDB.close_db(conn)
        self.tableWidget.setRowCount(len(sorted_most_popular_movie_data))
        row = 0
        for data in sorted_most_popular_movie_data:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(str(data['rank'])))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(str(data['rank_up_down'])))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['title']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data['full_title']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(data['year']))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(data['crew']))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(data['imdb_rating'])))
            self.tableWidget.setItem(row, 8, QtWidgets.QTableWidgetItem(str(data['imdb_rating_count'])))
            row = row + 1
