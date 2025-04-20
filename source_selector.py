# source_selector.py
import os
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QListWidget, QPushButton, QMessageBox
from PyQt5.QtCore import Qt, pyqtSignal

VOCAB_DIR = os.path.join("vocabulary", "En")

class SourceSelector(QWidget):
    sourceSelected = pyqtSignal(str)

    def __init__(self, callback):
        super().__init__()
        self.setWindowTitle("选择单词来源")
        self.setFixedSize(300, 400)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.callback = callback
        self.list_widget = QListWidget()

        # 添加随机词源
        self.list_widget.addItem("随机单词 (random-word)")

        # 添加自定义词库
        if not os.path.exists(VOCAB_DIR):
            os.makedirs(VOCAB_DIR)

        self.available_files = []  # 保存完整路径
        for filename in os.listdir(VOCAB_DIR):
            if filename.endswith(".json"):
                filepath = os.path.join(VOCAB_DIR, filename)
                self.available_files.append(filepath)
                self.list_widget.addItem(f"词库: {filename}")

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
            idx = self.list_widget.currentRow() - 1  # -1 因为第一项是随机词源
            filepath = self.available_files[idx]
            self.callback(filepath)
        self.close()
