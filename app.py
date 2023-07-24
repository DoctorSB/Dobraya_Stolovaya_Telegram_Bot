import asyncio
from aiogram.filters import ContentTypesFilter, Command
from func.loader import dp, bot
from func.bot import *



async def startet():
    await dp.start_polling()
    

if __name__ == '__main__':
    print('бот запущен')
    asyncio.run(startet())
