from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from app.filters import is_admin

from app.keyboards.callbacks.plans_callback import PlansCallback
from app.keyboards.callbacks.main_callback import MainCallback


def plans_keyboard(user_id : str, is_start : bool = False) -> InlineKeyboardMarkup:
    plans_keyboard = InlineKeyboardBuilder()
        
    plans_keyboard.row(
        InlineKeyboardButton(
            text="Бесплатный", 
            callback_data=PlansCallback(plan="free").pack()
        ),
    )
    
    plans_keyboard.row(
        InlineKeyboardButton(
            text="Уведомления", 
            callback_data=PlansCallback(plan="alert").pack()
        )
    )
    
    plans_keyboard.row(
        InlineKeyboardButton(
            text="Полная информация", 
            callback_data=PlansCallback(plan="full_data").pack()
        )
    )

    
    if not is_start:
        plans_keyboard.row(
            InlineKeyboardButton(text="🔙 К главному меню", callback_data=MainCallback(action="main_menu").pack())
        )
    
    if is_admin(user_id):
        plans_keyboard.row(
            InlineKeyboardButton(text="👑 Админ панель", callback_data=MainCallback(action="admin").pack())
        )
    
    return plans_keyboard.as_markup()

