import json
import datetime
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from telegram import Update
from scheduler import start_scheduler

bot_token = "8034335353:AAEOoEY-G3di-swr-UqX9BREv_cKoyVNKm0" 
key ="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"   


def save_message(user_id, username, text):
    filename = "messages.json"

    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append({
        "user_id": user_id,
        "user_name": username or "no-username",
        "text": text,
        "time": datetime.datetime.now().isoformat()
    })

    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Привет, я бот :)")

async def handle_message(update: Update, context: ContextTypes):
    user = update.message.from_user
    msg = update.message.text

    save_message(user.id, user.username, msg)
    await update.message.reply_text(f"Вы писали: {msg}")

if __name__ == "__main__":
    start_scheduler()
    app = ApplicationBuilder().token(bot_token).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Бот готов и работает...")
    app.run_polling()
