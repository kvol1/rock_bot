from aiogram import Dispatcher
from aiogram.types import Message

from lexicon.lexicon_ru import LEXICON_RU


async def send_answer(message: Message):
    await message.answer(text=LEXICON_RU['other_answer'])


def register_other_handlers(dp: Dispatcher):
    return register_other_handlers(send_answer)