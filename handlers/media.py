from aiogram.types import ContentType, Message

from create_bot import dp


@dp.message_handler(content_types=ContentType.PHOTO)
async def send_foto_file_id(message: Message):
    await message.reply(message.photo[-1].file_id)

