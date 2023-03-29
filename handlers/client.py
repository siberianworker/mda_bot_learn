from aiogram import types, Dispatcher
from aiogram.types import InputMediaPhoto
from create_bot import dp, bot
from keyboards import client_kb
from information import base


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

#Плюсофон
plusofon1 = 'AgACAgIAAxkBAAICCWQf43KvPP8FqAe4o8nTL58O6gerAAI4yDEbUhcBSTfqSRhX4fcwAQADAgADeQADLwQ'
img_plus1 = InputMediaPhoto(plusofon1)
plusofon2 = 'AgACAgIAAxkBAAICDmQf9YivnE0LH--gb9YPrxKVJxhvAAJ-yDEbUhcBSSuaz0I5bdxjAQADAgADeQADLwQ'
img_plus2 = InputMediaPhoto(plusofon2)
plusofon3 = 'AgACAgIAAxkBAAICEmQf93Ls2igZKcNOZrOu8N-8AT1vAAKHyDEbUhcBSdMvyiqn6-j_AQADAgADeQADLwQ'
img_plus3 = InputMediaPhoto(plusofon3)
plusofon4 = 'AgACAgIAAxkBAAICFGQf-wpn7Qjwr3Ohvoa81cHpsvnLAAKUyDEbUhcBSd8pXnF4AAE3nQEAAwIAA3kAAy8E'
img_plus4 = InputMediaPhoto(plusofon4, base.plus4)
plusofon5 = 'AgACAgIAAxkBAAICFmQf_aMtS3-xryLp9zdRV_187-Y-AAKgyDEbUhcBSRHAHV99NpjUAQADAgADeQADLwQ'
img_plus5 = InputMediaPhoto(plusofon5, base.plus5)
plusofon6 = 'AgACAgIAAxkBAAICGGQgAkzgFPqpVu0fzfU32tHyDr4oAAKyyDEbUhcBSW_VneM6NY0nAQADAgADeQADLwQ'
img_plus6 = InputMediaPhoto(plusofon6, base.plus6)
plusofon7 = 'AgACAgIAAxkBAAICGmQgGPZzUyIaJ8f5R28KqU95qUcuAAIFyTEbUhcBSXK3p3rXZHk0AQADAgADeQADLwQ'
img_plus7 = InputMediaPhoto(plusofon7)
plusofon8 = 'AgACAgIAAxkBAAICHGQgIHDDY-CrRlLFU3imdYCcR-bgAAIlyTEbUhcBSQz-xG555HdSAQADAgADeQADLwQ'
img_plus8 = InputMediaPhoto(plusofon8, base.plus8)
plusofon9 = 'AgACAgIAAxkBAAICHmQgJ1geELYT7w49GvcYy4SkJIl0AAJCyTEbUhcBSRh4iwgWNj7CAQADAgADeQADLwQ'
img_plus9 = InputMediaPhoto(plusofon9, base.plus9)
plusofon10 = 'AgACAgIAAxkBAAICIGQgSEqOkUBM0A5zbVT2rDpN_AjMAAKyyTEbUhcBSTc1Xi5w9Q2MAQADAgADeQADLwQ'
img_plus10 = InputMediaPhoto(plusofon10)
plusofon11 = 'AgACAgIAAxkBAAICImQgSpW15G63woU_hiUtxR2F8804AALryDEbUhcJSTU08yXfyJYdAQADAgADeQADLwQ'
img_plus11 = InputMediaPhoto(plusofon11, base.plus11)
plusofon12 = 'AgACAgIAAxkBAAICJGQgTgABZwOHK2G5tkIvxXhLK-XLMwAC-sgxG1IXCUk_yeuUfPXo_QEAAwIAA3kAAy8E'
img_plus12 = InputMediaPhoto(plusofon12, base.plus12)
plusofon13 = 'AgACAgIAAxkBAAICJmQgT6EB6dbk7gbitLSS7_mT8BXmAAIDyTEbUhcJSVpHGk_q-0YXAQADAgADeQADLwQ'
img_plus13 = InputMediaPhoto(plusofon13)
plusofon14 = 'AgACAgIAAxkBAAICKGQgUWOjOOSrcPGoy3x5iQvZb_JrAAIMyTEbUhcJSceNiIT6SXQ0AQADAgADeQADLwQ'
img_plus14 = InputMediaPhoto(plusofon14, base.plus14)
plusofon15 = 'AgACAgIAAxkBAAICKmQgU2LR-THqy6DMBN4AAUdV7leWtwACFckxG1IXCUnhFwfQL3TKnwEAAwIAA3kAAy8E'
img_plus15 = InputMediaPhoto(plusofon15, base.plus15)

