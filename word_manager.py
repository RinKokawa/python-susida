# word_manager.py
from PyQt5.QtCore import QTimer

class WordManager:
    def __init__(self, source, config=None):
        self.generator = source
        self.config = config or {}
        self.word = ""
        self.current_index = 0
        self.status_list = []
        self.translation = ""

    def load_new_word(self):
        while True:
            word = self.generator.get_random_word()
            if word and word.isalpha() and 3 <= len(word) <= 15:
                self.word = word.lower()
                break

        self.current_index = 0
        self.status_list = ['default'] * len(self.word)

        if hasattr(self.generator, 'get_translation'):
            self.translation = self.generator.get_translation(self.word)
        else:
            self.translation = "(暂无翻译)"

    def get_current_word(self):
        return self.word

    def get_status_list(self):
        return self.status_list

    def get_translation(self):
        return self.translation

    def process_input(self, char):
        if self.current_index >= len(self.word):
            return False, False

        expected = self.word[self.current_index]
        if char == expected:
            self.status_list[self.current_index] = 'correct'
            self.current_index += 1
            if self.current_index >= len(self.word):
                return True, True  # 正确并完成
            return True, False     # 正确但未完成
        else:
            self.status_list[self.current_index] = 'wrong'
            return False, False