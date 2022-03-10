import CrossReferenceDB
import sortData
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QVBoxLayout, QWidget


class SortTVButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("TV Sort Buttons")
        sort_by_rank_button = QPushButton("Sorted by: Rank", self)
        sort_by_rank_button.clicked.connect(self.rank_shows_window)
        sort_by_rank_up_down_button = QPushButton("Sorted by: RankUpDown", self)
        sort_by_rank_up_down_button.clicked.connect(self.rank_up_down_window)
        cross_ref_button = QPushButton("Shows in Top 250 and Most Popular", self)
        cross_ref_button.clicked.connect(self.cross_ref_shows_window)
        layout = QHBoxLayout()
        layout.stretch(1)
        layout.addWidget(sort_by_rank_button)
        layout.addWidget(sort_by_rank_up_down_button)
        layout.addWidget(cross_ref_button)
        v_layout = QVBoxLayout()
        v_layout.stretch(1)
        v_layout.addLayout(layout)
        self.setLayout(v_layout)
        self.setGeometry(300, 300, 300, 150)
        self.show()

    def rank_shows_window(self):
        self.w = sortData.RankShowWindow()
        self.w.show()

    def rank_up_down_window(self):
        self.w = sortData.RankUpDownShowWindow()
        self.w.show()

    def cross_ref_shows_window(self):
        self.w = CrossReferenceDB.CrossRefShowWindow()
        self.w.show()


class SortMovieButtons(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.setWindowTitle("Movie Sort Buttons")
        sort_by_rank_button = QPushButton("Sorted by: Rank", self)
        sort_by_rank_button.clicked.connect(self.rank_shows_window)
        sort_by_rank_up_down_button = QPushButton("Sorted by: RankUpDown", self)
        sort_by_rank_up_down_button.clicked.connect(self.rank_up_down_window)
        cross_ref_button = QPushButton("Movies in Top 250 and Most Popular", self)
        cross_ref_button.clicked.connect(self.cross_ref_movies_window)
        layout = QHBoxLayout()
        layout.stretch(1)
        layout.addWidget(sort_by_rank_button)
        layout.addWidget(sort_by_rank_up_down_button)
        layout.addWidget(cross_ref_button)
        v_layout = QVBoxLayout()
        v_layout.stretch(1)
        v_layout.addLayout(layout)
        self.setLayout(v_layout)
        self.setGeometry(300, 300, 300, 150)
        self.show()

    def rank_shows_window(self):
        self.w = sortData.RankMovieWindow()
        self.w.show()

    def rank_up_down_window(self):
        self.w = sortData.RankUpDownMovieWindow()
        self.w.show()

    def cross_ref_movies_window(self):
        self.w = CrossReferenceDB.CrossRefMovieWindow()
        self.w.show()