#Qiwi
qiwi2 = 'AgACAgIAAxkBAAICRmQhh9rK5qz4i_pUhFrL0nOst7HcAAKjxTEbUhcRSQHSp6HqvwbrAQADAgADeQADLwQ'
img_qiwi2 = InputMediaPhoto(qiwi2, base.qiwi2)
qiwi3 = 'AgACAgIAAxkBAAICTWQhxUGG_8EJMapeCcuBYvAWCjMcAALaxjEbUhcRSX3KcJx95t-VAQADAgADeAADLwQ'
img_qiwi3 = InputMediaPhoto(qiwi3, base.qiwi3)
qiwi4 = 'AgACAgIAAxkBAAICU2Qhy_4EELcjiLabn_akvMk2YGgDAAJR0jEb-bQRSSziddtZVZcLAQADAgADeQADLwQ'
img_qiwi4 = InputMediaPhoto(qiwi4, base.qiwi4)
qiwi5 = 'AgACAgIAAxkBAAICVWQhzwN8ojjEQk9b0-H2Xx9MWiy4AAJU0jEb-bQRSbmYSfj7DMBTAQADAgADeQADLwQ'
img_qiwi5 = InputMediaPhoto(qiwi5, base.qiwi5)
qiwi6 = 'AgACAgIAAxkBAAICV2Qh0OT7baaPEH9vf5z1fVhaOu2yAAJ20jEb-bQRSQlyIiJTla9FAQADAgADeQADLwQ'
img_qiwi6 = InputMediaPhoto(qiwi6, base.qiwi6)
qiwi7 = 'AgACAgIAAxkBAAICWWQh0lbN2VIeJ7rZAAHcLTpXPOJt8AACotIxG_m0EUm5Tewp8imY2AEAAwIAA3kAAy8E'
img_qiwi7 = InputMediaPhoto(qiwi7, base.qiwi7)

#Модульбанк
modulbank = 'AgACAgIAAxkBAAICXGQh1b82RFDRbpTHickxKkObBMTyAALZ0jEb-bQRScV6L3UTmvL2AQADAgADeQADLwQ'
img_modul = InputMediaPhoto(modulbank, base.run_modul)
modulbank1 = 'AgACAgIAAxkBAAICYWQh3qSTFzKVFrKEQSC8QglPaFlFAAIM0zEb-bQRSczWRA__rAY-AQADAgADeQADLwQ'
img_modul1 = InputMediaPhoto(modulbank1, base.modul1)

#ОнлайнСИМ
osim1 = 'AgACAgIAAxkBAAICbmQisCv8yLwmZpCRq6XdLdVIW0ydAALhzzEb-bQZSbwRauvvms9mAQADAgADeQADLwQ'
img_osim1 = InputMediaPhoto(osim1, base.osim1)
osim2 = 'AgACAgIAAxkBAAICc2QizEPKPfYd4CA4Icy4uqIBArFwAAKF0DEb-bQZSZ5HlgABN-O_4gEAAwIAA3kAAy8E'
img_osim2 = InputMediaPhoto(osim2, base.osim2)
osim3 = 'AgACAgIAAxkBAAICd2Qiz1DdFdvZ4f0VG5G-KvjZGMWlAAKO0DEb-bQZSTszDL4jWCLyAQADAgADeQADLwQ'
img_osim3 = InputMediaPhoto(osim3, base.osim3)
osim4 = 'AgACAgIAAxkBAAICeWQi02PVcG6fRum4rwzZLHq6tmUrAAKb0DEb-bQZSYfCxvkj9k11AQADAgADeQADLwQ'
img_osim4 = InputMediaPhoto(osim4, base.osim4)

