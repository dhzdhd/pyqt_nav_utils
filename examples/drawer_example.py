import sys

import PyQt6.QtCore as qtc
import PyQt6.QtWidgets as qtw

import pyqt_nav_utils as qtd


class Window(qtw.QDialog):
    def __init__(self) -> None:
        super().__init__(parent=None)
        self.setWindowTitle("Example")
        self.setGeometry(1000, 1000, 2000, 500)

        self.init_widgets()
        self.set_layout()
        self.add_to_layout()

    def init_widgets(self) -> None:
        self.main_frame = qtw.QFrame(self)

        self.content_frame = qtw.QFrame(self.main_frame)
        self.content_frame.setStyleSheet("""background-color: rgb(230, 230, 230)""")
        self.content_frame.setSizePolicy(
            qtw.QSizePolicy(
                qtw.QSizePolicy.Policy.Expanding,
                qtw.QSizePolicy.Policy.Preferred,
            )
        )

        self.button_list = [qtw.QPushButton(f"{_}") for _ in range(5)]

        self.drawer = qtd.Drawer(self.main_frame, 50, 1000)

    def set_layout(self) -> None:
        self.main_layout = qtw.QVBoxLayout(self)
        self.main_layout.setContentsMargins(0, 0, 0, 0)
        self.main_layout.setSpacing(0)

        self.main_frame_layout = qtw.QHBoxLayout(self.main_frame)
        self.main_frame_layout.setContentsMargins(0, 0, 0, 0)
        self.main_frame_layout.setSpacing(0)

        self.drawer.layout().setAlignment(qtc.Qt.AlignmentFlag.AlignTop)

        self.content_frame_layout = qtw.QHBoxLayout(self.content_frame)
        for i in self.button_list:
            self.content_frame_layout.addWidget(i)

    def add_to_layout(self) -> None:
        self.main_layout.addWidget(self.main_frame)

        self.main_frame_layout.addWidget(self.drawer)
        self.main_frame_layout.addWidget(self.content_frame)

        self.setLayout(self.main_layout)


if __name__ == "__main__":
    app = qtw.QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
