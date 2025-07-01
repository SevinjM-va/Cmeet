import json
import datetime
from telegram import Bot
from summarizer import summarize_messages
from apscheduler.schedulers.background import BackgroundScheduler



channel_id = "-2736686379"
bot_token = "8034335353:AAEOoEY-G3di-swr-UqX9BREv_cKoyVNKm0"
openrouter_api_key = "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"
messages_file = "messages.json"


def collect_messages():
    try:
        with open(messages_file, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    today = datetime.date.today().isoformat()
    return [item["text"] for item in data if item.get("time","").startswith(today)]


def send_sum():
    bot = Bot(token=bot_token)
    messages = collect_messages()

    if not messages:
        print("Сегодня сообщений нет.")
        return

    summary = summarize_messages(messages, openrouter_api_key)
    print("DeepSeek ответ:", summary) 
    bot.send_message(chat_id=channel_id, text=summary)
    print("Сегодняшние сообщения были отправлены в канал Telegram.")


def start_scheduler():
    scheduler = BackgroundScheduler(timezone="Asia/Baku")
    scheduler.add_job(send_sum, "cron", hour=21, minute=0)  
    scheduler.start()
    print("Scheduler işə düşdü.")


if __name__ == "__main__":
    send_sum()