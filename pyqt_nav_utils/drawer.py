from __future__ import annotations

from PyQt6.QtCore import QPropertyAnimation, Qt
from PyQt6.QtGui import QFont
from PyQt6.QtWidgets import (
    QWidget,
    QLayout,
    QFrame,
    QSplitter,
    QVBoxLayout,
    QSizePolicy,
    QPushButton,
)


class Drawer(QWidget):
    """
    An animated Drawer widget
    """

    def __init__(
        self, parent: QWidget, drawer_width: int, expanded_width: int | None = None
    ) -> None:
        super().__init__(parent)

        assert drawer_width >= 50, "Drawer width cannot be lesser than 50."
        assert (
            expanded_width <= self.window().width() / 2
        ), "Expanded width cannot be greater than the half the window width."

        self._drawer_width = drawer_width
        self._expanded_width = expanded_width
        self._is_expanded = False
        self._layout = QVBoxLayout(self)
        self._menu_button = QPushButton(self)

        self._init_widgets()
        self._add_to_layout()
        self._add_functionality()

    @property
    def is_expanded(self) -> bool:
        return self._is_expanded

    def _init_widgets(self) -> None:
        self.setMinimumWidth(self._drawer_width)
        self.setMaximumWidth(self._drawer_width)
        self.setGeometry(0, 0, self._drawer_width, self.parentWidget().height())
        self.setSizePolicy(
            QSizePolicy(
                QSizePolicy.Policy.MinimumExpanding, QSizePolicy.Policy.Preferred
            )
        )

        self._menu_button.setText("≡")
        self._menu_button.setFont(QFont("", 20, 10))
        self._menu_button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                border-style: outset;
                border-color: transparent;
            }
            QPushButton:hover {
                background-color: rgb(230, 230, 230);
            }
            QPushButton:pressed {
                background-color: rgb(210, 210, 210);
                color: #21a1f1;
            }
            """
        )

    def _add_to_layout(self) -> None:
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addWidget(self._menu_button)

        self.setLayout(self._layout)

    def _add_functionality(self) -> None:
        self._menu_button.clicked.connect(self._add_animation)

    def _add_animation(self) -> None:
        self._anim = QPropertyAnimation(self, b"maximumWidth")
        self._anim.setDuration(300)

        if self.maximumWidth() == self._expanded_width:
            self._anim.setEndValue(self._drawer_width)
        else:
            self._anim.setEndValue(self._expanded_width)

        self._is_expanded = not self._is_expanded
        self._anim.start()


class DraggableDrawer(Drawer):
    """
    A draggable animated Drawer widget.
    To be used with QWidgets.QSplitter as the parent widget.
    """

    def __init__(
        self, parent: QWidget | QLayout, drawer_width: int, expanded_width: int
    ):
        super().__init__(parent, drawer_width, expanded_width)

        assert (
            self.parentWidget() == QSplitter
        ), "Intended to be used with a parent QtWidgets.QSplitter widget only"

        self.setMaximumWidth(drawer_width)
        self.setSizePolicy(
            QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        )
