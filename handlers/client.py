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
#media_group1 = [a1, a2]

#Хеш картинок
shablon = 'AgACAgIAAxkBAAOLZBG8UHDAENxv4hmz_EkEVg4xOncAAkLFMRtdjpFI6oXhDFP3l0YBAAMCAAN5AAMvBA'

#Задарма
zadarma_1 = 'AgACAgIAAxkBAAIB2GQYS8VougW1bM8XjRNSkvedaVmHAALb4DEboU3ASAHbssCutlfiAQADAgADeQADLwQ'
img_zad1 = InputMediaPhoto(zadarma_1, base.zad1)
zadarma_2 = 'AgACAgIAAxkBAAIB4WQYX0y8PMnnuVVcmjAxhQ_HHmljAAJn4TEboU3ASI3wWw4ioyCmAQADAgADeQADLwQ'
img_zad2 = InputMediaPhoto(zadarma_2, base.zad2)
zadarma_3 = 'AgACAgIAAxkBAAIB8WQYbPUbq5aTPXZfHTM8b9cLuUI4AALU4TEboU3ASPevLg-cA0xIAQADAgADeQADLwQ'
img_zad3 = InputMediaPhoto(zadarma_3, base.zad3)
zadarma_4 = 'AgACAgIAAxkBAAIB92QYcAzkEH0kLI4kQer-CLZ_iM0kAALc4TEboU3ASFJV0P3iZXtzAQADAgADeQADLwQ'
img_zad4 = InputMediaPhoto(zadarma_4, base.zad4)
zadarma_5 = 'AgACAgIAAxkBAAIB_mQZT4I0mJJDEafabl5kQldBM26tAAKAxTEbPZ7QSKWeuOHuBc38AQADAgADeQADLwQ'
img_zad5 = InputMediaPhoto(zadarma_5, base.zad5)
zadarma_6 = 'AgACAgIAAxkBAAICAmQZUjfPEA3JEcK5qZ_YVrXsdEqWAAImyDEb_wjISB-y2sSk24d6AQADAgADeQADLwQ'
img_zad6 = InputMediaPhoto(zadarma_6)
zadarma_7 = 'AgACAgIAAxkBAAICBGQZVLuuzljfjuj8cC65-I5k3oJ3AAI1yDEb_wjISAweAZQ57X0jAQADAgADeQADLwQ'
img_zad7 = InputMediaPhoto(zadarma_7, base.zad7)


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
        await callback.message.answer_photo(shablon, base.run, reply_markup=client_kb.ikb)
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
        await callback.message.edit_text(base.run_zadarma, reply_markup=client_kb.ikzad)
    elif callback.data == 'next_zad':
        await callback.message.answer_photo(zadarma_1, base.zad1, reply_markup=client_kb.ikzad1)
        await callback.message.delete()
    elif callback.data == 'next_zad1':
        await callback.message.edit_media(img_zad2, reply_markup=client_kb.ikzad2)
    elif callback.data == 'next_zad2':
        await callback.message.edit_media(img_zad3, reply_markup=client_kb.ikzad3)
    elif callback.data == 'next_zad3':
        await callback.message.edit_media(img_zad4, reply_markup=client_kb.ikzad4)
    elif callback.data == 'next_zad4':
        await callback.message.edit_media(img_zad5, reply_markup=client_kb.ikzad5)
    elif callback.data == 'next_zad5':
        await callback.message.edit_media(img_zad6, reply_markup=client_kb.ikzad6)
    elif callback.data == 'next_zad6':
        await callback.message.edit_media(img_zad7, reply_markup=client_kb.ikzad7)

    #Плюсофон
    elif callback.data == 'run_plus':
        await callback.message.edit_text(base.run_plusofon, reply_markup=client_kb.ikplus)


    #Назад
    elif callback.data == 'back':
        await callback.message.answer_photo(shablon, base.run, reply_markup=client_kb.ikb)
        await callback.message.delete()
    elif callback.data == 'back1':
        await callback.message.edit_text(text=base.run1, reply_markup=client_kb.ikc)
    elif callback.data == 'back2':
        await callback.message.edit_text(text=base.run2_2, reply_markup=client_kb.ikserver)
    elif callback.data == 'back_pc':
        await callback.message.edit_text(text=base.run2_1, reply_markup=client_kb.ikpc)
    elif callback.data == 'back_server':
        await callback.message.edit_text(text=base.run2_2_1, reply_markup=client_kb.ikserver1)
    elif callback.data == 'back_sms':
        await callback.message.edit_text(text=base.run_sms, reply_markup=client_kb.iksms)
    #Задарма
    elif callback.data == 'back_zad1':
        await callback.message.answer(text=base.run_zadarma, reply_markup=client_kb.ikzad)
        await callback.message.delete()
    elif callback.data == 'back_zad2':
        await callback.message.edit_media(img_zad1, reply_markup=client_kb.ikzad1)
    elif callback.data == 'back_zad3':
        await callback.message.edit_media(img_zad2, reply_markup=client_kb.ikzad2)
    elif callback.data == 'back_zad4':
        await callback.message.edit_media(img_zad3, reply_markup=client_kb.ikzad3)
    elif callback.data == 'back_zad5':
        await callback.message.edit_media(img_zad4, reply_markup=client_kb.ikzad4)
    elif callback.data == 'back_zad6':
        await callback.message.edit_media(img_zad5, reply_markup=client_kb.ikzad5)
    elif callback.data == 'back_zad7':
        await callback.message.edit_media(img_zad6, reply_markup=client_kb.ikzad6)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])