#SMS-activate
activ1 = 'AgACAgIAAxkBAAICfGQi3HJ-6yHjNO1apU6Mi5S0OtPZAAIi0TEb-bQZSTSU0iTseDBVAQADAgADeAADLwQ'
img_activ1 = InputMediaPhoto(activ1, base.activ1)
activ2 = 'AgACAgIAAxkBAAICgWQj9nXLKigjz3yKUFRiH7j4PZq_AALPyDEbBDkgSftU5-r89RykAQADAgADeAADLwQ'
img_activ2 = InputMediaPhoto(activ2, base.activ2)
activ3 = 'AgACAgIAAxkBAAICjWQj-cUGl3YDgo-FwGgqQLI4WUAkAALbyDEbBDkgSTsZ4ZJiiKc6AQADAgADeAADLwQ'
img_activ3 = InputMediaPhoto(activ3, base.activ3)


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
    elif callback.data == 'next_plus':
        await callback.message.answer_photo(plusofon1, reply_markup=client_kb.ikplus1)
        await callback.message.delete()
    elif callback.data == 'next_plus1':
        await callback.message.edit_media(img_plus2, reply_markup=client_kb.ikplus2)
    elif callback.data == 'next_plus2':
        await callback.message.edit_media(img_plus3, reply_markup=client_kb.ikplus3)
    elif callback.data == 'next_plus3':
        await callback.message.edit_media(img_plus4, reply_markup=client_kb.ikplus4)
    elif callback.data == 'next_plus4':
        await callback.message.edit_media(img_plus5, reply_markup=client_kb.ikplus5)
    elif callback.data == 'next_plus5':
        await callback.message.edit_media(img_plus6, reply_markup=client_kb.ikplus6)
    elif callback.data == 'next_plus6':
        await callback.message.edit_media(img_plus7, reply_markup=client_kb.ikplus7)
    elif callback.data == 'next_plus7':
        await callback.message.edit_media(img_plus8, reply_markup=client_kb.ikplus8)
    elif callback.data == 'next_plus8':
        await callback.message.edit_media(img_plus9, reply_markup=client_kb.ikplus9)
    elif callback.data == 'next_plus9':
        await callback.message.edit_media(img_plus10, reply_markup=client_kb.ikplus10)
    elif callback.data == 'next_plus10':
        await callback.message.edit_media(img_plus11, reply_markup=client_kb.ikplus11)
    elif callback.data == 'next_plus11':
        await callback.message.edit_media(img_plus12, reply_markup=client_kb.ikplus12)
    elif callback.data == 'next_plus12':
        await callback.message.edit_media(img_plus13, reply_markup=client_kb.ikplus13)
    elif callback.data == 'next_plus13':
        await callback.message.edit_media(img_plus14, reply_markup=client_kb.ikplus14)
    elif callback.data == 'next_plus14':
        await callback.message.edit_media(img_plus15, reply_markup=client_kb.ikplus15)

    #Закрываются ветки смс
    elif callback.data == 'exit_sms':
        await callback.message.answer(base.run_bank, reply_markup=client_kb.ikbank)
        await callback.message.delete()

    #Киви
    elif callback.data == 'run_qiwi':
        await callback.message.edit_text(base.run_qiwi, reply_markup=client_kb.ikqiwi)
    elif callback.data == 'next_qiwi':
        await callback.message.edit_text(base.qiwi1, reply_markup=client_kb.ikqiwi1)
    elif callback.data == 'next_qiwi1':
        await callback.message.answer_photo(qiwi2, base.qiwi2, reply_markup=client_kb.ikqiwi2)
        await callback.message.delete()
    elif callback.data == 'next_qiwi2':
        await callback.message.edit_media(img_qiwi3, reply_markup=client_kb.ikqiwi3)
    elif callback.data == 'next_qiwi3':
        await callback.message.edit_media(img_qiwi4, reply_markup=client_kb.ikqiwi4)
    elif callback.data == 'next_qiwi4':
        await callback.message.edit_media(img_qiwi5, reply_markup=client_kb.ikqiwi5)
    elif callback.data == 'next_qiwi5':
        await callback.message.edit_media(img_qiwi6, reply_markup=client_kb.ikqiwi6)
    elif callback.data == 'next_qiwi6':
        await callback.message.edit_media(img_qiwi7, reply_markup=client_kb.ikqiwi7)
    elif callback.data == 'next_qiwi7':
        await callback.message.answer(base.run_reg, reply_markup=client_kb.ikreg)
        await callback.message.delete()

    #Модульбанк
    elif callback.data == 'run_modulbank':
        await callback.message.answer_photo(modulbank, reply_markup=client_kb.ikmodul)
        await callback.message.delete()
    elif callback.data == 'next_modul':
        await callback.message.edit_media(img_modul1, reply_markup=client_kb.ikmodul1)
    elif callback.data == 'next_modul1':
        await callback.message.answer(base.run_reg, reply_markup=client_kb.ikreg)
        await callback.message.delete()

    #ОнлайнСИМ
    elif callback.data == 'onlinesim':
        await callback.message.edit_text(base.run_osim, reply_markup=client_kb.ikosim)
    elif callback.data == 'next_osim':
        await callback.message.answer_photo(osim1, base.osim1, reply_markup=client_kb.ikosim1)
        await callback.message.delete()
    elif callback.data == 'next_osim1':
        await callback.message.edit_media(img_osim2, reply_markup=client_kb.ikosim2)
    elif callback.data == 'next_osim2':
        await callback.message.edit_media(img_osim3, reply_markup=client_kb.ikosim3)
    elif callback.data == 'next_osim3':
        await callback.message.edit_media(img_osim4, reply_markup=client_kb.ikosim4)

    #SMS-activate
    elif callback.data == 'activate':
        await callback.message.edit_text(base.run_activ, reply_markup=client_kb.ikactiv)
    elif callback.data == 'next_activ':
        await callback.message.answer_photo(activ1, base.activ1, reply_markup=client_kb.ikactiv1)
        await callback.message.delete()
    elif callback.data == 'next_activ1':
        await callback.message.edit_media(img_activ2, reply_markup=client_kb.ikactiv2)
    elif callback.data == 'next_activ2':
        await callback.message.edit_media(img_activ3, reply_markup=client_kb.ikactiv3)


