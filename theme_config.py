# theme_config.py

DEFAULT_THEME = {
    "word_font": {
        "family": "Consolas",
        "size": 20,
        "bold": True
    },
    "translation_font": {
        "family": "Segoe UI",
        "size": 12,
        "bold": False
    }
}

def load_theme():
    return DEFAULT_THEME
