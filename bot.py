import logging
from aiogram import Bot, Dispatcher, executor, types
from get_weather import get_weather

from configuration import Configuration

confjson = Configuration.load_json('config.json')

API_TOKEN = confjson.telegram
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("/weather - Погода в Новокузнецке \n ")

@dp.message_handler(commands=['weather'])
async def send_weather(message: types.Message):

    await message.reply(get_weather())

@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, "Your text: " + msg.text)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)