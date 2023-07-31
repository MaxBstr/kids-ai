from pathlib import Path

from environs import Env


env = Env()
env.read_env()

MEDIA_ROOT = Path("media")
BOT_TOKEN = env.str("BOT_TOKEN")
SOURCE_REPO_LINK = env.str("SOURCE_REPO_LINK")

AVAILABLE_COMMANDS_TEXTS = {
    "menu": "Посмотреть список доступных команд",
    "photos": "Посмотреть фотографии",
    "about": "Почитать краткую биографию",
    "hobbies": "Почитать про мои увлечения",
    "voices": "Послушать голосовые",
    "source_repo": "Получить ссылку на репозиторий с исходниками бота",
    "cancel": "Отмена",
}
