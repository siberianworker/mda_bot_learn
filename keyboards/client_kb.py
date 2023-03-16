from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

home = InlineKeyboardButton(text='С начала 🔝', callback_data='start')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
back1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back1')

#Начало
ika = InlineKeyboardMarkup(row_width=2)
ib = InlineKeyboardButton(text='Начать', callback_data='run')
ika.add(ib)

#Вторая
ikb = InlineKeyboardMarkup(row_width=2)
next1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='run1')
shablon1 = InlineKeyboardButton(text='Шаблон для доступов', url='https://docs.google.com/spreadsheets/d/1YQqEAYWyIrRUB2jr9dKVZr_x3Mz7qHNN3pBN1I_U_qQ/edit#gid=0')
ikb.add(next1, home).add(shablon1)

ikc = InlineKeyboardMarkup(row_width=2)
#next2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='run2')
pc = InlineKeyboardButton(text='На свой ПК', callback_data='pc')

ikc.add(pc).add(home, back)

ikd = InlineKeyboardMarkup(row_width=2)
ikd.add(home, back1)