from aiogram.utils.keyboard import InlineKeyboardBuilder, InlineKeyboardMarkup
from aiogram.types.inline_keyboard_button import InlineKeyboardButton

from app.backend import action_by_id, change_alert_status

from app.keyboards.callbacks.my_track_callback import MyTrackCallback
from app.keyboards.callbacks.main_callback import MainCallback

from app.data.alert_dict import alert_status_dict


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
    
    result = action_by_id(id=track_id)
    
    if result.get("result"):
        alert = result.get("result").get("alert")
    
    back_keyboard.row(
        InlineKeyboardButton(
            text=f"🔄 Сообщения | {alert_status_dict.get(alert)}", 
            callback_data=MyTrackCallback(
                    action="change_message",
                    track_id=f"{track_id}"
                ).pack()
            ),
        )
    
    back_keyboard.row(
        InlineKeyboardButton(
            text=f"🔄 Изменить план", 
            callback_data=MyTrackCallback(
                    action="change_plan",
                    track_id=f"{track_id}"
                ).pack()
            ),
        )
    
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