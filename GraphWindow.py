import imdbDB
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib as plt
from PyQt5.QtWidgets import QMainWindow, QWidget, QGridLayout
import pyqtgraph as pg
import sqlite3
plt.use('Qt5Agg')


def biggest_movers_loop(imdb_data) -> list[int]:
    rank_change_array = []
    for data in imdb_data:
        data_type = data['rank_up_down']
        if isinstance(data_type, str):
            mod_data = ''.join(c for c in data['rank_up_down'] if (c.isnumeric() or c == '-'))
            mod_data = int(mod_data)
            rank_change_array.append(mod_data)
        else:
            rank_change_array.append(data['rank_up_down'])
    return rank_change_array


def find_biggest_movers2(table1, table2, db) -> list[int]:
    shows_up = 0
    shows_down = 0
    movies_up = 0
    movies_down = 0
    conn = sqlite3.connect(db)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table1}")
    top_tv_data = cur.fetchall()
    tv_change_count = biggest_movers_loop(top_tv_data)
    for entry in tv_change_count:
        if entry > 0:
            shows_up = shows_up + 1
        elif entry < 0:
            shows_down = shows_down + 1
    cur.execute(f"SELECT * FROM {table2}")
    top_movie_data = cur.fetchall()
    movie_change_count = biggest_movers_loop(top_movie_data)
    for entry in movie_change_count:
        if entry > 0:
            movies_up = movies_up + 1
        elif entry < 0:
            movies_down = movies_down + 1
    count_list = [shows_up, shows_down, movies_up, movies_down]
    imdbDB.close_db(conn)
    return count_list


class GraphWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Movers Graph")
        self.setGeometry(100, 100, 600, 500)
        self.setup_window()
        self.show()

    def setup_window(self):
        count_list = find_biggest_movers2('MOST_POPULAR_TV_SHOWS', 'MOST_POPULAR_MOVIES', 'output/imdb_db.sqlite')
        widget = QWidget()
        plot = pg.plot()
        y = [count_list[0], count_list[1], count_list[2], count_list[3]]
        x = [1, 2, 3, 4]
        bargraph = pg.BarGraphItem(x=x, height=y, width=.5, brush='g')
        plot.addItem(bargraph)
        layout = QGridLayout()
        widget.setLayout(layout)
        layout.addWidget(plot)
        self.setCentralWidget(widget)


class PieChartWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        title = "Count of Movies/Shows moving up and down in Popularity"
        self.setWindowTitle(title)
        self.setGeometry(400, 400, 700, 400)
        self.setup_window()

    def setup_window(self):
        canvas = Canvas(self, width=8, height=4)
        canvas.move(0, 0)


def make_autopct(x):
    def my_autopct(pct):
        total = sum(x)
        val = int(round(pct * total / 100.0))
        return '{p:.2f}%  ({v:d})'.format(p=pct, v=val)

    return my_autopct


class Canvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=5, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        self.plot()

    def plot(self):
        count_list = find_biggest_movers2('MOST_POPULAR_TV_SHOWS', 'MOST_POPULAR_MOVIES', 'output/imdb_db.sqlite')
        x = [count_list[0], count_list[1], count_list[2], count_list[3]]
        labels = ['Popular shows down', 'Popular shows up', 'Popular movies down', 'Popular movies up']
        ax = self.figure.add_subplot(111)
        ax.pie(x, labels=labels, autopct=make_autopct(x))
