from pathlib import Path

from aiogram import types, Dispatcher

from config import MEDIA_ROOT, AVAILABLE_COMMANDS_TEXTS
from enums import PhotoEnum, VoiceMessageEnum


def get_photo_path(photo_type: str) -> Path:
    """ Получить путь до фотографии по типу """
    photos_dir = MEDIA_ROOT / "photos"
    match photo_type:
        case PhotoEnum.SELFIE:
            return photos_dir / "selfie.jpg"
        case PhotoEnum.SCHOOL:
            return photos_dir / "school.jpg"


def get_voice_path(voice_type: str) -> Path:
    """ Получить путь до голосового сообщения по типу """
    voices_dir = MEDIA_ROOT / "voices"
    match voice_type:
        case VoiceMessageEnum.GPT:
            return voices_dir / "gpt.ogg"
        case VoiceMessageEnum.SQL:
            return voices_dir / "sql.ogg"
        case VoiceMessageEnum.LOVE:
            return voices_dir / "love.ogg"


async def set_default_commands(dp: Dispatcher) -> bool:
    """ Настроить доступные команды бота """
    await dp.bot.set_my_commands(
        [
            types.BotCommand("menu", AVAILABLE_COMMANDS_TEXTS["menu"]),
            types.BotCommand("about", AVAILABLE_COMMANDS_TEXTS["about"]),
            types.BotCommand("hobbies", AVAILABLE_COMMANDS_TEXTS["hobbies"]),
            types.BotCommand("photos", AVAILABLE_COMMANDS_TEXTS["photos"]),
            types.BotCommand("voices", AVAILABLE_COMMANDS_TEXTS["voices"]),
            types.BotCommand("source_repo", AVAILABLE_COMMANDS_TEXTS["source_repo"]),
        ]
    )
