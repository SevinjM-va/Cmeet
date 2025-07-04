from aiogram import Bot, Dispatcher, types
import asyncio
import os

TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
  await message.answer("Привет! Я работаю.")

async def main():
  await dp.start_polling(bot)


if __name__ == "__main__":
  asyncio.run(main())