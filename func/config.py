from environs import Env, EnvValidationError
import os

env = Env()
env.read_env()


def get_bot_token():
    try:
        BOT_TOKEN = env.str("BOT_TOKEN")
    except EnvValidationError:
        BOT_TOKEN = os.environ['BOT_TOKEN']
    return BOT_TOKEN


def get_url():
    try:
        URL = env.str('URL')
    except EnvValidationError:
        URL = os.environ['URL']
    return URL


BOT_TOKEN = get_bot_token()
URL = get_url()
