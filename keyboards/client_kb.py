from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

#Общие
home = InlineKeyboardButton(text='С начала 🔝', callback_data='start')
back = InlineKeyboardButton(text='Назад 🔙', callback_data='back')
back1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back1')
back_sms = InlineKeyboardButton(text='Назад 🔙', callback_data='back_sms')
exit_serv_pc = InlineKeyboardButton(text='Продолжить ✅', callback_data='exit')
back_pc = InlineKeyboardButton(text='Назад 🔙', callback_data='back_pc')
exit_sms = InlineKeyboardButton(text='Продолжить ✅', callback_data='exit_sms')
back_bank = InlineKeyboardButton(text='Назад 🔙', callback_data='back_bank')
back_reg = InlineKeyboardButton(text='Назад 🔙', callback_data='back_reg')
exit_reg = InlineKeyboardButton(text='Продолжить ✅', callback_data='exit_reg')
back_zenno1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zenno1')

#Ссылки
url_rdp_win = 'https://apps.microsoft.com/store/detail/%D1%83%D0%B4%D0%B0%D0%BB%D0%B5%D0%BD%D0%BD%D1%8B%D0%B9-%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9-\
              %D1%81%D1%82%D0%BE%D0%BB-%D0%BC%D0%B0%D0%B9%D0%BA%D1%80%D0%BE%D1%81%D0%BE%D1%84%D1%82/9WZDNCRFJ3PS?hl=ru-ru&gl=ru&activetab=pivot%3Aoverviewtab'
url_rdp_mac = 'https://apps.apple.com/ru/app/microsoft-remote-desktop/id1295203466?mt=12'
url_modulbank = 'https://modulbank.ru/marketplace/?utm_source=agentnet&utm_medium=partner&utm_campaign=RKO_ag-212102486441'
url_json = 'https://zennolab.atlassian.net/wiki/spaces/RU/pages/735576090/Google+PM'

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
ikc.add(bpc).add(back, home)

#ПК
ikpc = InlineKeyboardMarkup(row_width=2)
bserver = InlineKeyboardButton(text='Выбрать сервер', callback_data='server')
ikpc.add(exit_serv_pc).add(bserver).add(back1, home)

#Сервера
ikserver = InlineKeyboardMarkup(row_width=2)
serv1 = InlineKeyboardButton(text='Selectel', url='https://selectel.ru/?ref_code=e2d2d054d4')
serv2 = InlineKeyboardButton(text='Serfstack', url='https://client.serfstack.com/aff.php?aff=35')
next_serv = InlineKeyboardButton(text='Продолжить ✅', callback_data='run_serv')
ikserver.add(serv1, serv2).add(next_serv).add(back_pc, home)

#RDP
ikserver1 = InlineKeyboardMarkup(row_width=2)
serv1_1 = InlineKeyboardButton(text='Скачать для Windows', url=url_rdp_win)
serv1_2 = InlineKeyboardButton(text='Скачать для Mac', url=url_rdp_mac)
back2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back2')
ikserver1.add(serv1_1, serv1_2).add(exit_serv_pc).add(back2, home)

#######################Регистрируем СМС сервисы####################################
iksms = InlineKeyboardMarkup(row_width=2)
zadarma = InlineKeyboardButton(text='Zadarma', callback_data='run_zad')
plusofon = InlineKeyboardButton(text='Плюсофон', callback_data='run_plus')
skip_sms = InlineKeyboardButton(text='Пропустить', callback_data='skip_sms')
#back_server = InlineKeyboardButton(text='Назад 🔙', callback_data='back_server')
iksms.add(zadarma).add(skip_sms).add(back_pc, home)


#Задарма
ikzad = InlineKeyboardMarkup(row_width=2)
zad_vid1 = InlineKeyboardButton(text='Видео 1 часть', url='https://youtu.be/DWcpuXONPho')
zad_vid2 = InlineKeyboardButton(text='Видео 2 часть', url='https://youtu.be/Cnn88_iVUqc')
zad_url = InlineKeyboardButton(text='Регистрация', url='https://zadarma.com/ru/?ref=dcf761984bc63ea302d80c33bd61361f')
next_zad = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zad')
ikzad.add(zad_vid1, zad_vid2).add(zad_url).add(next_zad).add(back_sms, home)

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
back_zad7 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zad7')
ikzad7.add(exit_sms).add(back_zad7, home)


