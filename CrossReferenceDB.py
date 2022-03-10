import imdbDB
import sqlite3
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidget


def get_db_entry(ttid: str, table: str, db: str):
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table}")
    top_tv_data = cur.fetchall()
    imdbDB.close_db(conn)
    for data in top_tv_data:
        if data['id'] == ttid:
            return data


def cross_ref(table1, table2, db_name) -> list:
    conn = sqlite3.connect(db_name)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table1}")
    most_popular_data = cur.fetchall()
    cur.execute(f"SELECT * FROM {table2}")
    top_data = cur.fetchall()
    imdbDB.close_db(conn)
    ref_entry = []
    for pop_entry in most_popular_data:
        for top_250_entry in top_data:
            if pop_entry['id'] == top_250_entry['id']:
                ref_entry.append(top_250_entry)
    return ref_entry


class CrossRefShowWindow(QTableWidget):
    def __init__(self):
        super(CrossRefShowWindow, self).__init__()
        loadUi("imdbDBTop250.ui", self)
        self.setup_window()
        self.insert_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular TV Shows found in Top 250 Shows")
        self.resizeColumnToContents(0)
        self.show()

    def insert_data(self):
        shows = cross_ref('MOST_POPULAR_TV_SHOWS', 'TOP_250_TV_SHOWS', 'output/imdb_db.sqlite')
        self.tableWidget.setRowCount(len(shows))
        row = 0
        for data in shows:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data['title']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data['full_title']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['year']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data['crew']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data['imdb_rating'])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data['imdb_rating_count'])))
            row = row + 1


class CrossRefMovieWindow(QTableWidget):
    def __init__(self):
        super(CrossRefMovieWindow, self).__init__()
        loadUi("imdbDBTop250.ui", self)
        self.setup_window()
        self.insert_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular Movies found in Top 250 Movies")
        self.resizeColumnToContents(0)
        self.show()

    def insert_data(self):
        movies = cross_ref('MOST_POPULAR_MOVIES', 'TOP_250_MOVIES', 'output/imdb_db.sqlite')
        self.tableWidget.setRowCount(len(movies))
        row = 0
        for data in movies:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data['id']))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data['title']))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data['full_title']))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data['year']))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data['crew']))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(str(data['imdb_rating'])))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(data['imdb_rating_count'])))
            row = row + 1
