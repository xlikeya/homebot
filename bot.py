import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from get_weather import get_weather

from configuration import Configuration

confjson = Configuration.load_json('config.json')

API_TOKEN = confjson.telegram
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command('start', 'help'))
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("/weather - Погода в Новокузнецке \n ")

@dp.message(Command('weather'))
async def send_weather(message: types.Message):

    await message.reply(get_weather())

@dp.message()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Your text: " + msg.text)

    # Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())