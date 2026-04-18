import smtplib
from email.mime.text import MIMEText
from datetime import datetime
import os

# -------------------------- 你的配置 --------------------------
QQ_EMAIL = os.environ.get("QQ_EMAIL")
QQ_AUTH = os.environ.get("QQ_AUTH")
CITY = "广州"
# -------------------------------------------------------------

def get_ai_report():
    today = datetime.now().strftime("%Y-%m-%d")
    report = f"""
📅 {today} 每日综合日报
━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🌤️ 今日天气（{CITY}）
- 晴朗 / 多云 / 阴天 实时天气

📈 A股市场
- 大盘走势简要参考
- 今日热点板块

🔐 网络安全动态
- 行业重要新闻

🏭 智能制造 / 机械 / 材料
- 前沿技术动态

💻 GitHub 热门项目
- 今日趋势项目

🔬 科技 & 数码电子
- 最新资讯

🌍 政治局势简要
- 国内外重要事件

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
AI 自动日报 · 每日 09:30 准时推送
"""
    return report

def send_email(report):
    msg = MIMEText(report, "plain", "utf-8")
    msg["Subject"] = f"📅 {today} 每日AI日报"
    msg["From"] = QQ_EMAIL
    msg["To"] = QQ_EMAIL

    with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
        server.login(QQ_EMAIL, QQ_AUTH)
        server.sendmail(QQ_EMAIL, [QQ_EMAIL], msg.as_string())

if __name__ == "__main__":
    report = get_ai_report()
    send_email(report)
    print("✅ 发送成功")
