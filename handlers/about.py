from aiogram import types

import config
from loader import dp, bot
from keyboards.inline import photo_keyboard, voice_keyboard
from utils import get_photo_path, get_voice_path


@dp.message_handler(text=config.AVAILABLE_COMMANDS_TEXTS["photos"])
@dp.message_handler(commands=["photos"])
async def choose_photo(message: types.Message) -> types.Message:
    """ Выбрать интересуемое фото """
    await message.reply(text="Выберите интересуемую фотографию", reply_markup=photo_keyboard)


@dp.callback_query_handler(lambda query: query.data.endswith("photo") is True)
async def get_photo(callback_query: types.CallbackQuery) -> types.Message:
    """ Получить выбранное фото """
    await bot.answer_callback_query(callback_query.id)

    photo_path = get_photo_path(photo_type=callback_query.data)
    with photo_path.open(mode="rb") as photo_file:
        await bot.send_photo(chat_id=callback_query.from_user.id, photo=photo_file)

    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


@dp.message_handler(text=config.AVAILABLE_COMMANDS_TEXTS["voices"])
@dp.message_handler(commands=["voices"])
async def choose_voice_message(message: types.Message) -> types.Message:
    """ Выбрать интересуемое голосовое сообщение """
    await message.reply(text="Выберите интересуемое голосовое сообщение", reply_markup=voice_keyboard)


@dp.callback_query_handler(lambda query: query.data.endswith("voice") is True)
async def get_voice_message(callback_query: types.CallbackQuery) -> types.Message:
    """ Получить выбранное голосовое сообщение """
    await bot.answer_callback_query(callback_query.id)

    voice_path = get_voice_path(voice_type=callback_query.data)
    voice_file = types.InputFile(voice_path)

    await bot.send_voice(chat_id=callback_query.from_user.id, voice=voice_file)
    await bot.delete_message(chat_id=callback_query.from_user.id, message_id=callback_query.message.message_id)


@dp.message_handler(text=config.AVAILABLE_COMMANDS_TEXTS["about"])
@dp.message_handler(commands=["about"])
async def get_about_me_info(message: types.Message) -> types.Message:
    """ Получить краткую биографию """
    await message.reply(
        text=(
            "Мне 22 года, закончил школу с золотой медалью, имею диплом олимпиады РСОШ по математике.\n"
            "В этом году получил диплом о высшем образовании, закончив факультет информационных технологий "
            "и программирования университета ИТМО.\n"
            "Работаю в научном центре когнитивных разработок университета ИТМО уже полтора года, "
            "на текущий момент занимаюсь разработкой low-code платформы машинного обучения SMILE CLOUD.\n"
            "Люблю преподавание, в 2019 году подготовил более 60 ребят к егэ по математике, средний балл ~ 75. "
            "Считаю это крутым достижением, большинство ребят поступило в топовые вузы России!\n"
            "В 2023 году подготовил более 30 ребят в рамках федеральной образовательной программы \"Код будущего\" "
            "совместно с университетом Иннополис, преподавал курс \"Разработка парсеров на ЯП Python\".\n"
            "На текущий момент прохожу курсы профессиональной переподготовки по направлению "
            "\"Педагогическая деятельность в сфере дополнительного образования\" от университета Иннополис "
            "для получения квалификации \"Педагог дополнительного образования детей и взрослых\".\n"
            "Мечтаю в будущем открыть свою онлайн школу, связанную с информационными технологиями!"
        )
    )


@dp.message_handler(text=config.AVAILABLE_COMMANDS_TEXTS["hobbies"])
@dp.message_handler(commands=["hobbies"])
async def get_hobbies_info(message: types.Message) -> types.Message:
    """ Получить описание увлечений """
    await message.reply(
        text=(
            "Люблю все виды игр: настольные, компьютерные, спортивные.\n"
            "Занимался смешанными единоборствами на протяжении 4х лет, неплохо играю в баскетбол и хоккей,"
            " обожаю настольный теннис.\n"
            "Имеется приличная коллекция настольных игр, которая насчитывает свыше 20 интереснейших коробок!\n"
            "Самое главное увлечение - это музыка, играю на гитаре на протяжении 7 лет, "
            "умею играть интерстеллар и петь песни группы \"Кино\"! В будущем планирую карьеру музыканта.\n"
            "Всегда открыт к новым открытиям и приключениям)"
        )
    )


@dp.message_handler(text=config.AVAILABLE_COMMANDS_TEXTS["source_repo"])
@dp.message_handler(commands=["source_repo"])
async def get_source_repo_link(message: types.Message) -> types.Message:
    """ Получить ссылку на репозиторий """
    await message.reply(text=f"Лови ссылку на <a href='{config.SOURCE_REPO_LINK}'>репозиторий</a>!", parse_mode="HTML")
