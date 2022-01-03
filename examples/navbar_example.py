import pyqt_nav_utils as qtu
import PyQt6.QtCore as qtc
import PyQt6.QtWidgets as qtw
import sys


class Window(qtw.QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Example")
        self.setGeometry(1000, 1000, 2000, 500)

        self.main_frame = qtw.QFrame(self)
        self.content_frame = qtw.QFrame(self.main_frame)
        # self.button_list = [qtu.NavigationBarItem(f"{_}") for _ in range(5)]
        self.navbar = qtu.NavigationBar(self.main_frame, 50, 0)
        self.navbar.add_item(qtu.NavigationBarItem("Home"))
        self.navbar.add_item(qtu.NavigationBarItem("Maps"))
        self.navbar.add_item(qtu.NavigationBarItem("Settings"))

        self.main_layout = qtw.QVBoxLayout(self)
        self.main_frame_layout = qtw.QVBoxLayout(self.main_frame)

        self.init_widgets()
        self.set_layout()
        self.add_to_layout()

    def init_widgets(self) -> None:
        self.content_frame.setStyleSheet("""background-color: rgb(230, 230, 230)""")

    def set_layout(self) -> None:
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.main_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.main_frame_layout.setSpacing(0)

        self.content_frame_layout = qtw.QHBoxLayout(self.content_frame)
        for _ in range(10):
            self.content_frame_layout.addWidget(qtw.QPushButton('e'))

    def add_to_layout(self) -> None:
        self.main_layout.addWidget(self.main_frame)

        self.main_frame_layout.addWidget(self.content_frame)
        self.main_frame_layout.addWidget(self.navbar)

        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = qtw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
