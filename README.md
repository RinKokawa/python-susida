# 寿司打（PyQt5 打字练习工具）

这是一个使用 PyQt5 构建的简洁打字练习应用，灵感来源于「寿司打」。支持英文单词输入、即时反馈、自动翻译等功能，适合练习打字和英语词汇记忆。

[GitHub](https://github.com/RinKokawa/python-susida) [Gitee](https://gitee.com/rinkokawa/python-susida)

---

## 🧩 功能特点

- ✅ 单词打字练习，支持即时判断对错
- ✅ 正确绿色，错误红色，自动切换下一个词
- ✅ 单词下方显示百度翻译（可选）
- ✅ 窗口置顶、全透明背景、可拖动界面
- ✅ 自带关闭按钮（右上角 X）
- ✅ 配置文件自动初始化，支持自定义翻译密钥

---

## 🛠️ 安装依赖

请先确保你已经安装 Python（建议 3.8+），然后执行以下命令：

```bash
pip install -r requirements.txt
```

### requirements.txt 内容：
```txt
PyQt5
random-word
requests
```

---

## 🚀 启动程序

```bash
python main.py
```

首次运行会自动创建 `config.json`，请在其中填写百度翻译 API 的 `appid` 和 `secret`：

```json
{
  "baidu": {
    "appid": "你的appid",
    "secret": "你的密钥"
  }
}
```

若未填写，程序仍可使用，但不显示翻译。

---

## 📁 项目结构

```
.
├── main.py              # 主程序入口（UI）
├── word_manager.py      # 单词生成与判断逻辑
├── config_loader.py     # 配置加载和初始化
├── utils.py             # 工具函数：对比色、翻译请求
├── config.json          # 外部配置文件（自动生成）
└── README.md
```

---

## 📌 待办 & 扩展建议

- [ ] 打字计分系统
- [ ] 自定义词库加载
- [ ] 界面主题切换
- [ ] 托盘驻留 + 最小化

---

## 📄 许可证

MIT License

---

欢迎提 Issue 或 Fork 自定义版本！打字愉快 🥷🎯
