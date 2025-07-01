import openai
import asyncio
from collections import defaultdict
from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.client.bot import DefaultBotProperties
from TelegramBot.deepSeekVS.config import key, tg_token

openai.api_key = key
openai.base_url = "https://api.deepseek.com"

router = Router()
bot = Bot(tg_token, default=DefaultBotProperties(parse_mode='HTML'))
user_messages = defaultdict(list)

@router.message()
async def get_msg(message: Message):
    chat_id = message.chat.id
    text = message.text
    user_messages[chat_id].append({"role": "user", "content": text})

    answer = await ask_gpt(user_messages[chat_id])
    user_messages[chat_id].append({"role": "system", "content": answer})

    await message.reply(answer)

async def ask_gpt(messages):
    response = openai.chat.completions.create(
        model="deepseek-chat",
        messages=messages
    )
    return response.choices[0].message.content

async def main():
    print("Запуск телеграм бота")
    dp = Dispatcher()
    dp.include_routers(router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())







