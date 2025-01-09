from datetime import datetime

from aiogram.types import CallbackQuery, Message, LabeledPrice, PreCheckoutQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F

from app.states import AddTrackState
from app.backend import get_action_by_user, get_daily_report

from app.keyboards.inline.menu_keyboard import back_keyboard
from app.keyboards.inline.my_tracking_keyboard import my_track_keyboard, back_or_update_keyboard

from app.keyboards.callbacks.my_track_callback import MyTrackCallback
from app.keyboards.callbacks.main_callback import MainCallback

my_tracking_router = Router()

@my_tracking_router.callback_query(MainCallback.filter(F.action == "my_track"))
async def command_start_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    try:
        result = get_action_by_user(callback_query.message.chat.id)
        
        await callback_query.message.edit_text("Ваши отслеживания:", reply_markup=my_track_keyboard(reports=result.get("result")))
        
    except Exception as e:
        result = get_action_by_user(callback_query.message.chat.id)
        
        await callback_query.message.answer("Ваши отслеживания:", reply_markup=my_track_keyboard(reports=result.get("result")))
        
@my_tracking_router.callback_query(MyTrackCallback.filter(F.action == "get_report"))
async def command_start_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    try:
        track_id = callback_query.data.split(":")[2]
        
        result = get_daily_report(chat_id=track_id)
        
        if result.get("status"):
            data = result.get("result").get("documents")[0]
            text = f"""
🌟 Информация о пользователе 🌟
🆔 ID отчёта: {data.get('id', 'N/A')}  
👤 Имя пользователя: {data.get('username', 'N/A')}  
📅 Дата создания отчёта: {data.get('creation_date', 'N/A')}  
⏰ Самый частопосещаемый час в сутки: {data.get('most_visited_hour', 'N/A')}  
⏳ Сегодня проведено в телеграм: {data.get('total', 'N/A')}  

🔄 Обновлено: {datetime.now().isoformat()}
            """
            
            username = data.get('username')
            await callback_query.message.edit_text(text=text, reply_markup=back_or_update_keyboard(track_id=username))
        
    except Exception as e:
        track_id = callback_query.data.split(":")[2]
        
        result = get_daily_report(chat_id=track_id)
        
        if result.get("status"):
            data = result.get("result")
            print(data)
            text = f"""
🌟 Информация о пользователе 🌟
🆔 ID отчёта: {data.get('id', 'N/A')}  
👤 Имя пользователя: {data.get('username', 'N/A')}  
📅 Дата создания отчёта: {data.get('creation_date', 'N/A')}  
⏰ Самый частопосещаемый час в сутки: {data.get('most_visited_hour', 'N/A')}  
⏳ Сегодня проведено в телеграм: {data.get('total', 'N/A')}  
            """
            
            await callback_query.message.answer(text=text, reply_markup=back_or_update_keyboard(data.get('username')))