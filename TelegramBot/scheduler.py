import json
import datetime
from telegram import Bot
from summarizer import summarize_messages
from apscheduler.schedulers.background import BackgroundScheduler


bot_token = "7669197497:AAHiQL6KJbD2Y093YN2GqrLKJV1p3j5qWi4"
channel_id = "-2736686379"
messages_file = "messages.json"

openrouter_api_key  = "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"

def collect_messages():
    try:
        with open("messages.json", "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        return []

    today = datetime.date.today().isoformat()
    messages_today = []

    for item in data:
        if item["time"].startswith(today):
            messages_today.append(item["text"])

    return messages_today

def send_sum():
    bot = Bot(token=bot_token)
    messages = collect_messages()
    summary = summarize_messages(messages, openrouter_api_key)
    bot.send_message(chat_id=channel_id, text=summary)

def start_scheduler():
    scheduler = BackgroundScheduler(timezone="Asia/Baku")
    scheduler.add_job(send_sum, "cron", hour=19, minute=40)
    scheduler.start()
