from PyQt5.QtWidgets import *
import sys
import pyqtgraph as pg
import sqlite3
import imdbDB
from PyQt5.QtChart import QChart, QChartView, QValueAxis, QBarCategoryAxis, QBarSet, QBarSeries
from PyQt5.Qt import Qt
from PyQt5.QtGui import QPainter
shows_up = 0
shows_down = 0
movies_up = 0
movies_down = 0


def find_biggest_movers():
    global shows_up
    global shows_down
    global movies_up
    global movies_down
    shows_up = 0
    shows_down = 0
    movies_up = 0
    movies_down = 0
    conn = sqlite3.connect('output/imdb_db.sqlite')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute('SELECT * FROM MOST_POPULAR_TV_SHOWS')
    top_tv_data = cur.fetchall()
    tv_rank_change_array = []
    for data in top_tv_data:
        data_type = data['rank_up_down']
        if isinstance(data_type, str):
            mod_data = ''.join(c for c in data['rank_up_down'] if (c.isnumeric() or c == '-'))
            mod_data = int(mod_data)
            tv_rank_change_array.append(mod_data)
        else:
            tv_rank_change_array.append(data['rank_up_down'])
    for entry in tv_rank_change_array:
        if entry > 0:
            shows_up = shows_up + 1
        elif entry < 0:
            shows_down = shows_down + 1
    cur.execute('SELECT * FROM MOST_POPULAR_MOVIES')
    top_movie_data = cur.fetchall()
    movie_rank_change_array = []
    for data in top_movie_data:
        data_type = data['rank_up_down']
        if isinstance(data_type, str):
            mod_data = ''.join(c for c in data['rank_up_down'] if (c.isnumeric() or c == '-'))
            mod_data = int(mod_data)
            movie_rank_change_array.append(mod_data)
        else:
            movie_rank_change_array.append(data['rank_up_down'])
    for entry in movie_rank_change_array:
        if entry > 0:
            movies_up = movies_up + 1
        elif entry < 0:
            movies_down = movies_down + 1
    imdbDB.close_db(conn)


class GraphWindow2(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movers Graph")
        self.setGeometry(100, 100, 800, 700)
        self.setup_window()
        self.show()

    def setup_window(self):
        global shows_up
        global shows_down
        global movies_up
        global movies_down
        find_biggest_movers()
        set0 = QBarSet('Pop shows Moving down')
        set1 = QBarSet('Pop shows moving up')
        set2 = QBarSet('Pop movies moving up')
        set3 = QBarSet('Pop movies moving down')
        set0.append(shows_down)
        set1.append(shows_up)
        set2.append(movies_down)
        set3.append(movies_up)
        changes_series = QBarSeries()
        changes_series.append(set0)
        changes_series.append(set1)
        changes_series.append(set2)
        changes_series.append(set3)

        movers_chart = QChart()
        movers_chart.addSeries(changes_series)
        movers_chart.setTitle("Number of Movers in Most Popular Data")
        movers_chart.setAnimationOptions(QChart.SeriesAnimations)

        labels = [str(shows_down), str(shows_up), str(movies_down), str(movies_up)]
        print(labels)
        axis_x = QBarCategoryAxis()
        axis_x.setRange(labels[0], labels[3])
        axis_x.append(labels)
        axis_y = QValueAxis()
        axis_y.setRange(0, 60)

        movers_chart.addAxis(axis_x, Qt.AlignBottom)
        movers_chart.addAxis(axis_y, Qt.AlignLeft)
        movers_chart.legend().setVisible(True)
        movers_chart.legend().setAlignment(Qt.AlignBottom)
        movers_chart_view = QChartView(movers_chart)
        self.setCentralWidget(movers_chart_view)


class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movers Graph")
        self.setGeometry(100, 100, 600, 500)
        self.setup_window()
        self.show()

    def setup_window(self):
        global shows_up
        global shows_down
        global movies_up
        global movies_down
        find_biggest_movers()
        widget = QWidget()
        plot = pg.plot()
        y = [shows_down, shows_up, movies_down, movies_up]
        x = [1, 2, 3, 4]
        bargraph = pg.BarGraphItem(x=x, height=y, width=.5, brush='g')
        plot.addItem(bargraph)
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(plot)
        self.setCentralWidget(widget)
