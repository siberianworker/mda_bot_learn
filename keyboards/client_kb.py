from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

home = InlineKeyboardButton(text='С начала', callback_data='start')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
back1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back1')

#Начало
ika = InlineKeyboardMarkup(row_width=2)
ib = InlineKeyboardButton(text='Начать', callback_data='run')
ika.add(ib)

#Вторая
ikb = InlineKeyboardMarkup(row_width=2)
button1 = InlineKeyboardButton(text='Продолжить', callback_data='run1')
ikb.add(button1).add(home)

ikc = InlineKeyboardMarkup(row_width=2)
button1 = InlineKeyboardButton(text='Продолжить', callback_data='run2')
ikc.add(button1).add(home, back)

ikd = InlineKeyboardMarkup(row_width=2)
ikd.add(home, back1)