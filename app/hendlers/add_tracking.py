from aiogram.types import CallbackQuery, Message, LabeledPrice, PreCheckoutQuery
from aiogram.fsm.context import FSMContext
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Router, F

from app.states import AddTrackState
from app.backend import create_actions, success_payment

from app.keyboards.inline.menu_keyboard import start_keyboard
from app.keyboards.inline.plans_keyboard import plans_keyboard
from app.keyboards.callbacks.main_callback import MainCallback

add_tracking_router = Router()

@add_tracking_router.callback_query(MainCallback.filter(F.action == "add_track"))
async def command_start_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    try:
        await callback_query.message.answer("Введи юзернейм для отслеживания: ")
        
        await state.set_state(AddTrackState.username)
        await state.update_data({"user" : str(callback_query.message.chat.id)})
        
    except Exception as e:
        print(e)
    
@add_tracking_router.message(AddTrackState.username)
async def create_transaction_amount_handler(message: Message, state: FSMContext) -> None:
    try:
        await state.update_data({"track_id" : message.text})
        
        await message.answer("Выберете тариф: ", reply_markup=plans_keyboard(message.chat.id))
        
        await state.set_state(AddTrackState.plan)
        
    except Exception as e:
        print(e)
    
@add_tracking_router.callback_query(AddTrackState.plan)
async def create_transaction_currency_handler(callback_query: CallbackQuery, state: FSMContext) -> None:
    try: 
        prefix, plan = callback_query.data.split(":")
        await state.update_data({"plan": plan})
        
        await callback_query.message.answer("Запрос для создания отслеживания отправлен")
        
        data = await state.get_data()
        request = create_actions(data)
        result = request.get("result")
        
        if not result:
            await callback_query.message.answer("Произошла ошибка")
            return

        if result.get("payment"):
            payment = result.get("payment")
            amount = payment.get("amount", 1)
            payload = f"{payment.get('id')}_stars"

            kb = InlineKeyboardBuilder()
            kb.button(
                text="Оплатить звёздами ⭐️", 
                pay=True
            )
            kb.button(
                text="Отменить",
                callback_data="donate_cancel"
            )
            
            kb.adjust(1)
            
            prices = [LabeledPrice(label="Оплата подписки", amount=amount)]

            await callback_query.message.answer_invoice(
                title="Оплата отслеживания активности аккаунта",
                description=f"Оплата плана {plan}",
                payload=payload,
                provider_token="",
                currency="XTR",
                prices=prices,
                reply_markup=kb.as_markup()
            )
        else:
            await state.clear()
            await callback_query.message.answer("Ваше бесплатное отслеживание добавленно")

    except Exception as e:
        print(f"Ошибка: {e}")
        await callback_query.message.answer("Произошла ошибка при обработке платежа.")

@add_tracking_router.pre_checkout_query()
async def pre_checkout_handler(query: PreCheckoutQuery):
    try:
        # Проверка перед подтверждением платежа
        await query.answer(ok=True)
    except Exception as e:
        print(f"Ошибка при подтверждении: {e}")
        await query.answer(ok=False, error_message="Произошла ошибка. Попробуйте снова.")

@add_tracking_router.message(F.successful_payment)
async def successful_payment_handler(message: Message, state: FSMContext):
    try:
        successful_payment = message.successful_payment
        payload = successful_payment.invoice_payload
        charge_id = successful_payment.telegram_payment_charge_id

        id, sufix = payload.split("_") 

        request = success_payment(id)
        
        if not request.get("status"):
            await message.answer("При обработке вашего платежа произошла ошибка. Обратитесь в поддержку! 🙏")
        
        await message.answer(
            f"✅ <b>Платёж успешно обработан!</b>\n\n"
            f"🆔 <b>Айди платежа:</b> <code>{id}</code>\n"
            f"💳 <b>ID транзакции:</b> <code>{charge_id}</code>\n\n"
            f"🎉 Спасибо за вашу покупку! Мы очень ценим вашу поддержку! 🙏",
            
            reply_markup=start_keyboard(message.chat.id),
        )
        await state.clear()
    except Exception as e:
        print(f"Ошибка при обработке успешного платежа: {e}")
        await message.answer("Произошла ошибка при обработке успешного платежа.")