#####################################Пропустить############################
    #Смс
    elif callback.data == 'skip_sms':
        await callback.message.edit_text(base.run_bank, reply_markup=client_kb.ikbank)
    #Банк
    elif callback.data == 'skip_bank':
        await callback.message.edit_text(base.run_reg, reply_markup=client_kb.ikreg)


#####################################Назад#################################
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

    #Плюсофон
    elif callback.data == 'back_plus1':
        await callback.message.answer(text=base.run_plusofon, reply_markup=client_kb.ikplus)
        await callback.message.delete()
    elif callback.data == 'back_plus2':
        await callback.message.edit_media(img_plus1, reply_markup=client_kb.ikplus1)
    elif callback.data == 'back_plus3':
        await callback.message.edit_media(img_plus2, reply_markup=client_kb.ikplus2)
    elif callback.data == 'back_plus4':
        await callback.message.edit_media(img_plus3, reply_markup=client_kb.ikplus3)
    elif callback.data == 'back_plus5':
        await callback.message.edit_media(img_plus4, reply_markup=client_kb.ikplus4)
    elif callback.data == 'back_plus6':
        await callback.message.edit_media(img_plus5, reply_markup=client_kb.ikplus5)
    elif callback.data == 'back_plus7':
        await callback.message.edit_media(img_plus6, reply_markup=client_kb.ikplus6)
    elif callback.data == 'back_plus8':
        await callback.message.edit_media(img_plus7, reply_markup=client_kb.ikplus7)
    elif callback.data == 'back_plus9':
        await callback.message.edit_media(img_plus8, reply_markup=client_kb.ikplus8)
    elif callback.data == 'back_plus10':
        await callback.message.edit_media(img_plus9, reply_markup=client_kb.ikplus9)
    elif callback.data == 'back_plus11':
        await callback.message.edit_media(img_plus10, reply_markup=client_kb.ikplus10)
    elif callback.data == 'back_plus12':
        await callback.message.edit_media(img_plus11, reply_markup=client_kb.ikplus11)
    elif callback.data == 'back_plus13':
        await callback.message.edit_media(img_plus12, reply_markup=client_kb.ikplus12)
    elif callback.data == 'back_plus14':
        await callback.message.edit_media(img_plus13, reply_markup=client_kb.ikplus13)
    elif callback.data == 'back_plus15':
        await callback.message.edit_media(img_plus14, reply_markup=client_kb.ikplus14)

    #Назад к смс
    elif callback.data == 'back_in_sms':
        await callback.message.edit_text(base.run_sms, reply_markup=client_kb.iksms)

    #Назад к банку (qiwi)
    elif callback.data == 'back_bank':
        await callback.message.edit_text(base.run_bank, reply_markup=client_kb.ikbank)

    #Модульбанк
    elif callback.data == 'back_modul':
        await callback.message.answer(base.run_bank, reply_markup=client_kb.ikbank)
        await callback.message.delete()
    elif callback.data == 'back_modul1':
        await callback.message.edit_media(img_modul, reply_markup=client_kb.ikmodul)

    #Киви
    elif callback.data == 'back_qiwi1':
        await callback.message.edit_text(base.run_qiwi, reply_markup=client_kb.ikqiwi)
    elif callback.data == 'back_qiwi2':
        await callback.message.answer(base.qiwi1, reply_markup=client_kb.ikqiwi1)
        await callback.message.delete()
    elif callback.data == 'back_qiwi3':
        await callback.message.edit_media(img_qiwi2, reply_markup=client_kb.ikqiwi2)
    elif callback.data == 'back_qiwi4':
        await callback.message.edit_media(img_qiwi3, reply_markup=client_kb.ikqiwi3)
    elif callback.data == 'back_qiwi5':
        await callback.message.edit_media(img_qiwi4, reply_markup=client_kb.ikqiwi4)
    elif callback.data == 'back_qiwi6':
        await callback.message.edit_media(img_qiwi5, reply_markup=client_kb.ikqiwi5)
    elif callback.data == 'back_qiwi7':
        await callback.message.edit_media(img_qiwi6, reply_markup=client_kb.ikqiwi6)

    #Назад к банку
    elif callback.data == 'back_in_bank':
        await callback.message.edit_text(base.run_bank, reply_markup=client_kb.ikbank)

    #Назад к регистрации аккаунтов
    elif callback.data == 'back_reg':
        await callback.message.edit_text(base.run_reg, reply_markup=client_kb.ikreg)

    #ОнлайнСИМ
    elif callback.data == 'back_osim1':
        await callback.message.answer(base.run_osim, reply_markup=client_kb.ikosim)
        await callback.message.delete()
    elif callback.data == 'back_osim2':
        await callback.message.edit_media(img_osim1, reply_markup=client_kb.ikosim1)
    elif callback.data == 'back_osim3':
        await callback.message.edit_media(img_osim2, reply_markup=client_kb.ikosim2)
    elif callback.data == 'back_osim4':
        await callback.message.edit_media(img_osim3, reply_markup=client_kb.ikosim3)

    #SMS-activate
    elif callback.data == 'back_activ1':
        await callback.message.answer(base.run_activ, reply_markup=client_kb.ikactiv)
        await callback.message.delete()
    elif callback.data == 'back_activ2':
        await callback.message.edit_media(img_activ1, reply_markup=client_kb.ikactiv1)
    elif callback.data == 'back_activ3':
        await callback.message.edit_media(img_activ2, reply_markup=client_kb.ikactiv2)


def register_handlers_client(dp : Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])