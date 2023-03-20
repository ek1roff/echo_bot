from aiogram import Router
from aiogram.types import Message
from lexicon.lexicon import LEXICON_RU

router: Router = Router()


@router.message()
async def send_echo(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        print(message.json(exclude_none=True, indent=4))
    except TypeError:
        await message.reply(text=LEXICON_RU['no_echo'])
