from __future__ import annotations

from PyQt6.QtCore import QPropertyAnimation
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QWidget,
    QLayout,
    QFrame,
    QStackedWidget,
    QVBoxLayout,
    QSizePolicy,
    QPushButton,
)


class NavigationBar(QFrame):
    def __init__(self, parent) -> None:
        super().__init__(parent)
