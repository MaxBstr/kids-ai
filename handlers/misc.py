from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.default import menu_keyboard
from loader import dp, bot
from config import AVAILABLE_COMMANDS_TEXTS


@dp.message_handler(CommandStart())
async def get_start_info(message: types.Message) -> types.message:
    """ Получить приветственное сообщение """
    await message.answer(
        text=(
            "Привет, меня зовут Максим!\n"
            "Давай знакомиться, выбирай интересующий тебя пункт!"
        ),
        reply_markup=menu_keyboard
    )


@dp.message_handler(text=AVAILABLE_COMMANDS_TEXTS["menu"])
@dp.message_handler(commands=["menu"])
async def show_menu(message: types.Message) -> types.Message:
    """ Показать меню доступных команд """
    await message.answer(
        text="Доступные команды",
        reply_markup=menu_keyboard
    )


@dp.message_handler(text=AVAILABLE_COMMANDS_TEXTS["cancel"], state="*")
async def cancel_call(message: types.Message) -> types.Message:
    """ Скрыть клавиатуру меню """
    await message.answer(text="Клавиатура скрыта", reply_markup=types.ReplyKeyboardRemove())


@dp.message_handler()
async def echo_message(msg: types.Message) -> types.Message:
    """ Ответить пользователю эхо-сообщением """
    await bot.send_message(chat_id=msg.from_user.id, text=msg.text)
