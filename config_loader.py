import json
import os

default_config = {
    "baidu": {
        "appid": "",
        "secret": ""
    }
}

def load_config(path='config.json'):
    if not os.path.exists(path):
        print("[INFO] config.json 不存在，正在创建默认模板...")
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(default_config, f, indent=4, ensure_ascii=False)
        return default_config

    with open(path, 'r', encoding='utf-8') as f:
        config = json.load(f)

    return config
