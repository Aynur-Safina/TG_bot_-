from create_bot import bot
from telebot import types
from fun_calculator import calculator, plus_vorota
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

material=''
h = 0
montage = ''
rab_karkas = ''
kalytka = ''
dlina_zab = 0
dlina_vor = 0

@bot.message_handler(content_types = ['text'])
def dlina_zabor(message):
    global dlina_zab
    dlina_zab = message.text
    if dlina_zab.isdigit():
        dlina_zab=int(dlina_zab)
        keyboard = types.InlineKeyboardMarkup()
        key_vorota_3 =types.InlineKeyboardButton(text='Ворота 3м', callback_data='vor_3')
        key_vorota_4 =types.InlineKeyboardButton(text='Ворота 4м', callback_data='vor_4')
        key_vorota_no =types.InlineKeyboardButton(text='❌БЕЗ ворот', callback_data='vor_NO')
        keyboard.add(key_vorota_3, key_vorota_4, key_vorota_no)
        bot.send_message(message.from_user.id, f'6️⃣ Выберите  ширину ворот ', reply_markup=keyboard)
    elif message.text == '↩️ Вернуться в МЕНЮ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_info = types.KeyboardButton(text='🔖Информация о нас')
        key_catalog = types.KeyboardButton(text='⚒ Примеры работ')
        key_calc = types.KeyboardButton(text='💵Рассчитать стоимость забора')
        markup.add(key_info, key_catalog, key_calc)
        bot.send_message(message.from_user.id, f' Выберите нужный пункт в меню:',
                         reply_markup=markup)
    elif message.text == '🧮️ Новый РАСЧЕТ стоимости':
        keyboard = types.InlineKeyboardMarkup()
        key_type_1 = types.InlineKeyboardButton(text='Профнастил: забор+ворота+калитка', callback_data='профнастил')
        key_type_2 = types.InlineKeyboardButton(text='Рабица: забор+ворота+калитка', callback_data='рабица')
        key_type_3 = types.InlineKeyboardButton(text='Ворота(без забора)', callback_data='ворота')
        key_type_4 = types.InlineKeyboardButton(text='Калитка(без забора)', callback_data='калитка')
        keyboard.add(key_type_1)  # Прописываем каждый раз "keyboard.add" заново,
        # чтобы кнокпи добавлялись на новую строчку. Если прописать все вместе ( с 1 скобках), то они будут в 1 ряд
        keyboard.add(key_type_2)
        keyboard.add(key_type_3)
        keyboard.add(key_type_4)
        bot.send_message(message.from_user.id, f' 1️⃣ Выберите нужный объект: ', reply_markup=keyboard)
    else:
        bot.send_message(message.from_user.id, 'Вводите цифрами')
        bot.register_next_step_handler(message, dlina_zabor)
    return dlina_zab

@bot.callback_query_handler (func=lambda call: True)
# Должна вызываться только 1 (ОДИН) раз за всю программу,
# в ней обрабатываются ВСЕ нажатия на кнопки, независимо от того,
# в какой последовательности идет. Пишется внизу, после всех функций
def callback_worker(call):
    global h, material, montage, kalytka, rab_karkas, dlina_vor

