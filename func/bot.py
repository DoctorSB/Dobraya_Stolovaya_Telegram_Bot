from aiogram import types
from aiogram import Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import CommandStart
from func.loader import data
from func.loader import bot, dp
import datetime


global now

router = Router()

btn = []
key_b = []

for i in range(len(data.data.keys())):
    btn += [[f'{list(data.data.keys())[i]}']]
for i in range(len(btn)):
    key_b.append([KeyboardButton(text=btn[i][0])])
panel_choose_target = ReplyKeyboardMarkup(keyboard=key_b, resize_keyboard=True)

# Команда /start
async def start(message: types.message):
    await message.answer('Выберите позицию', reply_markup=panel_choose_target)

async def menu(message: types.Message):
    now = datetime.datetime.now().hour
    position = message.text
    if position in data.data.keys():
        count = 0
        for i in range(len(data.data[position])):
            time = "Завтрак"
            if now > 10 and now < 17:
                time = "Обед"
            elif now > 16:
                time = "Ужин"
            if data.data[position][i][time] != '—' and data.data[position][i][time] != '_':
                count += 1
                await bot.send_photo(message.chat.id, photo=f'{data.data[position][i]["img"]}')
                await bot.send_message(message.chat.id, f' {data.data[position][i]["Название"]} - {data.data[position][i][time]}')
        if count == 0:
            await bot.send_message(message.chat.id, text='Сейчас тут отсутвуют позиции')
    else:
        # найдти фотографию блюда которое ввел пользователь
        pass
