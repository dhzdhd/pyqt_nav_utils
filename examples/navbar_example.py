import sys

from PyQt6.QtCore import QSize
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import QApplication, QDialog, QFrame, QPushButton, QStackedWidget, QStyle, QVBoxLayout

from pyqtnavutils import NavigationBar, NavigationBarItem


class Window(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.setWindowTitle("Example")
        self.setGeometry(1000, 1000, 2000, 500)

        self.mainFrame = QFrame(self)
        self.stackedWidget = QStackedWidget(self.mainFrame)
        self.navbar = NavigationBar(self.mainFrame, 50)
        self.navbar.addItem(NavigationBarItem("Home"))
        self.navbar.addItem(
            NavigationBarItem(
                pixmap=self.style()
                .standardIcon(QStyle.StandardPixmap.SP_DirIcon)
                .pixmap(QSize(30, 30))
            )
        )
        self.navbar.addItem(
            NavigationBarItem(
                "Settings",
                pixmap=self.style()
                .standardIcon(QStyle.StandardPixmap.SP_MediaPlay)
                .pixmap(QSize(10, 10)),
            )
        )

        self.mainLayout = QVBoxLayout(self)
        self.mainFrameLayout = QVBoxLayout(self.mainFrame)

        self.initWidgets()
        self.initLayout()
        self.addToLayout()

    def initWidgets(self) -> None:
        self.stackedWidget.setStyleSheet("""background-color: rgb(230, 230, 230)""")
        self.stackedWidget.setContentsMargins(10, 10, 10, 10)

        for _ in range(3):
            button = QPushButton(f"{_}")
            button.setFont(QFont([], 100))
            self.stackedWidget.addWidget(button)
        self.stackedWidget.setCurrentIndex(0)

        self.navbar.getItems[0].getButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(0)
        )
        self.navbar.getItems[1].getButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(1)
        )
        self.navbar.getItems[2].getButton.clicked.connect(
            lambda: self.stackedWidget.setCurrentIndex(2)
        )

    def initLayout(self) -> None:
        self.mainLayout.setContentsMargins(0, 0, 0, 0)
        self.mainLayout.setSpacing(0)

        self.mainFrameLayout.setContentsMargins(0, 0, 0, 0)
        self.mainFrameLayout.setSpacing(0)

    def addToLayout(self) -> None:
        self.mainLayout.addWidget(self.mainFrame)

        self.mainFrameLayout.addWidget(self.stackedWidget)
        self.mainFrameLayout.addWidget(self.navbar)

        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())
