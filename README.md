
# 🥢 寿司打 - PyQt5 打字练习工具

一个灵感来自「寿司打」的简洁打字练习软件，使用 PyQt5 构建，支持多词库切换、自定义字体、每日打字数据自动记录，是练习英文打字和词汇记忆的理想工具。

---

## ✨ 功能特点

- ✅ 支持打字实时反馈：正确字母绿色，高亮错误位置
- ✅ 词源切换支持：
  - 随机英文单词（random-word）
  - 自定义 JSON 词库（读取自 `/vocabulary/En` 目录下的多个文件）
- ✅ 单词下方显示中文翻译（如已配置百度翻译 API）
- ✅ 自定义字体（从系统或项目 fonts 文件夹中选择）
- ✅ 每日打字日志自动生成（WPM / 准确率 / 错误统计）
- ✅ 窗口置顶、全透明、可拖动界面
- ✅ 内置关闭按钮

---

## 📁 项目结构

```
python-susida/
├── main.py                  # 主程序入口
├── log_writer.py            # 打字日志记录模块
├── word_manager.py          # 单词处理逻辑
├── word_source.py           # JSON 词库加载器
├── source_selector.py       # 词源切换弹窗
├── font_selector.py         # 字体选择弹窗
├── config_loader.py         # 百度翻译配置加载
├── theme_config.py          # 字体样式配置
├── utils.py                 # 工具函数（对比色 / 翻译）
├── vocabulary/
│   └── En/                  # 词库文件夹（.json）
│       ├── basic.json
│       └── cet4.json
├── data/                    # 每日打字记录输出目录
└── config.json              # 百度翻译 API 配置
```

---

## 🧩 使用说明

### 🔧 安装依赖

确保你已经安装 Python 3.8+：

```bash
pip install -r requirements.txt
```

内容包括：

```text
PyQt5
random-word
requests
```

---

### 🚀 启动程序

```bash
python main.py
```

首次运行将自动创建：

- `config.json`（如需翻译，请填写百度翻译 AppID 和 Secret）
- `data/YYYY-MM-DD.json`（自动记录打字日志）

---

## 🗂️ JSON 词库格式说明

放置路径：`vocabulary/En/*.json`

结构如下：

```json
[
  {
    "word": "ability",
    "translations": [
      { "type": "n", "translation": "能力，能耐；才能" }
    ],
    "phrases": [
      { "phrase": "innovation ability", "translation": "创新能力" }
    ]
  },
  ...
]
```

---

## 📝 打字记录格式示例

每天会自动生成一个 `data/YYYY-MM-DD.json` 文件，结构如下：

```json
{
  "timestamp": 1713651835.456,
  "word": "example",
  "typed": "exapmle",
  "start_time": 1713651830.123,
  "end_time": 1713651835.456,
  "duration": 5.33,
  "wpm": 45.0,
  "accuracy": 85.71,
  "mistakes": [
    { "index": 3, "expected": "m", "typed": "p" },
    { "index": 4, "expected": "p", "typed": "m" }
  ]
}
```

---

## 📌 后续计划（TODO）

- [ ] 导出 CSV 统计与图表分析
- [ ] 自定义主题配色支持
- [ ] 打字排行榜模式
- [ ] 托盘驻留 + 最小化

---

## 🙏 特别感谢

- 📘 本项目使用的英文词库结构与示例数据部分参考自 [@KyleBing/english-vocabulary](https://github.com/KyleBing/english-vocabulary) 项目，  
  感谢其无私分享高质量的英文单词文档与通用数据结构。

---

## 📄 License

MIT License

---

Made with ❤️ by [@RinKokawa](https://github.com/RinKokawa)
也欢迎访问[我的主页](www.rinkokawa.com)

打字愉快 🥷💥
