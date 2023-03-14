from aiogram import types, Dispatcher
from create_bot import dp, bot
from keyboards import client_kb
from information import base


async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, base.welcome, reply_markup=client_kb.ika)

@dp.callback_query_handler()
async def first_call(callback: types.CallbackQuery):

    if callback.data == 'start':
        await callback.message.edit_text(text=base.welcome, reply_markup=client_kb.ika)
    elif callback.data == 'run':
        await callback.message.edit_text(text=base.run, reply_markup=client_kb.ikb)
    elif callback.data == 'run1':
        await callback.message.edit_text(text=base.run1, reply_markup=client_kb.ikc)
    elif callback.data == 'run2':
        await callback.message.edit_text(text=base.run2, reply_markup=client_kb.ikd)
    if callback.data == 'back':
        await callback.message.edit_text(text=base.run, reply_markup=client_kb.ikb)
    if callback.data == 'back1':
        await callback.message.edit_text(text=base.run1, reply_markup=client_kb.ikc)



#отлавливает информацию
#@dp.callback_query_handler(lambda callback: "info" in callback.data)
#async def info_callback(callback):
#    await callback.message.edit_reply_markup(client_kb.ikb4)





def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])