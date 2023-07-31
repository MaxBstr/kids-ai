from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from enums import PhotoEnum, VoiceMessageEnum


# --- PHOTOS ---
photo_buttons = [
    InlineKeyboardButton(text="Последнее селфи", callback_data=PhotoEnum.SELFIE.value),
    InlineKeyboardButton(text="Школьное фото", callback_data=PhotoEnum.SCHOOL.value),
]

photo_keyboard = InlineKeyboardMarkup(row_width=2)
photo_keyboard.add(*photo_buttons)


# --- VOICES ---
voice_buttons = [
    InlineKeyboardButton(text="Что такое Chat GPT простыми словами", callback_data=VoiceMessageEnum.GPT.value),
    InlineKeyboardButton(text="В чем различие SQL и NoSQL баз данных", callback_data=VoiceMessageEnum.SQL.value),
    InlineKeyboardButton(text="История первой любви", callback_data=VoiceMessageEnum.LOVE.value),
]

voice_keyboard = InlineKeyboardMarkup(row_width=1)
voice_keyboard.add(*voice_buttons)
