from __future__ import annotations

from PyQt6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QSequentialAnimationGroup, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import (
    QAbstractButton, QFrame, QHBoxLayout, QLabel, QPushButton, QStackedLayout, QVBoxLayout, QWidget
)


class NavigationBar(QWidget):
    def __init__(self, parent: QWidget, height: int) -> None:
        """

        :param parent:
        :param height:
        """

        super().__init__(parent)

        assert height >= 50, "NavigationBar height cannot be lesser than 50."

        self._height = height
        self._items = []
        self._layout = QHBoxLayout(self)

        self._initWidgets()
        self._addToLayout()

    @property
    def getItems(self) -> list[NavigationBarItem]:
        """

        :return:
        """

        return self._items

    def addItem(self, item: NavigationBarItem) -> None:
        """

        :param item:
        """

        self._items.append(item)
        self._layout.addWidget(item)

    def _initWidgets(self) -> None:
        self.setFixedHeight(self._height)

    def _addToLayout(self) -> None:
        self._layout.setContentsMargins(0, 0, 0, 0)
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

        self._animGroup = QSequentialAnimationGroup()
        self._animGroup.addAnimation(self._anim1)
        self._animGroup.addAnimation(self._anim2)

        self._animGroup.start()


class NavigationBarItem(QWidget):
    def __init__(self, text: str | None = None, pixmap: QPixmap | None = None) -> None:
        """

        :param text:
        :param pixmap:
        """

        super().__init__()

        # assert icon is not None and text is not None, "Text, icon or both have to be supplied to the widget."

        self._text = text
        self._pixmap = pixmap
        self._stack = QStackedLayout(self)
        self._contentFrame = QFrame()
        self._contentLayout = QVBoxLayout()
        self._button = QPushButton()
        self._label = QLabel(text)
        self._icon = QLabel()

        self._initWidgets()
        self._addToLayout()
        self._addFunctionality()

    @property
    def getButton(self) -> QPushButton:
        """

        :return:
        """

        return self._button

    def _initWidgets(self) -> None:
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

    def _addToLayout(self) -> None:
        if self._pixmap is not None:
            self._icon.setPixmap(self._pixmap)
            self._contentLayout.addWidget(self._icon)
        else:
            self._icon.destroy()

        if self._text is not None:
            self._contentLayout.addWidget(self._label)
        else:
            self._label.destroy()

        self._contentLayout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self._contentFrame.setLayout(self._contentLayout)

        self._stack.setContentsMargins(0, 0, 0, 0)
        self._stack.setStackingMode(QStackedLayout.StackingMode.StackAll)
        self._stack.addWidget(self._button)
        self._stack.addWidget(self._contentFrame)

        self.setLayout(self._stack)

    def _addFunctionality(self) -> None:
        self._button.clicked.connect(lambda: self._animate())

    def _animate(self) -> None:
        self._anim1 = QPropertyAnimation(self, b"pos")
        self._anim1.setDuration(100)
        self._anim1.setEasingCurve(QEasingCurve.Type.BezierSpline)
        self._anim1.setStartValue(QPoint(self.x(), self.y()))
        self._anim1.setEndValue(QPoint(self.x(), self.y() - 5))

        self._anim2 = QPropertyAnimation(self, b"pos")
        self._anim2.setDuration(100)
        self._anim2.setStartValue(QPoint(self.x(), self.y() - 5))
        self._anim2.setEndValue(QPoint(self.x(), self.y()))

        self._animGroup = QSequentialAnimationGroup()
        self._animGroup.addAnimation(self._anim1)
        self._animGroup.addAnimation(self._anim2)

        self._animGroup.start()
