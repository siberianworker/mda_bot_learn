from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

from create_bot import dp, bot
from keyboards import client_kb
from information import base

zero = ''
one = 'AgACAgIAAxkBAAMhZBCgyEqr6sgPYWAaQcnII0O2mNMAAtHGMRtdjolIAqZh6sTIcecBAAMCAAN5AAMvBA'
two = 'AgACAgIAAxkBAAMrZBFpUnVjXGCwT_fCWqIfKuvMLZcAAnXDMRtdjpFIP2DSB_mtWt8BAAMCAAN5AAMvBA'
three = 'AgACAgIAAxkBAAMtZBFpZXyc0W-UhG8p4hdyGsTYQa4AAnfDMRtdjpFIYjwY9EpRxrwBAAMCAAN5AAMvBA'

file0 = InputMediaPhoto(zero, caption=base.welcome)
file1 = InputMediaPhoto(one, caption=base.run)
file2 = InputMediaPhoto(two, caption=base.run1)
file3 = InputMediaPhoto(three, caption=base.run2)

async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, base.welcome, reply_markup=client_kb.ika)


@dp.callback_query_handler()
async def first_call(callback: types.CallbackQuery):

    if callback.data == 'start':
        await callback.message.delete()
        await callback.message.answer(text=base.welcome, reply_markup=client_kb.ika)
    elif callback.data == 'run':
        await callback.message.answer_photo(one, base.run, reply_markup=client_kb.ikb)
        await callback.message.delete()
    elif callback.data == 'run1':
        await callback.message.edit_media(file2, reply_markup=client_kb.ikc)
    elif callback.data == 'run2':
        await callback.message.edit_media(file3, reply_markup=client_kb.ikd)
    elif callback.data == 'back':
       await callback.message.edit_media(file1, reply_markup=client_kb.ikb)
    elif callback.data == 'back1':
        await callback.message.edit_media(file2, reply_markup=client_kb.ikc)



def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])