if __name__ == '__main__':
    from threading import Timer
    from aiogram import executor
    from func.loader import dp
    from func.bot import *

    print('бот запущен')
    t = Timer(1800.0, executor.start_polling(dp))
    t.start()
    