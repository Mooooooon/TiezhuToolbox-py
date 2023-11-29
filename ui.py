from PyQt5.QtWidgets import QWidget, QGridLayout, QLineEdit, QPushButton, QLabel, QSizePolicy
from PyQt5.QtCore import Qt


class SmithUI(QWidget):
    def __init__(self, connect_emulator_callback, take_screenshot_callback):
        super().__init__()
        self.connect_emulator_callback = connect_emulator_callback
        self.take_screenshot_callback = take_screenshot_callback
        self.initUI()

    def initUI(self):
        self.layout = QGridLayout()
        self.layout.setSpacing(5)  # 设置控件间的间距
        self.setFixedSize(400, 400)

        self.portInput = QLineEdit(self)
        self.portInput.setText("7555")
        self.portInput.setFixedSize(100, 24)

        self.connectButton = QPushButton('连接模拟器', self)
        self.connectButton.setFixedSize(100, 24)
        self.connectButton.setStyleSheet(
            "border: 1px solid #888888;"  # 设置1px灰色边框
            "background-color: transparent;"  # 设置背景色为透明
            "color: #000000;"  # 设置文本颜色，可以根据需要修改颜色值
        )

        self.screenshotButton = QPushButton('截取屏幕', self)
        self.screenshotButton.setFixedSize(100, 24)
        self.screenshotButton.setStyleSheet(
            "border: 1px solid #888888;"  # 设置1px灰色边框
            "background-color: transparent;"  # 设置背景色为透明
            "color: #00000;"  # 设置文本颜色，可以根据需要修改颜色值
        )

        self.resultLabel = QLabel('尚未链接', self)
        self.resultLabel.setFixedSize(100, 24)
        self.resultLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)  # 设置文字居中对齐
        self.resultLabel.setStyleSheet("font-size: 16px;")  # 设置字号为18
        font_style = "font-size: 14px; font-family: '微软雅黑';"

        self.levelLabel = QLabel('', self)
        self.levelLabel.setStyleSheet(font_style)
        self.levelLabel.setFixedSize(200, 16)

        self.partLabel = QLabel('', self)
        self.partLabel.setStyleSheet(font_style)
        self.partLabel.setFixedSize(200, 16)

        self.attribute1Label = QLabel('', self)
        self.attribute1Label.setStyleSheet(font_style)
        self.attribute1Label.setFixedSize(200, 16)

        self.attribute2Label = QLabel('', self)
        self.attribute2Label.setStyleSheet(font_style)
        self.attribute2Label.setFixedSize(200, 16)

        self.attribute3Label = QLabel('', self)
        self.attribute3Label.setStyleSheet(font_style)
        self.attribute3Label.setFixedSize(200, 16)

        self.attribute4Label = QLabel('', self)
        self.attribute4Label.setStyleSheet(font_style)
        self.attribute4Label.setFixedSize(200, 16)

        self.scoreLabel = QLabel('', self)
        self.scoreLabel.setStyleSheet(font_style)
        self.scoreLabel.setFixedSize(200, 16)

        self.suitLabel = QLabel('', self)
        self.suitLabel.setStyleSheet(font_style)
        self.suitLabel.setFixedSize(200, 16)

        self.itemInfoText = QLineEdit(self)
        self.itemInfoText.setPlaceholderText("")
        # 设置文本框为只读
        self.itemInfoText.setReadOnly(True)
        # 设置尺寸策略以允许文本框垂直扩展
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        self.itemInfoText.setSizePolicy(sizePolicy)
        # 这将使文本框从第一行开始，跨越12行（假设你有12个元素在左侧）
        self.layout.addWidget(self.itemInfoText, 0, 1, 12, 1)

        # 添加控件到布局
        self.layout.addWidget(self.portInput, 0, 0, Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.connectButton, 1, 0,
                              Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.screenshotButton, 2,
                              0, Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.resultLabel, 3, 0,
                              Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.levelLabel, 4, 0,
                              Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.partLabel, 5, 0, Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.attribute1Label, 6, 0,
                              Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.attribute2Label, 7, 0,
                              Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.attribute3Label, 8, 0,
                              Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.attribute4Label, 9, 0,
                              Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.scoreLabel, 10, 0,
                              Qt.AlignLeft | Qt.AlignTop)
        self.layout.addWidget(self.suitLabel, 11, 0,
                              Qt.AlignLeft | Qt.AlignTop)

        self.setLayout(self.layout)

        self.connectButton.clicked.connect(self.connect_emulator_callback)
        self.screenshotButton.clicked.connect(self.take_screenshot_callback)
