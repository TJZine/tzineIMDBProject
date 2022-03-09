import imdbDB
import sqlite3
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QHBoxLayout, QTableWidget,\
    QPushButton, QMessageBox, QMainWindow, QVBoxLayout, QWidget


class RankShowWindow(QTableWidget):
    def __init__(self):
        super(RankShowWindow, self).__init__()
        loadUi("imdbDBTest.ui", self)
        self.setup_window()
        self.get_sorted_pop_tv_data()

    def setup_window(self):
        self.setWindowTitle("Most Popular TV Shows: sorted by rank")
        self.setGeometry(300, 100, 400, 500)
        self.setColumnWidth(0, 50)
        self.show()

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
        self.setWindowTitle("Most Popular TV Shows: sorted by rank")
        self.setGeometry(300, 100, 400, 500)
        self.setColumnWidth(0, 50)
        self.show()

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