#Плюсофон
ikplus = InlineKeyboardMarkup(row_width=2)
plus_url = InlineKeyboardButton(text='Регистрация', url='https://new-portal.plusofon.ru/signup-user?promocode=qekv')
next_plus = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus')
ikplus.add(plus_url).add(next_plus).add(back_sms, home)

ikplus1 = InlineKeyboardMarkup(row_width=2)
next_plus1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus1')
back_plus1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus1')
ikplus1.add(next_plus1).add(back_plus1, home)

ikplus2 = InlineKeyboardMarkup(row_width=2)
next_plus2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus2')
back_plus2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus2')
ikplus2.add(next_plus2).add(back_plus2, home)

ikplus3 = InlineKeyboardMarkup(row_width=2)
next_plus3 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus3')
back_plus3 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus3')
ikplus3.add(next_plus3).add(back_plus3, home)

ikplus4 = InlineKeyboardMarkup(row_width=2)
next_plus4 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus4')
back_plus4 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus4')
ikplus4.add(next_plus4).add(back_plus4, home)

ikplus5 = InlineKeyboardMarkup(row_width=2)
next_plus5 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus5')
back_plus5 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus5')
ikplus5.add(next_plus5).add(back_plus5, home)

ikplus6 = InlineKeyboardMarkup(row_width=2)
next_plus6 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus6')
back_plus6 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus6')
ikplus6.add(next_plus6).add(back_plus6, home)

ikplus7 = InlineKeyboardMarkup(row_width=2)
next_plus7 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus7')
back_plus7 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus7')
ikplus7.add(next_plus7).add(back_plus7, home)

ikplus8 = InlineKeyboardMarkup(row_width=2)
next_plus8 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus8')
back_plus8 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus8')
ikplus8.add(next_plus8).add(back_plus8, home)

ikplus9 = InlineKeyboardMarkup(row_width=2)
next_plus9 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus9')
back_plus9 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus9')
ikplus9.add(next_plus9).add(back_plus9, home)

ikplus10 = InlineKeyboardMarkup(row_width=2)
next_plus10 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus10')
back_plus10 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus10')
ikplus10.add(next_plus10).add(back_plus10, home)

ikplus11 = InlineKeyboardMarkup(row_width=2)
next_plus11 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus11')
back_plus11 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus11')
ikplus11.add(next_plus11).add(back_plus11, home)

ikplus12 = InlineKeyboardMarkup(row_width=2)
next_plus12 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus12')
back_plus12 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus12')
ikplus12.add(next_plus12).add(back_plus12, home)

ikplus13 = InlineKeyboardMarkup(row_width=2)
next_plus13 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus13')
back_plus13 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus13')
ikplus13.add(next_plus13).add(back_plus13, home)

ikplus14 = InlineKeyboardMarkup(row_width=2)
next_plus14 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_plus14')
back_plus14 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus14')
ikplus14.add(next_plus14).add(back_plus14, home)

ikplus15 = InlineKeyboardMarkup(row_width=2)
back_plus15 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_plus15')
ikplus15.add(exit_sms).add(back_plus15, home)


###################################Банки######################################
ikbank = InlineKeyboardMarkup(row_width=2)
back_in_sms = InlineKeyboardButton(text='Назад 🔙', callback_data='back_in_sms')
qiwi = InlineKeyboardButton(text='QIWI-кошелек', callback_data='run_qiwi')
modulbank = InlineKeyboardButton(text='Модульбанк', callback_data='run_modulbank')
skip_bank = InlineKeyboardButton(text='Пропустить', callback_data='skip_bank')
ikbank.add(qiwi, modulbank).add(skip_bank).add(back_in_sms, home)


#QIWI
ikqiwi = InlineKeyboardMarkup(row_width=2)
next_qiwi = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_qiwi')
qiwi_url = InlineKeyboardButton(text='Регистрация', url='https://qiwi.com/')
qiwi_video = InlineKeyboardButton(text='Видеоинструкция', url='https://youtu.be/dqrYg1vilxE')
ikqiwi.add(qiwi_url, qiwi_video).add(next_qiwi).add(back_bank, home)

