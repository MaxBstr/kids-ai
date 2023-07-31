from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from config import AVAILABLE_COMMANDS_TEXTS

menu_keyboard = ReplyKeyboardMarkup(
    resize_keyboard=True,
    one_time_keyboard=True,
    row_width=1
)

buttons = [
    KeyboardButton(text=AVAILABLE_COMMANDS_TEXTS["photos"]),
    KeyboardButton(text=AVAILABLE_COMMANDS_TEXTS["about"]),
    KeyboardButton(text=AVAILABLE_COMMANDS_TEXTS["hobbies"]),
    KeyboardButton(text=AVAILABLE_COMMANDS_TEXTS["voices"]),
    KeyboardButton(text=AVAILABLE_COMMANDS_TEXTS["source_repo"]),
    KeyboardButton(text=AVAILABLE_COMMANDS_TEXTS["cancel"]),
]

menu_keyboard.add(*buttons)
