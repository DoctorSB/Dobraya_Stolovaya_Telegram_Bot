from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from func.loader import data
from func.loader import bot, dp
import datetime


global now

btn = []
key_b = []

for i in range(len(data.data.keys())):
    btn += [[f'{list(data.data.keys())[i]}']]
for i in range(len(btn)):
    key_b.append([KeyboardButton(text=btn[i][0])])
panel_choose_target = ReplyKeyboardMarkup(keyboard=key_b, resize_keyboard=True)


@dp.message_handler(commands=['start'])
async def hello(message: types.message):
    await bot.send_message(message.chat.id, 'Меню', reply_markup=panel_choose_target)


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def menu(message: types.message):
    now = datetime.datetime.now().hour
    position = message.text
    if position in data.data.keys():
        count = 0
        for i in range(len(data.data[message.text])):
            time = "Завтрак"
            if now > 10 and now < 17:
                time = "Обед"
            elif now > 16:
                time = "Ужин"
            if data.data[message.text][i][time] != '—' and data.data[message.text][i][time] != '_':
                count += 1
                await bot.send_photo(message.chat.id, photo=f'{data.data[message.text][i]["img"]}')
                await bot.send_message(message.chat.id, f' {data.data[message.text][i]["Название"]} - {data.data[message.text][i][time]}')
        if count == 0:
            await bot.send_message(message.chat.id, text='Сейчас тут отсутвуют позиции')

