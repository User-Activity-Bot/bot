import os

from dotenv import load_dotenv, find_dotenv

from telethon import TelegramClient
from telethon.tl.types import UserStatusOnline, UserStatusOffline, UserStatusRecently

load_dotenv(find_dotenv())

api_id = os.getenv("API_ID")
api_hash = os.getenv("API_HASH")

client = TelegramClient('user_status_bot', api_id, api_hash)

async def get_user_status(username):
    try:
        user = await client.get_entity(username)

        print(user.status)

        if isinstance(user.status, UserStatusOnline):
            print(f"Пользователь {username} сейчас онлайн.")
        elif isinstance(user.status, UserStatusOffline):
            print(f"Пользователь {username} был оффлайн в {user.status.was_online}.")
        elif isinstance(user.status, UserStatusRecently):
            print(f"Пользователь {username} сейчас офлайн. Последний онлайн скрыт")
        else:
            print(f"Статус пользователя {username} неизвестен или скрыт.")

    except Exception as e:
        print(f"Ошибка: {e}")
