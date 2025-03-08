import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from aiogram.types import BotCommand, BotCommandScopeDefault

from get_weather import get_weather

from configuration import Configuration

confjson = Configuration.load_json('config.json')

API_TOKEN = confjson.telegram
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Set all commands
async def set_commands():
    commands = [BotCommand(command='start', description='Старт'),
                BotCommand(command='weather', description='Погода'),
                BotCommand(command='help', description='Помощь'),
                BotCommand(command='about', description='О разработчике')]
    await bot.set_my_commands(commands, BotCommandScopeDefault())

# Command processing
@dp.message(Command('start', 'help'))
async def send_welcome(message: types.Message):
    await message.reply("/weather - Погода в Новокузнецке \n"
                        "/help - Список доступных команд \n"
                        "/about - Информация о разработчике \n")


@dp.message(Command('about'))
async def send_about(message: types.Message):
    await message.reply("Разработчик бота: Конева Вера Александровна\n"
                        "Telegram: @vera_koneva\n")

@dp.message(Command('weather'))
async def send_weather(message: types.Message):
    await message.reply(get_weather())


# Starting the polling process for new updates
async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    await set_commands()

if __name__ == '__main__':
    asyncio.run(main())