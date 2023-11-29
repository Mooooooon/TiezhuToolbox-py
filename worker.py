from PyQt5.QtCore import QThread, pyqtSignal


class ADBWorker(QThread):
    finished = pyqtSignal(bool, str)  # 发出连接结果的信号

    def __init__(self, adb, port):
        super().__init__()
        self.adb = adb
        self.port = port

    def run(self):
        success, message = self.adb.connect(self.port)
        self.finished.emit(success, message)
