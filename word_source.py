# word_source.py
import json
import random

class JsonWordSource:
    def __init__(self, path="data/wordlist.json"):
        with open(path, "r", encoding="utf-8") as f:
            self.words = json.load(f)

    def get_random_word(self):
        if not self.words:
            return None
        return random.choice(self.words)["word"]

    def get_translation(self, word):
        for entry in self.words:
            if entry["word"] == word:
                translations = entry.get("translations", [])
                phrases = entry.get("phrases", [])

                parts = [
                    f"({item.get('type', '')}) {item['translation']}"
                    for item in translations
                ]
                phrase_parts = [
                    f"• {p['phrase']}：{p['translation']}"
                    for p in phrases[:3]  # 最多显示 3 个短语
                ]

                return "\n".join(parts + phrase_parts)
        return "(无翻译信息)"
