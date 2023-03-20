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
#next_serv = InlineKeyboardButton(text='Продолжить ✅', callback_data='run_serv')
back_zad2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad2')
ikzad2.add(back_zad2, home)

#Плюсофон
ikplus = InlineKeyboardMarkup(row_width=2)
plus_url = InlineKeyboardButton(text='Регистрация', url='https://new-portal.plusofon.ru/signup-user?promocode=qekv')
ikplus.add(plus_url).add(home, back_sms)
