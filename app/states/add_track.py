from aiogram.fsm.state import State, StatesGroup

class AddTrackState(StatesGroup):
    user = State()
    username = State()
    plan = State()
