from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from app.filters import is_admin

from app.keyboards.callbacks.main_callback import MainCallback

def start_keyboard(user_id : str, is_start : bool = False) -> InlineKeyboardMarkup:
    start_keyboard = InlineKeyboardBuilder()
        
    start_keyboard.row(
        InlineKeyboardButton(
            text="➕ Добавить пользователя для слежки", 
            callback_data=MainCallback(action="add_track").pack()
        ),
    )
    start_keyboard.row(
        InlineKeyboardButton(
            text="👁️ Отслеживаемые пользователи", 
            callback_data=MainCallback(action="my_track").pack()
        )
    )

    
    if False:
        start_keyboard.row(
            InlineKeyboardButton(text="🔙 К главному меню", callback_data=MainCallback(action="main_menu").pack())
        )
    
    if is_admin(user_id):
        start_keyboard.row(
            InlineKeyboardButton(text="👑 Админ панель", callback_data=MainCallback(action="admin").pack())
        )
    
    return start_keyboard.as_markup()

def back_keyboard() -> InlineKeyboardMarkup:
    back_keyboard = InlineKeyboardBuilder()
    
    back_keyboard.row(
        InlineKeyboardButton(text="🔙 Обновить", callback_data=MainCallback(action="main_menu").pack())
    )
    
    back_keyboard.row(
        InlineKeyboardButton(text="🔙 К главному меню", callback_data=MainCallback(action="main_menu").pack())
    )
    
    return back_keyboard.as_markup()