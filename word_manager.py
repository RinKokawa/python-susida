import random
from utils import baidu_translate

class WordManager:
    def __init__(self, generator, config):
        self.generator = generator
        self.config = config
        self.word = ''
        self.current_index = 0
        self.status_list = []
        self.translation = ""

    def load_new_word(self):
        while True:
            word = self.generator.get_random_word()
            if word and word.isalpha() and 3 <= len(word) <= 8:
                self.word = word.lower()
                break

        print("[DEBUG] 当前单词：", self.word)

        if self.word and 'baidu' in self.config:
            baidu_conf = self.config['baidu']
            appid = baidu_conf.get('appid')
            secret = baidu_conf.get('secret')
            self.translation = baidu_translate(self.word, appid, secret)
        else:
            self.translation = "(无效词)"

        self.current_index = 0
        self.status_list = ['default'] * len(self.word)

    def process_input(self, key: str):
        if self.current_index >= len(self.word):
            return False, False

        expected = self.word[self.current_index]
        if key == expected:
            self.status_list[self.current_index] = 'correct'
            self.current_index += 1
            return True, self.current_index >= len(self.word)
        else:
            self.status_list[self.current_index] = 'wrong'
            return False, False

    def get_current_word(self):
        return self.word

    def get_status_list(self):
        return self.status_list

    def get_translation(self):
        return self.translation