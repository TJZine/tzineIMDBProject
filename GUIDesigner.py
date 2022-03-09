import sqlite3
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
import imdbDB


class DesignerWindow(QDialog):
    def __init__(self):
        super(DesignerWindow, self).__init__()
        loadUi("imdbDBTest.ui", self)
        self.tableWidget.setColumnWidth(0, 50)
        self.get_data()


    def get_data(self):
        most_popular_tv_data = []
        conn = sqlite3.connect('output/imdb_db.sqlite')
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS')
        raw_most_popular_tv_data = cur.fetchall()
        imdbDB.close_db(conn)
        self.tableWidget.setRowCount(len(raw_most_popular_tv_data))
        row = 0
        for data in raw_most_popular_tv_data:
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


def main():
    app = QApplication(sys.argv)
    mainWindow = DesignerWindow()
    widget = QtWidgets.QStackedWidget()
    widget.addWidget((mainWindow))
    widget.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
