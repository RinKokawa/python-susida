# utils.py
from PyQt5.QtGui import QColor
import requests
import hashlib
import random
import traceback

def get_contrasting_text_color(bg_color: QColor) -> QColor:
    """
    根据背景色计算合适的前景色（黑或白），以获得良好的可读性。
    """
    r, g, b = bg_color.red(), bg_color.green(), bg_color.blue()
    luminance = 0.299 * r + 0.587 * g + 0.114 * b
    return QColor(0, 0, 0) if luminance > 186 else QColor(255, 255, 255)

def baidu_translate(query, appid, secret_key, from_lang='en', to_lang='zh'):
    """
    使用百度翻译 API 获取翻译结果
    """
    if not query:
        print("[DEBUG] 翻译请求被跳过：空字符串")
        return "(翻译失败: 空字符串)"

    url = 'https://fanyi-api.baidu.com/api/trans/vip/translate'
    salt = str(random.randint(32768, 65536))
    sign = hashlib.md5((appid + query + salt + secret_key).encode('utf-8')).hexdigest()

    params = {
        'q': query,
        'from': from_lang,
        'to': to_lang,
        'appid': appid,
        'salt': salt,
        'sign': sign
    }

    print("[DEBUG] 翻译请求参数:", params)  # 调试日志

    try:
        response = requests.get(url, params=params, timeout=5)
        print("[DEBUG] 百度返回状态码:", response.status_code)
        result = response.json()
        print("[DEBUG] 百度返回内容:", result)

        if 'trans_result' in result:
            return result['trans_result'][0]['dst']
        elif 'error_msg' in result:
            return f"(翻译失败: {result['error_msg']})"
        else:
            return "(翻译失败: 未知返回)"
    except Exception as e:
        traceback.print_exc()
        return f"(错误: {e})"
