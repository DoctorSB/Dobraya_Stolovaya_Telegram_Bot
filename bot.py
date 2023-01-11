import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from parsing import Parser
from dowloader import Dowloader
from dson import Data

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5771094021:AAFzTXEgzQf9oRMl0hAeISE_7ZJadSCGk-k')

dp = Dispatcher(bot)

btn=[]

url = 'https://dobraya.su/menu/'
dowloader = Dowloader(url)
html = dowloader.get_html()
parser = Parser(html)
parser.save()
print(type(parser))
data = Data('menu.json')
print(type(data))

panel_choose_target = ReplyKeyboardMarkup(
    keyboard=[[types.KeyboardButton(text=f'{data.data.keys()}') for _ in range(len(parser))]],
    resize_keyboard=True
)


@dp.message_handler(commands=['start'])
async def hello(message: types.message):
    await bot.send_message(message.chat.id, 'Меню', reply_markup=panel_choose_target)

async def start():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio

    print('бот запущен')
    asyncio.run(start())
