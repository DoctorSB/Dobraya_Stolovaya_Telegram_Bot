import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from parsing import Parser
from dowloader import Dowloader
from dson import Data
import datetime

now = datetime.datetime.now().hour

logging.basicConfig(level=logging.INFO)

bot = Bot(token='5771094021:AAFzTXEgzQf9oRMl0hAeISE_7ZJadSCGk-k')

dp = Dispatcher(bot)


url = 'https://dobraya.su/menu/'
dowloader = Dowloader(url)
html = dowloader.get_html()
parser = Parser(html)
parser.save()
data = Data('menu.json')

btn = []

for i in range(len(data.data.keys())):
    btn += [[f'{list(data.data.keys())[i]}']]
# print(btn)
key_b = []
for i in range(len(btn)):
    key_b.append([KeyboardButton(text=btn[i][0])])
print(type(key_b[0]))
panel_choose_target = ReplyKeyboardMarkup(keyboard=key_b, resize_keyboard=True)
print(panel_choose_target)


@dp.message_handler(commands=['start'])
async def hello(message: types.message):
    await bot.send_message(message.chat.id, 'Меню', reply_markup=panel_choose_target)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def menu(message: types.message):
    position = message.text
    if position in data.data.keys():
        for i in range(len(data.data[message.text])):
            time = "Завтрак"
            if now > 10 and now < 17:
                time = "Обед"
            elif now > 16:
                time = "Ужин"
            if data.data[message.text][i][time] != '—' and data.data[message.text][i][time] != '_':
                await bot.send_message(message.chat.id, f'{data.data[message.text][i]["Название"]} - {data.data[message.text][i][time]}')


async def start():
    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio

    print('бот запущен')
    asyncio.run(start())
