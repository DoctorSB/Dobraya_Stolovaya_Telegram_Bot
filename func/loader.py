from func.config import BOT_TOKEN, URL
from aiogram import Bot, Dispatcher, types
from func.dowloader import Dowloader
from func.parsing import Parser
from func.dson import Data


bot = Bot(token=BOT_TOKEN, parse_mode=types.ParseMode.HTML)

dp = Dispatcher(bot)

dowloader = Dowloader(URL).get_html()
parser = Parser(dowloader)
parser.save()
data = Data('data/menu.json')
