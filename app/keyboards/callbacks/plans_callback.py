from aiogram.filters.callback_data import CallbackData

class PlansCallback(CallbackData, prefix="plan"):
    plan: str