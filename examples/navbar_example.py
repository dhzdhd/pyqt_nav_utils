import sys

import PyQt6.QtCore as qtc
import PyQt6.QtGui as qtg
import PyQt6.QtWidgets as qtw

import pyqt_nav_utils as qtu


class Window(qtw.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Example")
        self.setGeometry(1000, 1000, 2000, 500)

        self.main_frame = qtw.QFrame(self)
        self.stacked_widget = qtw.QStackedWidget(self.main_frame)
        self.navbar = qtu.NavigationBar(self.main_frame, 50, 0)
        self.navbar.add_item(qtu.NavigationBarItem("Home"))
        self.navbar.add_item(
            qtu.NavigationBarItem(
                pixmap=self.style()
                .standardIcon(qtw.QStyle.StandardPixmap.SP_DirIcon)
                .pixmap(qtc.QSize(30, 30))
            )
        )
        self.navbar.add_item(
            qtu.NavigationBarItem(
                "Settings",
                pixmap=self.style()
                .standardIcon(qtw.QStyle.StandardPixmap.SP_MediaPlay)
                .pixmap(qtc.QSize(10, 10)),
            )
        )

        self.main_layout = qtw.QVBoxLayout(self)
        self.main_frame_layout = qtw.QVBoxLayout(self.main_frame)

        self.init_widgets()
        self.set_layout()
        self.add_to_layout()

    def init_widgets(self) -> None:
        self.stacked_widget.setStyleSheet("""background-color: rgb(230, 230, 230)""")
        self.stacked_widget.setContentsMargins(10, 10, 10, 10)

        for _ in range(3):
            button = qtw.QPushButton(f"{_}")
            button.setFont(qtg.QFont([], 100))
            self.stacked_widget.addWidget(button)
        self.stacked_widget.setCurrentIndex(0)

        self.navbar._items[0]._button.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(0)
        )
        self.navbar._items[1]._button.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(1)
        )
        self.navbar._items[2]._button.clicked.connect(
            lambda: self.stacked_widget.setCurrentIndex(2)
        )

    def set_layout(self) -> None:
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.main_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.main_frame_layout.setSpacing(0)

    def add_to_layout(self) -> None:
        self.main_layout.addWidget(self.main_frame)

        self.main_frame_layout.addWidget(self.stacked_widget)
        self.main_frame_layout.addWidget(self.navbar)

        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = qtw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