# 1. даем пользователю выбрать нужный объект. Если выбирает забор, то получаем параметры забора
    if call.data == 'профнастил':
        x = 'profnastil'
        print('profnastil')
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура (инлайновая, кнопки - в поле сообщений)
        key_okrash = types.InlineKeyboardButton(text='Профнастил ОКРАШЕННЫЙ', callback_data='проф_окраш')
        key_zink = types.InlineKeyboardButton(text='Профнастил ОЦИНКОВАННЫЙ', callback_data='проф_цинк')
        keyboard.add(key_okrash, key_zink)
        bot.send_message(call.message.chat.id, ' 2️⃣ Выберите вариант профнастила: ',
                         reply_markup=keyboard)
        keyboard = types.InlineKeyboardMarkup()  #   Чтобы вывести два сообщения с разными кнопками из 1 elif,
        # нужно для каждого набора кнопок и сообщения создавать отдельную клавиатуру, инчае сообщения и кнопки сольются
        key_1_5м = types.InlineKeyboardButton(text='1.5 м', callback_data='1.5')
        key_1_8м = types.InlineKeyboardButton(text='1.8 м', callback_data='1.8')
        key_2_0м = types.InlineKeyboardButton(text='2.0 м', callback_data='2.0')
        key_2_5м = types.InlineKeyboardButton(text='2.5 м', callback_data='2.5')
        key_3_0м = types.InlineKeyboardButton(text='3.0 м', callback_data='3.0')
        keyboard.add(key_1_5м, key_1_8м, key_2_0м,key_2_5м, key_3_0м)
        bot.send_message(call.message.chat.id, ' 3️⃣ Выберите высоту забора: ',
                         reply_markup=keyboard)
        keyboard = types.InlineKeyboardMarkup()  # Чтобы вывести два сообщения с разными кнопками из 1 elif,
        # нужно для каждого набора кнопок и сообщения создавать отдельную клавиатуру, инчае сообщения и кнопки сольются
        key_M_W = types.InlineKeyboardButton(text='Материал+работа', callback_data='M_W')
        key_W = types.InlineKeyboardButton(text='Только работа', callback_data='W')
        keyboard.add(key_M_W, key_W)

        bot.send_message(call.message.chat.id, ' 4️⃣ Выберите вариант монтажа: ',
                         reply_markup=keyboard)
        bot.send_message(call.message.chat.id, ' 5️⃣ Укажите длину глухого забора '
                                               '(без калитки и ворот) в метрах ')

        bot.register_next_step_handler(call.message, dlina_zabor)
    elif call.data == 'рабица':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура (инлайновая, кнопки - в поле сообщений)
        key_bez_pvh = types.InlineKeyboardButton(text='Рабица ОЦИНКОВАННАЯ', callback_data='раб_без_пвх')
        key_pvh = types.InlineKeyboardButton(text='Рабица с ПВХ-покрытием', callback_data='раб_пвх')
        keyboard.add(key_bez_pvh, key_pvh)
        bot.send_message(call.message.chat.id, ' 2️⃣ Выберите сетку-рабицу: ',
                         reply_markup=keyboard)

        keyboard = types.InlineKeyboardMarkup()  # Чтобы вывести два сообщения с разными кнопками из 1 elif,
        # нужно для каждого набора кнопок и сообщения создавать отдельную клавиатуру, инчае сообщения и кнопки сольются
        key_1_5м = types.InlineKeyboardButton(text='1.5 м', callback_data='1.5')
        key_1_8м = types.InlineKeyboardButton(text='1.8 м', callback_data='1.8')
        key_2_0м = types.InlineKeyboardButton(text='2.0 м', callback_data='2.0')
        keyboard.add(key_1_5м, key_1_8м, key_2_0м)
        bot.send_message(call.message.chat.id, ' 3️⃣ Выберите высоту забора: ',
                         reply_markup=keyboard)

        keyboard = types.InlineKeyboardMarkup()
        key_karkas = types.InlineKeyboardButton(text='Сетка С КАРКАСОМ', callback_data='karkas')
        key_bez_karkasa = types.InlineKeyboardButton(text='БЕЗ каркаса', callback_data='bez_karkasa')
        keyboard.add(key_karkas, key_bez_karkasa)
        bot.send_message(call.message.chat.id, ' Выберите модель забора: ',
                         reply_markup=keyboard)

        keyboard = types.InlineKeyboardMarkup()  # Чтобы вывести два сообщения с разными кнопками из 1 elif,
        # нужно для каждого набора кнопок и сообщения создавать отдельную клавиатуру, инчае сообщения и кнопки сольются
        key_M_W = types.InlineKeyboardButton(text='Материал+работа', callback_data='M_W')
        key_W = types.InlineKeyboardButton(text='Только работа', callback_data='W')
        keyboard.add(key_M_W, key_W)
        bot.send_message(call.message.chat.id, ' 4️⃣ Выберите вариант монтажа: ',
                         reply_markup=keyboard)


        bot.send_message(call.message.chat.id, ' 5️⃣Укажите длину глухого забора '
                                               '(без калитки и ворот) в метрах ')

        bot.register_next_step_handler(call.message, dlina_zabor)
