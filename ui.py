from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QSizePolicy
from PyQt5.QtCore import Qt

class SmithUI(QWidget):
    def __init__(self, connect_emulator_callback, take_screenshot_callback):
        super().__init__()
        self.connect_emulator_callback = connect_emulator_callback
        self.take_screenshot_callback = take_screenshot_callback
        self.initUI()

    def initUI(self):
        self.layout = QVBoxLayout()
        self.layout.setSpacing(5)  # 设置控件间的间距
        self.layout.setAlignment(Qt.AlignTop)
        self.setFixedSize(400, 400)

        self.portInput = QLineEdit(self)
        self.portInput.setText("7555")
        self.portInput.setFixedWidth(100)  # 设置固定宽度
        

        self.connectButton = QPushButton('连接模拟器', self)
        self.connectButton.setFixedWidth(100)  # 设置固定宽度

        self.screenshotButton = QPushButton('截取屏幕', self)
        self.screenshotButton.setFixedWidth(100)  # 设置固定宽度

        self.resultLabel = QLabel('', self)
        self.levelLabel = QLabel('', self)
        self.partLabel = QLabel('', self)
        self.attribute1Label = QLabel('', self)
        self.attribute2Label = QLabel('', self)
        self.attribute3Label = QLabel('', self)
        self.attribute4Label = QLabel('', self)
        self.scoreLabel = QLabel('', self)
        self.suitLabel = QLabel('', self)

        # 添加控件到布局
        self.layout.addWidget(self.portInput)
        self.layout.addWidget(self.connectButton)
        self.layout.addWidget(self.screenshotButton)
        self.layout.addWidget(self.resultLabel)
        self.layout.addWidget(self.levelLabel)
        self.layout.addWidget(self.partLabel)
        self.layout.addWidget(self.attribute1Label)
        self.layout.addWidget(self.attribute2Label)
        self.layout.addWidget(self.attribute3Label)
        self.layout.addWidget(self.attribute4Label)
        self.layout.addWidget(self.scoreLabel)
        self.layout.addWidget(self.suitLabel)

        self.setLayout(self.layout)

        self.connectButton.clicked.connect(self.connect_emulator_callback)
        self.screenshotButton.clicked.connect(self.take_screenshot_callback)
