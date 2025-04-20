import os
import json
from datetime import datetime

class LogWriter:
    def __init__(self, folder="data"):
        os.makedirs(folder, exist_ok=True)
        today = datetime.now().strftime("%Y-%m-%d")
        self.filepath = os.path.join(folder, f"{today}.json")
        self.data = []

    def log_word(self, word, start_time, end_time, typed_chars):
        duration = end_time - start_time
        seconds = duration.total_seconds()
        wpm = (len(word) / 5) / (seconds / 60) if seconds > 0 else 0

        correct_count = 0
        mistakes = []
        for i, c in enumerate(typed_chars):
            if i < len(word):
                if c == word[i]:
                    correct_count += 1
                else:
                    mistakes.append({
                        "index": i,
                        "expected": word[i],
                        "typed": c
                    })
            else:
                mistakes.append({
                    "index": i,
                    "expected": "",
                    "typed": c
                })

        accuracy = (correct_count / max(len(typed_chars), 1)) * 100

        entry = {
            "timestamp": round(end_time.timestamp(), 3),
            "word": word,
            "typed": typed_chars,
            "start_time": round(start_time.timestamp(), 3),
            "end_time": round(end_time.timestamp(), 3),
            "duration": round(seconds, 2),
            "wpm": round(wpm, 2),
            "accuracy": round(accuracy, 2),
            "mistakes": mistakes
        }

        self.data.append(entry)

        # 即时保存到本地
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def save(self):
        # 可选：退出前统一调用一次也行
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