# 2. даем пользователю выбрать нужный объект. Если выбирает ворота/калитку без забора, то получаем параметры ворот и калитки
    elif call.data == 'ворота':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура (инлайновая, кнопки - в поле сообщений)
        key_vorota_3m_prof = types.InlineKeyboardButton(text='Профнастил 3 м', callback_data='3м_проф')
        key_vorota_4m_prof = types.InlineKeyboardButton(text='Профнастил 4 м', callback_data='4м_проф')
        key_vorota_3m_rabiza = types.InlineKeyboardButton(text='Рабица 3 м', callback_data='3м_рабица')
        key_vorota_4m_rabiza = types.InlineKeyboardButton(text='Рабица 4 м', callback_data='4м_рабица')
        keyboard.add(key_vorota_3m_prof, key_vorota_3m_rabiza )
        keyboard.add(key_vorota_4m_prof, key_vorota_4m_rabiza)
        bot.send_message(call.message.chat.id, ' 2️⃣ Выберите материал и длину ворот: ',
                         reply_markup=keyboard)
    elif call.data == 'калитка':
        keyboard = types.InlineKeyboardMarkup()  # наша клавиатура (инлайновая, кнопки - в поле сообщений)
        key_kalytka_prof = types.InlineKeyboardButton(text='Калитка из профнастила', callback_data='kalytka_prof')
        key_kalytka_rabiza = types.InlineKeyboardButton(text='Калитка из рабицы', callback_data='kalytka_rabiza')
        keyboard.add(key_kalytka_prof, key_kalytka_rabiza)
        bot.send_message(call.message.chat.id, ' 2️⃣ Выберите материал калитки: ',
                         reply_markup=keyboard)

    elif call.data == '3м_проф':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='🧮️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu, key_calculator)

        bot.send_message(call.message.chat.id, '✔️ Ворота из ПРОФНАСТИЛА,'
                                               '\n✔️ ширина 3 м '
                                               '\n✔️ монтаж\n'
                                               '\n💵 29 000 руб: ',
                         reply_markup=markup)
        bot.send_message(call.from_user.id,
                         f'          Телефон: '
                         f'\n <code>☎️ {+78432666222}</code>',
                         parse_mode='HTML')

    elif call.data == '4м_проф':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='🧮️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu, key_calculator)

        bot.send_message(call.message.chat.id, '✔️ Ворота из ПРОФНАСТИЛА,'
                                               '\n✔️ ширина 4 м + '
                                               '\n✔️ монтаж\n '
                                               '\n💵 34 000 руб: ', reply_markup=markup)
        bot.send_message(call.from_user.id,
                          f'          Телефон: '
                         f'\n <code>☎️ {+78432666222}</code>',
                         parse_mode='HTML')

    elif call.data == '3м_рабица':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='🧮️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu, key_calculator)
        bot.send_message(call.message.chat.id, '✔️ Ворота из РАБИЦЫ, '
                                               '\n✔️ширина 3 м  '
                                               '\n✔️ монтаж\n'
                                               '\n💵 23 000 руб: ',
                         reply_markup=markup)
        bot.send_message(call.from_user.id,
                         f'          Телефон: '
                         f'\n <code>☎️ {+78432666222}</code>',
                         parse_mode='HTML')
    elif call.data == '4м_рабица':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='🧮️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu, key_calculator)
        bot.send_message(call.message.chat.id, '✔️ Ворота из РАБИЦЫ,'
                                               '\n✔️ ширина 4 м '
                                               '\n✔️монтаж\n'
                                               '\n💵 26 000 руб: ',
                         reply_markup=markup)
        bot.send_message(call.from_user.id,
                          f'          Телефон: '
                         f'\n <code>☎️ {+78432666222}</code>',
                         parse_mode='HTML')
    elif call.data == 'kalytka_prof':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='🧮️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu, key_calculator)
        bot.send_message(call.message.chat.id, '✔️ Калитка из ПРОФНАСТИЛА,'
                                               '\n✔️ ширина 1 м'
                                               '\n✔️ врезной замок'
                                               '\n✔️ монтаж\n'
                                               '\n💵 19 000 руб: ',
                         reply_markup=markup)
        bot.send_message(call.from_user.id,
                          f'          Телефон: '
                         f'\n <code>☎️ {+78432666222}</code>',
                         parse_mode='HTML')
    elif call.data == 'kalytka_rabiza':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='🧮️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu, key_calculator)
        bot.send_message(call.message.chat.id, ' ✔️ Калитка из РАБИЦЫ '
                                               '\n✔️ ширина 1 м'
                                               '\n✔️ врезной замок '
                                               '\n✔️ монтаж\n'
                                               '\n 💵 18 000 руб: ',
                         reply_markup=markup)
        bot.send_message(call.from_user.id,
                         f'          Телефон: '
                         f'\n <code>☎️ {+78432666222}</code>',
                         parse_mode='HTML')

