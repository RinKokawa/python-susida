# source_selector.py
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal

class SourceSelector(QWidget):
    sourceSelected = pyqtSignal(str)  # 添加信号支持

    def __init__(self, callback):
        super().__init__()
        self.setWindowTitle("选择单词来源")
        self.setFixedSize(300, 200)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.callback = callback

        self.list_widget = QListWidget()
        self.list_widget.addItem("随机单词 (random-word)")
        self.list_widget.addItem("词库单词 (wordlist.json)")
        self.list_widget.setCurrentRow(0)

        self.confirm_btn = QPushButton("确认使用该来源")
        self.confirm_btn.clicked.connect(self.select_source)

        layout = QVBoxLayout()
        layout.addWidget(self.list_widget)
        layout.addWidget(self.confirm_btn)
        self.setLayout(layout)

    def select_source(self):
        current = self.list_widget.currentItem()
        if not current:
            QMessageBox.warning(self, "提示", "请选择一种词源！")
            return

        text = current.text()
        if "随机" in text:
            self.callback("random")
        else:
            self.callback("json")
        self.close()