ikqiwi1 = InlineKeyboardMarkup(row_width=2)
next_qiwi1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_qiwi1')
qiwi_url1 = InlineKeyboardButton(text='Zadarma', url='https://zadarma.com/ru/')
back_qiwi1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_qiwi1')
ikqiwi1.add(qiwi_url1).add(next_qiwi1).add(back_qiwi1, home)

ikqiwi2 = InlineKeyboardMarkup(row_width=2)
next_qiwi2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_qiwi2')
qiwi_url2 = InlineKeyboardButton(text='Основной', url='https://qiwi.com/support/information/subject5/identifikatsiya-v-qiwi-koshelke')
qiwi_url2_1 = InlineKeyboardButton(text='Профессиональный', url='https://qiwi.com/settings/identification/full-ru#ru')
back_qiwi2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_qiwi2')
ikqiwi2.add(qiwi_url2, qiwi_url2_1).add(next_qiwi2).add(back_qiwi2, home)

ikqiwi3 = InlineKeyboardMarkup(row_width=2)
next_qiwi3 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_qiwi3')
back_qiwi3 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_qiwi3')
ikqiwi3.add(next_qiwi3).add(back_qiwi3, home)

ikqiwi4 = InlineKeyboardMarkup(row_width=2)
next_qiwi4 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_qiwi4')
back_qiwi4 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_qiwi4')
ikqiwi4.add(next_qiwi4).add(back_qiwi4, home)

ikqiwi5 = InlineKeyboardMarkup(row_width=2)
next_qiwi5 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_qiwi5')
back_qiwi5 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_qiwi5')
ikqiwi5.add(next_qiwi5).add(back_qiwi5, home)

ikqiwi6 = InlineKeyboardMarkup(row_width=2)
next_qiwi6 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_qiwi6')
back_qiwi6 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_qiwi6')
ikqiwi6.add(next_qiwi6).add(back_qiwi6, home)

ikqiwi7 = InlineKeyboardMarkup(row_width=2)
next_qiwi7 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_qiwi7')
back_qiwi7 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_qiwi7')
ikqiwi7.add(next_qiwi7).add(back_qiwi7, home)


#Модульбанк
ikmodul = InlineKeyboardMarkup(row_width=2)
next_modul = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_modul')
modul_url = InlineKeyboardButton(text='Оставить заявку', url=url_modulbank)
back_modul = InlineKeyboardButton(text='Назад 🔙', callback_data='back_modul')
ikmodul.add(modul_url).add(next_modul).add(back_modul, home)

ikmodul1 = InlineKeyboardMarkup(row_width=2)
modul_url1 = InlineKeyboardButton(text='Zadarma', url='https://my.zadarma.com/')
next_modul1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_modul1')
back_modul1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_modul1')
ikmodul1.add(modul_url1).add(next_modul1).add(back_modul1, home)


############################Регистрации аккаунтов############################
ikreg = InlineKeyboardMarkup(row_width=2)
skip_reg = InlineKeyboardButton(text='Пропустить', callback_data='skip_reg')
onlinesim = InlineKeyboardButton(text='OnlineSIM', callback_data='onlinesim')
activate = InlineKeyboardButton(text='SMS-activate', callback_data='activate')
vak_sms = InlineKeyboardButton(text='Vak-sms', callback_data='vak_sms')
back_in_bank = InlineKeyboardButton(text='Назад 🔙', callback_data='back_in_bank')
ikreg.add(onlinesim, activate, vak_sms).add(skip_reg).add(back_in_bank, home)


#OnlineSIM
ikosim = InlineKeyboardMarkup(row_width=2)
next_osim = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_osim')
osim_url = InlineKeyboardButton(text='Регистрация', url='https://onlinesim.io/?ref=3245082')
osim_video = InlineKeyboardButton(text='Видеоинструкция', url='https://youtu.be/WmaBcA1oTkE')
ikosim.add(osim_url, osim_video).add(next_osim).add(back_reg, home)

