from aiogram.filters.callback_data import CallbackData

class MyTrackCallback(CallbackData, prefix="my_track"):
    action: str
    track_id: str