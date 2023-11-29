from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QVBoxLayout, QPushButton, QHBoxLayout, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from adb import ADB
from worker import ADBWorker
from paddleocr import PaddleOCR
from image import ImageProcessor
from item import Item
from ui import SmithUI
from drag import DraggableWidget
import sys
import os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.adb = ADB()
        self.ocr = PaddleOCR()
        self.initUI()

    def __del__(self):
        # 删除 screenshot.png、adbkey 和 adbkey.pub 文件
        files_to_delete = ["screenshot.png", "adbkey", "adbkey.pub"]
        for file_name in files_to_delete:
            if os.path.exists(file_name):
                os.remove(file_name)

    def initUI(self):
        self.setFixedSize(400, 430)
        self.setWindowFlags(Qt.FramelessWindowHint)

        # 创建主窗口的容器和布局
        self.main_widget = QWidget(self)
        self.setStyleSheet("background-color: white;")
        main_layout = QVBoxLayout(self.main_widget)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # 创建标题栏容器和布局
        title_bar_widget = DraggableWidget(self)
        title_bar_widget.setStyleSheet("background-color: gray;")  # 设置背景色为灰色
        title_bar_layout = QHBoxLayout(title_bar_widget)
        title_bar_layout.setContentsMargins(0, 0, 0, 0)
        title_bar_layout.setSpacing(0)

        # 添加 titleLabel
        self.titleLabel = QLabel('铁柱工具箱')
        self.titleLabel.setFixedSize(370, 30)  # 设置按钮大小
        self.titleLabel.setStyleSheet("""
            QLabel {
                font-family: '微软雅黑'; 
                font-size: 15px; 
                color: white; 
                padding-left: 10px;
            }
        """)  # 设置字体、字号和颜色
        title_bar_layout.addWidget(self.titleLabel)

        # 添加一个弹性空间
        spacer = QSpacerItem(
            40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        title_bar_layout.addSpacerItem(spacer)

        # 创建并添加 closeButton
        self.closeButton = QPushButton("×")
        self.closeButton.setFixedSize(30, 30)  # 设置按钮大小
        self.closeButton.clicked.connect(self.close)

        # 设置扁平化按钮的样式
        self.closeButton.setStyleSheet("""
            QPushButton {
                background-color: red;
                color: white;
                border: none;
                font-size: 20px;
            }
            QPushButton:hover {
                background-color: darkred;
            }
            QPushButton:pressed {
                background-color: #D64541;
            }
        """)
        self.closeButton.setFlat(True)  # 设置按钮为扁平化
        title_bar_layout.addWidget(self.closeButton)

        # 将标题栏容器添加到主布局
        main_layout.addWidget(title_bar_widget)

        # 将 emulatorUI 添加到主布局
        self.emulatorUI = SmithUI(self.connectEmulator, self.takeScreenshot)
        main_layout.addWidget(self.emulatorUI)

        # 为主窗口设置布局
        self.main_widget.setLayout(main_layout)
        self.setCentralWidget(self.main_widget)

    def connectEmulator(self):
        port = self.emulatorUI.portInput.text()
        self.adbWorker = ADBWorker(self.adb, port)
        self.adbWorker.finished.connect(self.onConnectionFinished)
        self.adbWorker.start()

    def onConnectionFinished(self, success, message):
        if success:
            self.emulatorUI.resultLabel.setText(message)
            self.emulatorUI.resultLabel.setStyleSheet(
                "color: green; font-size: 16px;")  # 成功时设置为绿色
        else:
            self.emulatorUI.resultLabel.setText(f'连接失败')
            self.emulatorUI.resultLabel.setStyleSheet(
                "color: red; font-size: 16px;")  # 失败时设置为红色

    def takeScreenshot(self):
        # 一旦截图完成，使用PaddleOCR提取文本
        success, result = self.adb.take_screenshot()
        if success:
            # 识别文字
            processor = ImageProcessor(result)
            processor.preprocess_for_ocr(0.025, 0.11, 0.29, 0.67)
            processor.erase_area(0, 0, 0.19, 0.1)
            processor.erase_area(0, 0.1, 1, 0.47)
            processor.erase_area(0, 0.75, 1, 0.9)
            processor.erase_area(0, 0.9, 0.12, 1)
            processor.save(result)
            texts = self.ocr.ocr(result, cls=False)
            texts = [item[1][0] for item in texts[0]]
            if len(texts) == 11:
                first_element = texts.pop(0)
                level = int(first_element[1:])
            else:
                level = 0
            self.emulatorUI.levelLabel.setText(f'强化等级：{level}')
            first_element = texts.pop(0)
            part = first_element[2:]
            self.emulatorUI.partLabel.setText(f'部位：{part}')
            last_element = texts.pop()
            suit = ''.join(
                [char for char in last_element if not char.isdigit() and char not in '（）()/'])
            self.emulatorUI.suitLabel.setText(f'套装：{suit}')
            grouped_list = []
            for i in range(0, len(texts), 2):
                group = texts[i:i+2]
                grouped_list.append(group)
            score = Item.calculate_score(grouped_list)
            formatted_score = f'分数：{score:.2f}'
            self.emulatorUI.scoreLabel.setText(formatted_score)
            for i in range(4):
                label = getattr(self.emulatorUI, f'attribute{i + 1}Label')
                label.setText(f'{grouped_list[i][0]}: {grouped_list[i][1]}')

        else:
            self.emulatorUI.resultLabel.setText(f'截图失败: {result}')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    ex.show()
    sys.exit(app.exec_())
