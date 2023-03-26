from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

home = InlineKeyboardButton(text='С начала 🔝', callback_data='start')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
back1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back1')
back_sms = InlineKeyboardButton(text='Назад 🔙', callback_data='back_sms')
exit_serv_pc = InlineKeyboardButton(text='Продолжить ✅', callback_data='exit')
back_pc = InlineKeyboardButton(text='Назад 🔙', callback_data='back_pc')

url_rdp_win = 'https://apps.microsoft.com/store/detail/%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9-\
              %D1%81%D1%82%D0%BE%D0%BB-%D0%BC%D0%B0%D0%B9%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D1%84%D1%82/9WZDNCRFJ3PS?hl=ru-ru&gl=ru&activetab=pivot%3Aoverviewtab'
url_rdp_mac = 'https://apps.apple.com/ru/app/microsoft-remote-desktop/id1295203466?mt=12'

#Начало
ika = InlineKeyboardMarkup(row_width=2)
ib = InlineKeyboardButton(text='Начать', callback_data='run')
ika.add(ib)

#Вторая
ikb = InlineKeyboardMarkup(row_width=2)
next1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='run1')
shablon1 = InlineKeyboardButton(text='Шаблон для доступов', url='https://docs.google.com/spreadsheets/d/1YQqEAYWyIrRUB2jr9dKVZr_x3Mz7qHNN3pBN1I_U_qQ/edit#gid=0')
ikb.add(next1, home).add(shablon1)

#Подготовка оборудования
ikc = InlineKeyboardMarkup(row_width=2)
#next2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='run2')
bpc = InlineKeyboardButton(text='Продолжить ✅', callback_data='pc')
ikc.add(bpc).add(home, back)

#ПК
ikpc = InlineKeyboardMarkup(row_width=2)
bserver = InlineKeyboardButton(text='Выбрать сервер', callback_data='server')
ikpc.add(exit_serv_pc).add(bserver).add(home, back1)

#Сервера
ikserver = InlineKeyboardMarkup(row_width=2)
serv1 = InlineKeyboardButton(text='Selectel', url='https://selectel.ru/?ref_code=e2d2d054d4')
serv2 = InlineKeyboardButton(text='Serfstack', url='https://client.serfstack.com/aff.php?aff=35')
next_serv = InlineKeyboardButton(text='Продолжить ✅', callback_data='run_serv')
ikserver.add(serv1, serv2).add(next_serv).add(home, back_pc)

#RDP
ikserver1 = InlineKeyboardMarkup(row_width=2)
serv1_1 = InlineKeyboardButton(text='Скачать для Windows', url=url_rdp_win)
serv1_2 = InlineKeyboardButton(text='Скачать для Mac', url=url_rdp_mac)
back2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back2')
ikserver1.add(serv1_1, serv1_2).add(exit_serv_pc).add(home, back2)

#Регистрируем СМС сервисы
iksms = InlineKeyboardMarkup(row_width=2)
zadarma = InlineKeyboardButton(text='Zadarma', callback_data='run_zad')
plusofon = InlineKeyboardButton(text='Плюсофон', callback_data='run_plus')
#back_server = InlineKeyboardButton(text='Назад 🔙', callback_data='back_server')
iksms.add(zadarma, plusofon).add(back_pc, home)


#Задарма
ikzad = InlineKeyboardMarkup(row_width=2)
zad_vid1 = InlineKeyboardButton(text='Видео 1 часть', url='https://youtu.be/DWcpuXONPho')
zad_vid2 = InlineKeyboardButton(text='Видео 2 часть', url='https://youtu.be/Cnn88_iVUqc')
zad_url = InlineKeyboardButton(text='Регистрация', url='https://zadarma.com/ru/?ref=dcf761984bc63ea302d80c33bd61361f')
next_zad = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad')
ikzad.add(zad_vid1, zad_vid2).add(zad_url).add(next_zad).add(home, back_sms)

ikzad1 = InlineKeyboardMarkup(row_width=2)
next_zad1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad1')
back_zad1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad1')
ikzad1.add(next_zad1).add(back_zad1, home)

ikzad2 = InlineKeyboardMarkup(row_width=2)
next_zad2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad2')
back_zad2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad2')
ikzad2.add(next_zad2).add(back_zad2, home)