# 3. Если выбрал забор, то записываем выбранные параметры в переменные
    elif call.data == 'проф_окраш':
        material = 'профнастил окрашенный'
        return material
    elif call.data == 'проф_цинк':
        material = 'профнастил оцинкованный'
        return material
    elif call.data == '1.5':
        h = 1.5
        return h
    elif call.data == '1.8':
        h = 1.8
        return h
    elif call.data == '2.0':
        h = 2.0
        return h
    elif call.data == '2.5':
        h = 2.5
        return h
    elif call.data == '3.0':
        h = 3.0
        return h
    elif call.data == 'M_W':
        montage = 'материалы+работа'
        return montage
    elif call.data == 'W':
        montage = 'только работа'
        return montage
    elif call.data == 'раб_без_пвх':
        material = 'рабица оцинкованная'
        return material
    elif call.data == 'раб_пвх':
        material = 'рабица c ПВХ-покрытием'
        return material
    elif call.data == 'karkas':
        rab_karkas = 'сетка в каркасе'
        return rab_karkas
    elif call.data == 'bez_karkasa':
        rab_karkas = 'сетка без каркаса'
        return rab_karkas
    elif call.data == 'vor_3':
        dlina_vor = 3
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='✅ Да', callback_data='kalytka_yes')  # кнопка да
        key_no = types.InlineKeyboardButton(text='❌ Нет', callback_data='kalytka_no')  # кнопка нет
        keyboard.add(key_yes, key_no )
        bot.send_message(call.message.chat.id, f'7️⃣ Вам нужна калитка? ', reply_markup=keyboard)
        return dlina_vor
    elif call.data =='vor_4':
        dlina_vor = 4
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='✅ Да', callback_data='kalytka_yes')  # кнопка да
        key_no = types.InlineKeyboardButton(text='❌ Нет', callback_data='kalytka_no')  # кнопка нет
        keyboard.add(key_yes, key_no)
        bot.send_message(call.message.chat.id, f'7️⃣ Вам нужна калитка? ', reply_markup=keyboard)
        return dlina_vor
    elif call.data == 'vor_NO':
        dlina_vor =0
        keyboard = types.InlineKeyboardMarkup()
        key_yes = types.InlineKeyboardButton(text='✅ Да', callback_data='kalytka_yes')  # кнопка да
        key_no = types.InlineKeyboardButton(text='❌ Нет', callback_data='kalytka_no')  # кнопка нет
        keyboard.add(key_yes, key_no)
        bot.send_message(call.message.chat.id, f'7️⃣ Вам нужна калитка? ', reply_markup=keyboard)
        return dlina_vor
    elif call.data == 'kalytka_yes':

        kalytka = 'с калиткой'
        bot.send_message(call.message.chat.id,
                         f'Параметры Вашего забора: '
                         f'\n✔️ {material},'
                         f'\n✔️ высота {h} м.,' f'{rab_karkas}'
                         f'\n✔️ {montage},'
                         f'\n✔️ {kalytka}, '
                         f'\n✔️ длина забора {dlina_zab} м.,'
                         f'\n✔️ ширина ворот {dlina_vor} м. '
                         f'\n✔️ доставка в радиусе 30 км от Казани')
# 4. После записи всех параметров, вызывем функөию calculator,
        # в нее передаем  все записанные переменные,
        # Результат, полученный от calculator, записываем в перемнную var и выводим var в сообщение.

        var=calculator(h, material, montage, kalytka, rab_karkas, dlina_vor, dlina_zab)
        var_2 =  plus_vorota(h, material, montage, kalytka, rab_karkas, dlina_vor, dlina_zab, var)
        bot.send_message(call.message.chat.id, text=f'  Стоимость забора: '
                                               f'\n💵 {var_2} рублей 💵')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='↩️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu)
        markup.add(key_calculator)
        bot.send_message(call.message.chat.id,
                         text=f'Для подтверждения стоимости забора, '
                              f'\nпозвоните нам: '
                              f'\n <code>☎️ {+78432666222}</code>',
                         parse_mode='HTML')
        return kalytka

    elif call.data == 'kalytka_no':
        kalytka = 'без калитки'
        bot.send_message(call.message.chat.id,
                          f'Параметры Вашего забора: '
                         f'\n✔️ {material},'
                         f'\n✔️ высота {h} м.,' f'{rab_karkas}'
                         f'\n✔️ {montage},'
                         f'\n✔️ {kalytka}, '
                         f'\n✔️ длина забора {dlina_zab} м.,'
                         f'\n✔️ ширина ворот {dlina_vor} м. '
                         f'\n✔️ доставка в радиусе 30 км от Казани')

        var = calculator(h, material, montage, kalytka, rab_karkas, dlina_vor, dlina_zab)
        var_2 = plus_vorota(h, material, montage, kalytka, rab_karkas, dlina_vor, dlina_zab, var)
        bot.send_message(call.message.chat.id, text=f' Стоимость забора: '
                                                    f'\n💵 {var_2} рублей 💵')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='↩️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu)
        markup.add(key_calculator)
        bot.send_message(call.message.chat.id,
                         text=f'Для подтверждения стоимости забора, '
                              f'\nпозвоните нам: '
                              f'\n <code> ☎️ {+78432666222}</code>',
                         parse_mode='HTML')
    return kalytka








