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
- 这里会显示实时天气与温度

📈 A股市场
- 大盘方向与热点板块简要

🔐 网络安全动态
- 行业重要事件与漏洞播报

🏭 智能制造/机械/材料
- 前沿技术与行业动态

💻 GitHub热门项目
- 今日趋势开源项目推荐

🔬 科技/数码电子
- 前沿资讯与新品动态

🌍 政治局势简要
- 国内外重要事件梳理

━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 今日小结：保持专注，高效前行！
    """
    return report, today

def send_email(report, today):
    msg = MIMEText(report, "plain", "utf-8")
    msg["Subject"] = f"📅 {today} 每日AI综合日报"
    msg["From"] = QQ_EMAIL
    msg["To"] = QQ_EMAIL

    with smtplib.SMTP_SSL("smtp.qq.com", 465) as server:
        server.login(QQ_EMAIL, QQ_AUTH)
        server.sendmail(QQ_EMAIL, [QQ_EMAIL], msg.as_string())

if __name__ == "__main__":
    report, today = get_ai_report()
    send_email(report, today)
    print("✅ 日报已发送成功！")