ikzad3 = InlineKeyboardMarkup(row_width=2)
next_zad3 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad3')
back_zad3 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad3')
ikzad3.add(next_zad3).add(back_zad3, home)

ikzad4 = InlineKeyboardMarkup(row_width=2)
next_zad4 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad4')
zad_chat = InlineKeyboardButton(text='Чат поддержки', url='https://t.me/MDA_teh')
back_zad4 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad4')
ikzad4.add(zad_chat).add(next_zad4).add(back_zad4, home)

ikzad5 = InlineKeyboardMarkup(row_width=2)
next_zad5 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad5')
back_zad5 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad5')
ikzad5.add(next_zad5).add(back_zad5, home)

ikzad6 = InlineKeyboardMarkup(row_width=2)
next_zad6 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad6')
back_zad6 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad6')
ikzad6.add(next_zad6).add(back_zad6, home)

ikzad7 = InlineKeyboardMarkup(row_width=2)
#next_zad7 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad7')
back_zad7 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad7')
ikzad7.add(back_zad7, home)


#Плюсофон
ikplus = InlineKeyboardMarkup(row_width=2)
plus_url = InlineKeyboardButton(text='Регистрация', url='https://new-portal.plusofon.ru/signup-user?promocode=qekv')
next_plus = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus')
ikplus.add(plus_url).add(next_plus).add(home, back_sms)

ikplus1 = InlineKeyboardMarkup(row_width=2)
next_plus1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus1')
back_plus1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus1')
ikplus1.add(next_plus1).add(home, back_plus1)

ikplus2 = InlineKeyboardMarkup(row_width=2)
next_plus2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus2')
back_plus2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus2')
ikplus2.add(next_plus2).add(home, back_plus2)

ikplus3 = InlineKeyboardMarkup(row_width=2)
next_plus3 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus3')
back_plus3 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus3')
ikplus3.add(next_plus3).add(home, back_plus3)

ikplus4 = InlineKeyboardMarkup(row_width=2)
next_plus4 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus4')
back_plus4 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus4')
ikplus4.add(next_plus4).add(home, back_plus4)

ikplus5 = InlineKeyboardMarkup(row_width=2)
next_plus5 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus5')
back_plus5 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus5')
ikplus5.add(next_plus5).add(home, back_plus5)

ikplus6 = InlineKeyboardMarkup(row_width=2)
next_plus6 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus6')
back_plus6 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus6')
ikplus6.add(next_plus6).add(home, back_plus6)

ikplus7 = InlineKeyboardMarkup(row_width=2)
next_plus7 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus7')
back_plus7 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus7')
ikplus7.add(next_plus7).add(home, back_plus7)

ikplus8 = InlineKeyboardMarkup(row_width=2)
next_plus8 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus8')
back_plus8 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus8')
ikplus8.add(next_plus8).add(home, back_plus8)

ikplus9 = InlineKeyboardMarkup(row_width=2)
next_plus9 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus9')
back_plus9 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus9')
ikplus9.add(next_plus9).add(home, back_plus9)

ikplus10 = InlineKeyboardMarkup(row_width=2)
next_plus10 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus10')
back_plus10 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus10')
ikplus10.add(next_plus10).add(home, back_plus10)

ikplus11 = InlineKeyboardMarkup(row_width=2)
next_plus11 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus11')
back_plus11 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus11')
ikplus11.add(next_plus11).add(home, back_plus11)

ikplus12 = InlineKeyboardMarkup(row_width=2)
next_plus12 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus12')
back_plus12 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus12')
ikplus12.add(next_plus12).add(home, back_plus12)

ikplus13 = InlineKeyboardMarkup(row_width=2)
next_plus13 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus13')
back_plus13 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus13')
ikplus13.add(next_plus13).add(home, back_plus13)

ikplus14 = InlineKeyboardMarkup(row_width=2)
next_plus14 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus14')
back_plus14 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus14')
ikplus14.add(next_plus14).add(home, back_plus14)

ikplus15 = InlineKeyboardMarkup(row_width=2)
#next_plus15 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus15')
back_plus15 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus15')
ikplus15.add(home, back_plus15)
