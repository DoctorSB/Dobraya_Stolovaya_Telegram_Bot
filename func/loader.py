from func.config import BOT_TOKEN, URL
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from func.dowloader import Dowloader
from func.parsing import Parser
from func.dson import Data
import asyncio


bot = Bot(token=BOT_TOKEN, parse_mode="HTML")


def menu():
    dowloader = Dowloader(URL).get_html()
    parser = Parser(dowloader)
    parser.save()
    data = Data('data/menu.json')
    return data


data = menu()


async def updater():
    while True:
        menu()
        await asyncio.sleep(8)

storage = MemoryStorage()

dp = Dispatcher(storage=storage)
