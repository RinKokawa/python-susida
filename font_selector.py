# font_selector.py
import os
import json
from PyQt5.QtWidgets import (
    QWidget, QListWidget, QLabel, QPushButton,
    QVBoxLayout, QMessageBox
)
from PyQt5.QtGui import QFontDatabase, QFont
from PyQt5.QtCore import Qt

FONTS_DIR = "fonts"
THEME_FILE = "theme_config.py"

class FontSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("选择字体")
        self.setFixedSize(400, 500)
        self.setWindowFlags(Qt.WindowStaysOnTopHint)

        self.font_list = QListWidget()
        self.preview = QLabel("The quick brown fox jumps over the lazy dog.")
        self.preview.setAlignment(Qt.AlignCenter)
        self.preview.setWordWrap(True)

        self.confirm_btn = QPushButton("使用选中字体")
        self.reset_btn = QPushButton("恢复默认字体")
        self.confirm_btn.clicked.connect(self.confirm_selection)
        self.reset_btn.clicked.connect(self.reset_default)

        layout = QVBoxLayout()
        layout.addWidget(self.font_list)
        layout.addWidget(self.preview)
        layout.addWidget(self.confirm_btn)
        layout.addWidget(self.reset_btn)
        self.setLayout(layout)

        self.font_map = {}  # 显示名 → 字体名
        self.load_fonts()
        self.font_list.currentTextChanged.connect(self.update_preview)

    def load_fonts(self):
        if not os.path.exists(FONTS_DIR):
            os.makedirs(FONTS_DIR)

        for filename in os.listdir(FONTS_DIR):
            if filename.endswith(".ttf"):
                path = os.path.join(FONTS_DIR, filename)
                font_id = QFontDatabase.addApplicationFont(path)
                families = QFontDatabase.applicationFontFamilies(font_id)
                if families:
                    display_name = f"{families[0]}  ({filename})"
                    self.font_map[display_name] = families[0]
                    self.font_list.addItem(display_name)

    def update_preview(self, display_name):
        family = self.font_map.get(display_name)
        if family:
            font = QFont(family, 16)
            self.preview.setFont(font)

    def confirm_selection(self):
        current = self.font_list.currentItem()
        if current:
            family = self.font_map.get(current.text())
            self.write_theme(family)
            QMessageBox.information(self, "字体已应用", f"已选择字体：{family}\n请关闭窗口查看效果。")
            self.close()
        else:
            QMessageBox.warning(self, "未选择", "请先选中一个字体！")

    def reset_default(self):
        self.write_theme("Consolas")
        QMessageBox.information(self, "字体已重置", "已恢复默认字体 Consolas。")
        self.close()

    def write_theme(self, font_family):
        theme_content = f"""# theme_config.py
def load_theme():
    return {{
        "word_font": {{
            "family": "{font_family}",
            "size": 22,
            "bold": True
        }},
        "translation_font": {{
            "family": "Segoe UI",
            "size": 13,
            "bold": False
        }}
    }}
"""
        with open(THEME_FILE, "w", encoding="utf-8") as f:
            f.write(theme_content)