ikosim1 = InlineKeyboardMarkup(row_width=2)
next_osi1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_osim1')
back_osim1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_osim1')
ikosim1.add(next_osi1).add(back_osim1, home)

ikosim2 = InlineKeyboardMarkup(row_width=2)
next_osi2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_osim2')
back_osim2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_osim2')
ikosim2.add(next_osi2).add(back_osim2, home)

ikosim3 = InlineKeyboardMarkup(row_width=2)
next_osi3 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_osim3')
back_osim3 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_osim3')
ikosim3.add(next_osi3).add(back_osim3, home)

ikosim4 = InlineKeyboardMarkup(row_width=2)
back_osim4 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_osim4')
ikosim4.add(exit_reg).add(back_osim4, home)


#SMS-activate
ikactiv = InlineKeyboardMarkup(row_width=2)
next_activ = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_activ')
activ_url = InlineKeyboardButton(text='Регистрация', url='https://sms-activate.org/?ref=1965570')
activ_video =InlineKeyboardButton(text='Видеоинструкция', url='https://youtu.be/IClOpurIEAw')
ikactiv.add(activ_url, activ_video).add(next_activ).add(back_reg, home)

ikactiv1 = InlineKeyboardMarkup(row_width=2)
next_activ1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_activ1')
back_activ1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_activ1')
ikactiv1.add(next_activ1).add(back_activ1, home)

ikactiv2 = InlineKeyboardMarkup(row_width=2)
next_activ2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_activ2')
back_activ2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_activ2')
ikactiv2.add(next_activ2).add(back_activ2, home)

ikactiv3 = InlineKeyboardMarkup(row_width=2)
back_activ3 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_activ3')
ikactiv3.add(exit_reg).add(back_activ3, home)


#Vak-sms
ikvak = InlineKeyboardMarkup(row_width=2)
next_vak = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_vak')
vak_url = InlineKeyboardButton(text='Регистрация', url='https://vak-sms.com/311621a1-6e74-4c16-bdd3-1f154349f311')
vak_video = InlineKeyboardButton(text='Видеоинструкция', url='https://youtu.be/ZuyU8zM6BF0')
ikvak.add(vak_url, vak_video).add(next_vak).add(back_reg, home)

ikvak1 = InlineKeyboardMarkup(row_width=2)
next_vak1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_vak1')
back_vak1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_vak1')
ikvak1.add(next_vak1).add(back_vak1, home)

ikvak2 = InlineKeyboardMarkup(row_width=2)
next_vak2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_vak2')
back_vak2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_vak2')
ikvak2.add(next_vak2).add(back_vak2, home)

ikvak3 = InlineKeyboardMarkup(row_width=2)
back_vak3 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_vak3')
ikvak3.add(exit_reg).add(back_vak3, home)


############################Аренда и установка прокси############################
ikproxy = InlineKeyboardMarkup(row_width=2)
next_proxy =InlineKeyboardButton(text='Продолжить ✅', callback_data='next_proxy')
proxy_url = InlineKeyboardButton(text='Наш прокси', callback_data='https://t.me/MDA_teh')
proxy_url_1 = InlineKeyboardButton(text='Proxy Promo', callback_data='https://proxy.promo')
back_in_reg = InlineKeyboardButton(text='Назад 🔙', callback_data='back_in_reg')
skip_proxy = InlineKeyboardButton(text='Пропустить', callback_data='skip_proxy')
ikproxy.add(proxy_url, proxy_url_1).add(next_proxy).add(skip_proxy).add(back_in_reg, home)

ikproxy1 = InlineKeyboardMarkup(row_width=2)
next_proxy1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_proxy1')
back_proxy1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_proxy1')
ikproxy1.add(next_proxy1).add(back_proxy1, home)

ikproxy2 = InlineKeyboardMarkup(row_width=2)
next_proxy2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_proxy2')
back_proxy2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_proxy2')
ikproxy2.add(next_proxy2).add(back_proxy2, home)


