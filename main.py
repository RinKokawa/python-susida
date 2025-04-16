import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget, QMessageBox
from PyQt5.QtGui import QPainter, QColor, QMouseEvent, QFont
from PyQt5.QtCore import Qt, QPoint, QRect
from random_word import RandomWords

from word_manager import WordManager
from utils import get_contrasting_text_color
from config_loader import load_config
from theme_config import load_theme
from font_selector import FontSelector

class TypingWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(600, 600)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setWindowTitle("寿司打练习（配置版）")

        self._dragging = False
        self._drag_position = QPoint()
        self.font_selector = None

        self.white_rect = QRect(
            (self.width() - 200) // 2,
            (self.height() - 20) // 2,
            200,
            20
        )

        self.close_button_rect = QRect(
            self.white_rect.right() - 20,
            self.white_rect.top(),
            20,
            self.white_rect.height()
        )

        self.font_button_rect = QRect(
            self.white_rect.left(),
            self.white_rect.top(),
            60,
            self.white_rect.height()
        )

        self.centerOnScreen()

        config = load_config()
        self.theme = load_theme()

        if not config.get("baidu", {}).get("appid") or not config["baidu"].get("secret"):
            QMessageBox.warning(self, "配置提示", "未填写百度翻译配置，翻译功能将不可用。\n请前往 config.json 填写 appid 和 secret。")

        self.word_mgr = WordManager(RandomWords(), config)
        self.word_mgr.load_new_word()

    def centerOnScreen(self):
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move(
            (screen.width() - size.width()) // 2,
            (screen.height() - size.height()) // 2
        )

    def paintEvent(self, event):
        painter = QPainter(self)
        bg_color = QColor(255, 255, 255)
        painter.setBrush(bg_color)
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.white_rect)

        painter.setBrush(QColor(220, 50, 50))
        painter.drawRect(self.close_button_rect)
        painter.setPen(QColor(255, 255, 255))
        close_font = QFont("Arial", 10)
        painter.setFont(close_font)
        painter.drawText(self.close_button_rect, Qt.AlignCenter, "X")

        painter.setBrush(QColor(100, 100, 255))
        painter.setPen(Qt.NoPen)
        painter.drawRect(self.font_button_rect)
        painter.setPen(QColor(255, 255, 255))
        font_btn_font = QFont("Arial", 10)
        painter.setFont(font_btn_font)
        painter.drawText(self.font_button_rect, Qt.AlignCenter, "字体")

        word_font_conf = self.theme["word_font"]
        word_font = QFont(word_font_conf["family"], word_font_conf["size"])
        word_font.setBold(word_font_conf.get("bold", False))
        painter.setFont(word_font)

        word = self.word_mgr.get_current_word()
        statuses = self.word_mgr.get_status_list()
        x = self.white_rect.center().x() - len(word) * 8
        y = self.white_rect.top() - 10

        normal_color = get_contrasting_text_color(bg_color)

        for i, char in enumerate(word):
            status = statuses[i]
            if status == 'correct':
                painter.setPen(QColor(0, 180, 0))
            elif status == 'wrong' and i == self.word_mgr.current_index:
                painter.setPen(QColor(200, 0, 0))
            else:
                painter.setPen(normal_color)
            painter.drawText(x + i * 16, y, char)

        trans_font_conf = self.theme["translation_font"]
        trans_font = QFont(trans_font_conf["family"], trans_font_conf["size"])
        trans_font.setBold(trans_font_conf.get("bold", False))
        painter.setFont(trans_font)

        painter.setPen(QColor(50, 50, 50))
        painter.drawText(
            self.white_rect.left(),
            self.white_rect.bottom() + 20,
            self.word_mgr.get_translation()
        )

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.word_mgr.load_new_word()
            self.update()
            return

        key = event.text().lower()
        if not key:
            return

        success, finished = self.word_mgr.process_input(key)
        if finished:
            self.word_mgr.load_new_word()
        self.update()

    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            if self.close_button_rect.contains(event.pos()):
                self.close()
                return
            elif self.font_button_rect.contains(event.pos()):
                self.font_selector = FontSelector()
                self.font_selector.show()
                return
            elif self.white_rect.contains(event.pos()):
                self._dragging = True
                self._drag_position = event.globalPos() - self.frameGeometry().topLeft()
                event.accept()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self._dragging:
            self.move(event.globalPos() - self._drag_position)
            event.accept()

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self._dragging = False
            self.theme = load_theme()
            self.update()
            event.accept()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = TypingWindow()
    window.show()
    sys.exit(app.exec_())