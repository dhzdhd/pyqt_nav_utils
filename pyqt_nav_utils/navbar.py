from __future__ import annotations

from PyQt6.QtGui import QIcon, QPixmap
from PyQt6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QSequentialAnimationGroup, Qt
from PyQt6.QtWidgets import QAbstractButton, QHBoxLayout, QSizePolicy, QFrame, QStackedLayout, QWidget, QSpacerItem, QLabel, QRadioButton, QVBoxLayout, QPushButton


class NavigationBar(QWidget):
    """An animated NavigationBar widget"""

    def __init__(self, parent: QWidget, height: int, default: int) -> None:
        super().__init__(parent)

        assert height >= 50, "NavigationBar height cannot be lesser than 50."

        self._height = height
        self._items = []
        self._layout = QHBoxLayout(self)

        self._init_widgets()
        self._add_to_layout()

    @property
    def get_items(self) -> list[NavigationBarItem]:
        return self._items

    def add_item(self, item: NavigationBarItem) -> None:
        self._items.append(item)
        self._layout.addWidget(item)
        self._layout.addSpacerItem(QSpacerItem(0, 0, hPolicy=QSizePolicy.Policy.MinimumExpanding))

    def _init_widgets(self) -> None:
        self.setFixedHeight(self._height)

    def _add_to_layout(self) -> None:
        self._layout.setContentsMargins(0, 0, 0, 0)
        self._layout.addSpacerItem(QSpacerItem(0, 0, hPolicy=QSizePolicy.Policy.MinimumExpanding))
        self.setLayout(self._layout)

    def _animate(self, widget: QAbstractButton) -> None:
        self._anim1 = QPropertyAnimation(widget, b"pos")
        self._anim1.setDuration(100)
        self._anim1.setEasingCurve(QEasingCurve.Type.BezierSpline)
        self._anim1.setStartValue(QPoint(widget.x(), widget.y()))
        self._anim1.setEndValue(QPoint(widget.x(), widget.y() - 10))

        self._anim2 = QPropertyAnimation(widget, b"pos")
        self._anim2.setDuration(100)
        self._anim2.setStartValue(QPoint(widget.x(), widget.y() - 10))
        self._anim2.setEndValue(QPoint(widget.x(), widget.y()))

        self._anim_group = QSequentialAnimationGroup()
        self._anim_group.addAnimation(self._anim1)
        self._anim_group.addAnimation(self._anim2)

        self._anim_group.start()


class NavigationBarItem(QWidget):
    def __init__(self, text: str | None = None, pixmap: QPixmap | None = None) -> None:
        super().__init__()

        # assert icon is not None and text is not None, "Text, icon or both have to be supplied to the widget."

        # self.setFixedWidth(50)
        self._pixmap = pixmap
        self._stack = QStackedLayout(self)
        self._content_frame = QFrame()
        self._content_layout = QVBoxLayout()
        self._button = QPushButton()
        self._label = QLabel(text)
        self._icon = QLabel()

        self._init_widgets()
        self._add_to_layout()
        self._add_functionality()

    def _init_widgets(self) -> None:
        self._icon.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._button.setStyleSheet(
            """
            QPushButton {
                background-color: transparent;
                color: transparent;
                border: none;
            }
            
            QPushButton::hover {
                background-color: rgba(230, 230, 230, 70);
            }
            """
        )

    def _add_to_layout(self) -> None:
        if self._pixmap is not None:
            self._icon.setPixmap(self._pixmap)
            self._content_layout.addWidget(self._icon)

        if self._label is not None:
            self._content_layout.addWidget(self._label)

        self._content_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._content_frame.setLayout(self._content_layout)

        self._stack.setContentsMargins(0, 0, 0, 0)
        self._stack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self._stack.addWidget(self._button)
        self._stack.addWidget(self._content_frame)

        self.setLayout(self._stack)

    def _add_functionality(self) -> None:
        self._button.clicked.connect(lambda: self._add_animation())

    def _add_animation(self):
        self._label.setStyleSheet("color: blue;")

        self._anim1 = QPropertyAnimation(self, b"pos")
        self._anim1.setDuration(100)
        self._anim1.setEasingCurve(QEasingCurve.Type.BezierSpline)
        self._anim1.setStartValue(QPoint(self.x(), self.y()))
        self._anim1.setEndValue(QPoint(self.x(), self.y() - 10))

        self._anim2 = QPropertyAnimation(self, b"pos")
        self._anim2.setDuration(100)
        self._anim2.setStartValue(QPoint(self.x(), self.y() - 10))
        self._anim2.setEndValue(QPoint(self.x(), self.y()))

        self._anim_group = QSequentialAnimationGroup()
        self._anim_group.addAnimation(self._anim1)
        self._anim_group.addAnimation(self._anim2)

        self._anim_group.start()
