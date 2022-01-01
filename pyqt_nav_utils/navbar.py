from __future__ import annotations

from PyQt6.QtCore import QEasingCurve, QPoint, QPropertyAnimation, QSequentialAnimationGroup
from PyQt6.QtWidgets import QAbstractButton, QHBoxLayout, QSizePolicy, QWidget


class NavigationBar(QWidget):
    """An animated NavigationBar widget"""

    def __init__(self, parent: QWidget, height: int, *args: QAbstractButton) -> None:
        super().__init__(parent)

        assert height >= 50, "NavigationBar height cannot be lesser than 50."

        self._height = height
        self._args = args
        self._layout = QHBoxLayout(self)
        self._state = dict(enumerate(args))

        self._init_widgets()
        self._add_to_layout()
        self._add_functionality()

    def _init_widgets(self) -> None:
        self.setFixedHeight(self._height)
        self.setSizePolicy(
            QSizePolicy(
                QSizePolicy.Policy.Preferred,
                QSizePolicy.Policy.Fixed,
            )
        )

    def _add_to_layout(self) -> None:
        for i in self._args:
            self._layout.addWidget(i)

        self.setLayout(self._layout)

    def _add_functionality(self) -> None:
        for i in self._args:
            i.clicked.connect(lambda: self._animate(i))

    def _animate(self, widget: QAbstractButton) -> None:
        widget.setDisabled(True)

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

        widget.setDisabled(False)
