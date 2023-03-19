from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto

from create_bot import dp, bot
from keyboards import client_kb
from information import base

#Тестовые
#one = 'AgACAgIAAxkBAAMhZBCgyEqr6sgPYWAaQcnII0O2mNMAAtHGMRtdjolIAqZh6sTIcecBAAMCAAN5AAMvBA'
#two = 'AgACAgIAAxkBAAMrZBFpUnVjXGCwT_fCWqIfKuvMLZcAAnXDMRtdjpFIP2DSB_mtWt8BAAMCAAN5AAMvBA'
#three = 'AgACAgIAAxkBAAMtZBFpZXyc0W-UhG8p4hdyGsTYQa4AAnfDMRtdjpFIYjwY9EpRxrwBAAMCAAN5AAMvBA'
#file1 = InputMediaPhoto(one, caption=base.run)
#file2 = InputMediaPhoto(two, caption=base.run1)
#file3 = InputMediaPhoto(three, caption=base.run2)

#Скачать шаблон
#a1 = 'AgACAgIAAxkBAAOJZBG8JlY8Lf_mzdIvJed1A18yj8UAAkDFMRtdjpFI-cEbWykYWaEBAAMCAAN4AAMvBA'
a1 = 'AgACAgIAAxkBAAOLZBG8UHDAENxv4hmz_EkEVg4xOncAAkLFMRtdjpFI6oXhDFP3l0YBAAMCAAN5AAMvBA'
#media_group1 = [a1, a2]


#Команда /start
async def command_start(message : types.Message):
    await bot.send_message(message.from_user.id, base.welcome, reply_markup=client_kb.ika)


@dp.callback_query_handler()
async def first_call(callback: types.CallbackQuery):
    #Возврат в начало
    if callback.data == 'start':
        await callback.message.delete()

        await callback.message.answer(text=base.welcome, reply_markup=client_kb.ika)
    elif callback.data == 'run':
        await callback.message.answer_photo(a1, base.run, reply_markup=client_kb.ikb)
        await callback.message.delete()
    elif callback.data == 'run1':
#        await callback.message.edit_media(file2, reply_markup=client_kb.ikc)
        await callback.message.answer(text=base.run1, reply_markup=client_kb.ikc)
        await callback.message.delete()
    elif callback.data == 'pc':
        await callback.message.edit_text(base.run2_1, reply_markup=client_kb.ikpc)

    #Ветка сервер
    elif callback.data == 'server':
        await callback.message.edit_text(base.run2_2, reply_markup=client_kb.ikserver)
    elif callback.data == 'run_serv':
        await callback.message.edit_text(base.run2_2_1, reply_markup=client_kb.ikserver1)

    #Закрываются ветки сервер и пк
    elif callback.data == 'exit':
        await callback.message.edit_text(base.run_sms, reply_markup=client_kb.iksms)

    #Задарма
    elif callback.data == 'run_zad':
        await callback.message.answer(text='В процессе')
    #Плюсофон
    elif callback.data == 'run_plus':
        await callback.message.answer(text='В процессе')


    #Назад
    elif callback.data == 'back':
        await callback.message.answer_photo(a1, base.run, reply_markup=client_kb.ikb)
        await callback.message.delete()
    elif callback.data == 'back1':
        await callback.message.edit_text(text=base.run1, reply_markup=client_kb.ikc)
    elif callback.data == 'back2':
        await callback.message.edit_text(text=base.run2_2, reply_markup=client_kb.ikserver)
    elif callback.data == 'back_pc':
        await callback.message.edit_text(text=base.run2_1, reply_markup=client_kb.ikpc)
    elif callback.data == 'back_server':
        await callback.message.edit_text(text=base.run2_2_1, reply_markup=client_kb.ikserver1)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])