################################ZennoLab#######################################
ikzenno = InlineKeyboardMarkup(row_width=2)
next_zenno = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zenno')
skip_zenno = InlineKeyboardButton(text='Пропустить', callback_data='skip_zenno')
zenno_url = InlineKeyboardButton(text='Регистрация', url='https://userarea.zennolab.com/lk/Registration.aspx')
zenno_video = InlineKeyboardButton(text='Видеоинструкция', callback_data='zenno_video')
back_zenno = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zenno')
ikzenno.add(zenno_url, zenno_video).add(next_zenno).add(skip_zenno).add(back_zenno, home)

#Видеоинструкция
ikzenno_video = InlineKeyboardMarkup(row_width=2)
zenno_video1 = InlineKeyboardButton(text='1 Часть', url='https://youtu.be/4zJFvLBSgpg')
zenno_video2 = InlineKeyboardButton(text='2 Часть', url='https://youtu.be/MCZcsEvRNNg')
zenno_video3 = InlineKeyboardButton(text='3 Часть', url='https://youtu.be/y7fSaZ-uXI8')
ikzenno_video.add(zenno_video1, zenno_video2, zenno_video3).add(back_zenno1, home)

ikzenno1 = InlineKeyboardMarkup(row_width=2)
next_zenno1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zenno1')
ikzenno1.add(next_zenno1).add(back_zenno1, home)

ikzenno2 = InlineKeyboardMarkup(row_width=2)
next_zenno2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zenno2')
zenno_url2 = InlineKeyboardButton(text='Скачать', url='https://account.zennolab.com/personal-area-main/my-products')
back_zenno2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zenno2')
ikzenno2.add(zenno_url2).add(next_zenno2).add(back_zenno2, home)

ikzenno3 = InlineKeyboardMarkup(row_width=2)
next_zenno3 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zenno3')
back_zenno3 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zenno3')
ikzenno3.add(next_zenno3).add(back_zenno3, home)

ikzenno4 = InlineKeyboardMarkup(row_width=2)
next_zenno4 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_zenno4')
zenno_url4 = InlineKeyboardButton(text='Оборудование', url='https://userarea.zennolab.com/lk/userarea/UserAddHardware.aspx')
back_zenno4 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_zenno4')
ikzenno4.add(zenno_url4).add(next_zenno4).add(back_zenno4, home)


##########################Разгадывание капчи###################################
ikcaptcha = InlineKeyboardMarkup(row_width=2)
next_captcha = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_captcha')
captha_url = InlineKeyboardButton(text='Регистрация', url='https://rucaptcha.com/?from=13800235')
captcha_video = InlineKeyboardButton(text='Видеоинструкция', url='https://youtu.be/3gmJPnUCYCo')
back_in_zenno = InlineKeyboardButton(text='Назад 🔙', callback_data='back_in_zenno')
skip_captcha = InlineKeyboardButton(text='Пропустить', callback_data='skip_captcha')
ikcaptcha.add(captha_url, captcha_video).add(next_captcha).add(skip_captcha).add(back_in_zenno, home)

ikcaptcha1 = InlineKeyboardMarkup(row_width=2)
next_captcha1 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_captcha1')
back_captcha1 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_captcha1')
ikcaptcha1.add(next_captcha1).add(back_captcha1, home)

ikcaptcha2 = InlineKeyboardMarkup(row_width=2)
next_captcha2 = InlineKeyboardButton(text='Продолжить ✅', callback_data='next_captcha2')
back_captcha2 = InlineKeyboardButton(text='Назад 🔙', callback_data='back_captcha2')
ikcaptcha2.add(next_captcha2).add(back_captcha2, home)


############################Google JSON#######################################
ikjson = InlineKeyboardMarkup(row_width=2)
json_url = InlineKeyboardButton(text='Регистрация почты', url='https://accounts.google.com/')
json_video = InlineKeyboardButton(text='Видеоинструкция', url='https://youtu.be/6EZBlu8OHoE')
json_text = InlineKeyboardButton(text='Инструкция от зенно', url=url_json)
back_in_captcha = InlineKeyboardButton(text='Назад 🔙', callback_data='back_in_captcha')
ikjson.add(json_url).add(json_video, json_text).add(back_in_captcha, home)

ikjson1 = InlineKeyboardMarkup(row_width=2)
