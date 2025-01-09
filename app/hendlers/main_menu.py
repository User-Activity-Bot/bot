import os
import aiohttp
from typing import Tuple, Dict
from urllib.parse import urlparse

from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram import Router, html, F

from app.keyboards.callbacks.main_callback import MainCallback
from app.keyboards.inline.menu_keyboard import start_keyboard
from app.backend import user_get_or_create, post_add_referral

start_router = Router()

@start_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    try:
        request = user_get_or_create(message.chat.id)
        
        if not request.get("result"):
            await message.answer(f"""Простите, произошла ошибка. Напишите /start позже, или обратитесь к админу.""")
        else:
            await message.answer(f"""Привет {message.from_user.username}""", reply_markup=start_keyboard(message.chat.id, is_start=True))
        await message.delete()
    except Exception as e:
        try:
            request = user_get_or_create(message.chat.id)
        except:
            await message.answer(f"""Простите, произошла ошибка. Напишите /start позже, или обратитесь к админу.""")
        
        if not request.get("result"):
            await message.answer(f"""Простите, произошла ошибка. Напишите /start позже, или обратитесь к админу.""")
        else:
            await message.answer(f"""Привет {message.from_user.username}""", reply_markup=start_keyboard(message.chat.id, is_start=True))
        await message.delete()
        
@start_router.callback_query(MainCallback.filter(F.action == "main_menu"))
async def command_start_handler(callback_query: CallbackQuery) -> None:
    try:
        request = user_get_or_create(callback_query.message.chat.id)
        
        if not request.get("result"):
            await callback_query.message.answer(f"""Простите, произошла ошибка. Напишите /start позже, или обратитесь к админу.""")
        else:
            await callback_query.message.answer(f"""Привет {callback_query.message.from_user.username}""", reply_markup=start_keyboard(callback_query.message.chat.id, is_start=True))
        await callback_query.message.delete()
    except Exception as e:
        try:
            request = user_get_or_create(callback_query.message.chat.id)
        except:
            await callback_query.message.answer(f"""Простите, произошла ошибка. Напишите /start позже, или обратитесь к админу.""")
        
        if not request.get("result"):
            await callback_query.message.answer(f"""Простите, произошла ошибка. Напишите /start позже, или обратитесь к админу.""")
        else:
            await callback_query.message.answer(f"""Привет {callback_query.message.from_user.username}""", reply_markup=start_keyboard(callback_query.message.chat.id, is_start=True))
        await callback_query.message.delete()