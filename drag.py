from PyQt5.QtCore import QPoint, Qt
from PyQt5.QtWidgets import QWidget


class DraggableWidget(QWidget):
    def __init__(self, parent=None):
        super(DraggableWidget, self).__init__(parent)
        self.dragPosition = QPoint()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.dragPosition = event.globalPos() - self.window().frameGeometry().topLeft()
            event.accept()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            self.window().move(event.globalPos() - self.dragPosition)
            event.accept()
