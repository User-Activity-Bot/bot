from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from app.filters import is_admin

from app.keyboards.callbacks.my_track_callback import MyTrackCallback
from app.keyboards.callbacks.main_callback import MainCallback


def my_track_keyboard(user_id : str = None, reports = None, is_start : bool = False) -> InlineKeyboardMarkup:
    my_track_keyboard = InlineKeyboardBuilder()
    
    for data in reports:
        my_track_keyboard.row(
            InlineKeyboardButton(
                text=f"{data.get('track_id')}", 
                callback_data=MyTrackCallback(
                        action="get_report",
                        track_id=f"{data.get('track_id')}"
                    ).pack()
            ),
        )
    
    if not is_start:
        my_track_keyboard.row(
            InlineKeyboardButton(text="🔙 К главному меню", callback_data=MainCallback(action="main_menu").pack())
        )
    
    return my_track_keyboard.as_markup()


def back_or_update_keyboard(track_id) -> InlineKeyboardMarkup:
    back_keyboard = InlineKeyboardBuilder()
    
    back_keyboard.row(
        InlineKeyboardButton(
            text=f"🔄 Обновить", 
            callback_data=MyTrackCallback(
                    action="get_report",
                    track_id=f"{track_id}"
                ).pack()
            ),
        )
    
    back_keyboard.row(
        InlineKeyboardButton(text="🔙 К главному меню", callback_data=MainCallback(action="main_menu").pack())
    )
    
    return back_keyboard.as_markup()