from enum import StrEnum


class PhotoEnum(StrEnum):
    """ Типы фотографий """
    SELFIE = "selfie_photo"
    SCHOOL = "school_photo"


class VoiceMessageEnum(StrEnum):
    """ Типы голосовых сообщений """
    GPT = "gpt_voice"
    SQL = "sql_voice"
    LOVE = "love_voice"
