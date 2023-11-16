from create_bot import bot
from handlers import handler__commands
from telebot import types
from handlers import data_base
from telegram import InputMediaPhoto
from telegram.constants import ParseMode
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import os
from os import listdir


def open_photo(message, my_dir, photo_text):   # Функция, чтобы открывать фото в разделе "Пример работ"
    all_photos = []  # Создаем пустой список, куда потом будем сохранять фото из папок
    home=os.getcwd()  # на всякий случай получаем адрес текущего каталога.
    os.chdir(my_dir)  # если фото лежат в отдельной папке
    # ( не в той, где лежит запускаемый питон-файл), то нужно поменять рабочую директорию (указать папку с фото),
    # иначе абс. путь к файлам будет выдаваться неверный
    folder_dir = os.getcwd()  # сохраняем адрес новую (нужную нам) рабочую директорию в переменную
    dir_path = os.path.abspath(folder_dir)  # получаем абсол. путь директории с фото
    for images in os.listdir(dir_path):  # получаем список фото в указанной директории и перебираем его
        img_path = os.path.abspath(images)  # получаем абсол. путь для каждого фото
        current_image_file = open(img_path, 'rb')  # открываем фото
        all_photos.append(types.InputMediaPhoto(
            # добавляем открытые фото в список фото, создавая экземпляр класса  InputMediaPhoto
            media=current_image_file,
            parse_mode=ParseMode.HTML,
            caption=photo_text
        ))
    bot.send_media_group(message.chat.id, media=all_photos)
    os.chdir(home)


@bot.message_handler(content_types=['text'])

def info_message(message):
    global all_photos

    first_name = message.chat.first_name  # Определяем автоматически имя пользователя
    id_var= message.chat.id  # Получаем ид пользователя
    count_info = data_base.get_info(id_var)  # Получаем значения счетчиков из БД
    count_photo = data_base.get_photo(id_var)
    count_calculator = data_base.get_calculator(id_var)
    # ****** 1. ИНФО **********
    if message.text == '🔖Информация о нас':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_info_1 = types.KeyboardButton(text='☎️Телефон')
        key_info_2 = types.KeyboardButton(text='🔖О нас')
        key_info_3 = types.KeyboardButton(text='🛠 Технология монтажа забора')
        key_info_4 = types.KeyboardButton(text='❗️Технические требования  для монтажа забора')
        key_menu = types.KeyboardButton(text= '↩️ Вернуться в МЕНЮ')
        markup.add(key_info_1, key_info_2, key_info_3, key_info_4,  key_menu)
        bot.send_message(message.from_user.id, f'Мы с удовольствием расскажем о себе.'
                                               f'\n Выберите нужный пункт:!',
                         reply_markup=markup)

        count_info = count_info + 1  # При нажатии кнопки "Инфо" счетчик прибавляется на 1
        data_base.db_update_count(id_var, count_info,count_photo, count_calculator) # Новое значение счетчика записывается в БД
    elif message.text == '☎️Телефон':
        bot.send_message(message.from_user.id, f' Телефон: \n <code>{+78432666222}</code>', parse_mode='HTML')
    elif message.text == '🔖О нас':
        text_about_1 = ('\nЗаборМастер - бригада строителей-монтажников 👷🏻‍♂️👷🏻‍♂️👷🏻‍♂️'
                        '\nпод руководством \n'
                        '\nТАГИРОВА ИЛЬНУРА (самозанятый гражданин)😎\n'
                        '\nМы работаем в строительстве с 2010 года\n'
                       )
        text_about_2 = ( '\nЧто МЫ СТРОИМ:\n'
                        '\n✅ЗАБОРЫ - это наша страсть 🤩🤩🤩\n'
                        '\n✅дачные дома\n'
                        '\n✅веранды, беседки\n'
                        '\n✅кровля\n'
                        '\n✅хоз.блоки, сараи, дачные туалеты \n'
                         '\n✅ограждения (заборы, перила) из профильной трубы \n'
                         '\n✅ металлические сетки-решетки на окна "Антикошка" \n'
                        )
        text_about_3 = (' ❗На все работы ГАРАНТИЯ - 1 год❗\n' )

        text_about_4= ('\nВыезд, замер, консультация - \n'
                       '\nБЕСПЛАТНО 👍' )

        bot.send_message(message.from_user.id, text= text_about_1)
        bot.send_message(message.from_user.id, text=text_about_2)
        bot.send_message(message.from_user.id, text=text_about_3)
        bot.send_message(message.from_user.id, text=text_about_4)

    elif message.text == '🛠 Технология монтажа забора':
        text_tech_1 = ('Мы имеем огромный опыт в строительстве и '
                        '\nу нас есть надежная \n'
                        '\n💯 ТЕХНОЛОГИЯ МОНТАЖА ЗАБОРОВ 💯'
                       )
        text_tech_2 = ( '\n✅ МЕТАЛЛИЧЕСКИЙ каркас забора \n'
                        '\n✅ СВАРКА столбов и поперечин \n'
                         '\n✅СТОЛБЫ - труба d=57 мм, толщина стенки 3,5 мм'
                         '\n или квадратная труба 60х60мм\n'
                        '\n✅ ЛУНКИ для столбов бурятся мотобуром,'
                         '\nглубина - 0,6-1,0 м\n'
                         '\n✅Столбы БЕТОНИРУЮТСЯ\n'
                         '\n✅ каркас забора ОКРАШИВАЕТСЯ краской по металлу\n'
                         '\n✅ ПОПЕРЕЧНЫЕ ТРУБЫ - 2 шт для высоты до 2,5 м, '
                         '\n3 шт - при высоте забора 2,5-3 м\n'
                         '\n✅ Толщина ПРОФЛИСТА - от 0,4 мм\n'
                         '\n✅ КАЛИТКА изготавливается с врезным замком,'
                         '\nВОРОТА -  с засовом'
                         )
        bot.send_message(message.from_user.id, text= text_tech_1)
        bot.send_message(message.from_user.id, text=text_tech_2)

    elif message.text == '❗️Технические требования  для монтажа забора':
        text_trebovanie_1 = ('Что ДОЛЖНО БЫТЬ НА ВАШЕМ УЧАСТКЕ, '
                             '\nчтобы мы могли установить Вам самый лучший забор:\n')

        text_trebovanie_2 = ('1️⃣ ВОДА\n'
                        '\n2️⃣ ЭЛЕКТРИЧЕСТВО (можно от электрогенератора)\n'
                        '\n3️⃣ ГРАНИЦЫ участка должны быть четко определены.'
                             '\n  Пожалуйста,  заранее согласуйте  '
                             '\n  спорные вопросы с соседями '
                             '\n  и прочими важными инстанциями\n'
                        "\n4️⃣ ТЕМПЕРАТУРА ВЫШЕ 0 С': "
                             "\n  на холоде невозможно бурить землю,"
                             "\n  бетонировать столбы, окрашивать металл \n"
                        '\n5️⃣ ДЕМОНТАЖ старого ограждения, '
                             '\n  построек, садовых насаждений '
                             '\n  не входит в стоимость забора '
                             '\n  и обговаривается отдельно'
                        )

        bot.send_message(message.from_user.id, text=text_trebovanie_1)
        bot.send_message(message.from_user.id, text=text_trebovanie_2)

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

        count_calculator = count_calculator + 1 #При нажатии кнопки "Новый расчет" счетчик калькулятора прибавляется на 1
        data_base.db_update_count(id_var, count_info, count_photo, count_calculator)# Новое значение счетчика записывается в БД

    # ****** 2. ФОТО **********

    elif message.text == '⚒ Примеры работ':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_example_1 = types.KeyboardButton(text='✅ Заборы из профнастила')
        key_example_2 = types.KeyboardButton(text='✅ Заборы из сетки-рабицы')
        key_example_3 = types.KeyboardButton(text='✅ Заборы из штакетника')
        key_example_4 = types.KeyboardButton(text='✅ Хоз.постройки')
        key_example_5 = types.KeyboardButton(text='✅ Кровля')
        key_example_6 = types.KeyboardButton(text='✅ Другое')
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        markup.add(key_example_1, key_example_2,key_example_3,)
        markup.add( key_example_4, key_example_5,key_example_6)
        markup.add( key_menu)
        bot.send_message(message.from_user.id,
                                               f'\n Мы построили километры заборов, '
                                               f'\n и с гордостью покажем Вам фото!'
                                               f'\n       📸 📸 📸 📸 📸 📸    ',
                         reply_markup=markup)

        count_photo += 1
        data_base.db_update_count(id_var, count_info, count_photo, count_calculator)
    elif message.text == '✅ Заборы из профнастила':
        my_dir = '../Бот_ЗаборМастер/media/проф'
        photo_text="<b>Заборы из профнастила</b>"
        open_photo(message, my_dir,photo_text)
    elif message.text == '✅ Заборы из сетки-рабицы':
        my_dir = '../Бот_ЗаборМастер/media/раби'
        photo_text = "<b>Заборы из cетки-рабицы</b>"
        open_photo(message, my_dir, photo_text)
    elif message.text == '✅ Заборы из штакетника':
        my_dir = '../Бот_ЗаборМастер/media/штакет'
        photo_text = "<b>Заборы из штакетника</b>"
        open_photo(message, my_dir, photo_text)
    elif message.text == '✅ Хоз.постройки':
        my_dir = '../Бот_ЗаборМастер/media/хоз'
        photo_text = "<b>Хоз.постройки</b>"
        open_photo(message, my_dir, photo_text)
    elif message.text == '✅ Кровля':
        my_dir = '../Бот_ЗаборМастер/media/другое'
        photo_text = "<b>Кровля</b>"
        open_photo(message, my_dir, photo_text)
    elif message.text == '✅ Другое':
        my_dir = '../Бот_ЗаборМастер/media/другое' # Указываем папку, откуда взять фото
        photo_text = '<b>Ограждения из проф.трубы, "Антикошка" на окна</b>' # Указываем, как подписать альбом
        open_photo(message, my_dir, photo_text) # Вызываем функцию ждя открытия фото

    # ****** 3. РАССЧЕТ СТОИМОСТИ **********
    elif message.text == '💵Рассчитать стоимость забора':
        bot.send_message(message.from_user.id,
                         '\nЧтобы рассчитать забор из ❗ШТАКЕТНИКа ❗️, '
                         '\nа также различные ❗️ХОЗ.ПОCТРОЙКИ❗️, позвоните нам: ')
        bot.send_message(message.from_user.id,
                                               f'\n <code>☎️ {+78432666222}</code>', parse_mode='HTML')
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        key_menu = types.KeyboardButton(text='↩️ Вернуться в МЕНЮ')
        key_calculator = types.KeyboardButton(text='🧮️ Новый РАСЧЕТ стоимости')
        markup.add(key_menu, key_calculator)

        bot.send_message(message.from_user.id,
                         'Бот поможет рассчитать '
                         '\nзабор из ✅ ПРОФНАСТИЛА И РАБИЦЫ ✅\n'
                         '\nДля этого нужно ответить на несколько вопросов:',
                         reply_markup=markup)
        keyboard = types.InlineKeyboardMarkup()
        key_type_1 = types.InlineKeyboardButton(text='Профнастил: забор+ворота+калитка', callback_data='профнастил')
        key_type_2 = types.InlineKeyboardButton(text='Рабица: забор+ворота+калитка', callback_data='рабица')
        key_type_3 = types.InlineKeyboardButton(text='Ворота(без забора)', callback_data='ворота')
        key_type_4 = types.InlineKeyboardButton(text='Калитка(без забора)', callback_data='калитка')
        keyboard.add(key_type_1) # Прописываем каждый раз "keyboard.add" заново,
        # чтобы кнокпи добавлялись на новую строчку. Если прописать все вместе ( с 1 скобках), то они будут в 1 ряд
        keyboard.add(key_type_2)
        keyboard.add(key_type_3)
        keyboard.add(key_type_4)
        bot.send_message(message.from_user.id, f' 1️⃣ Выберите нужный объект: ', reply_markup=keyboard)

        count_calculator += 1 # При нажатии на кнопку увеличиваем счетчик на 1
        data_base.db_update_count(id_var, count_info, count_photo, count_calculator) # Записываем новое значение счетчика в БД

 # ****** БОЛТАЛКА **********
    elif message.text.lower() in ['старт',
                                   'start'
                                  ]:
        handler__commands.fun_start(message)


    elif message.text.lower() in ['привет',
                                   'здравствуйте',
                                  'здравствуй',
                                   'бонжур',
                                    'hi',
                                   'hello',
                                   'шалом',
                                   'прив']:

        bot.reply_to(message, f'{message.text}, {first_name}! \n')
        bot.send_message(message.chat.id, f' Выберите нужный пункт в меню:')
    elif message.text.lower() in ['салам',
                                   'ассаламалейкум',
                                  'сәлам']:
        bot.reply_to(message, f'Сәләм, дускаем {first_name}! Кнопкага бас')
    elif message.text.lower() in ['хеллер ничек?',
                                     'хеллер ничек',
                                     'хәлләр ничек',
                                     'каеф ничек?',
                                      'кәеф ничек?',
                                      'кәеф ничек',
                                      'каеф ничек',
                                     'хэллэр ничек?',
                                     'хэллэр ничек',
                                     ]:
        bot.reply_to(message, 'Ничаво. Кнопкага бас инде!')
    elif message.text.lower() in ['как дела',
                                     'как дела?',
                                     'how are you?',
                                     'how are you',
                                     'how do you do?',
                                     'how do you do',
                                     'как поживаешь?',
                                     'как жизнь?',
                                     'как поживаешь',
                                     'как жизнь']:
        bot.reply_to(message, 'Лучше всех. Нажми уже на кнопку, что ли?')
    elif message.text.lower() in ['пойдем погуляем?',
                                     'погуляем?',
                                     'пойдем гулять?',
                                  'пойдем погуляем',
                                  'погуляем',
                                  'пойдем гулять',
                                  ]:
        bot.reply_to(message, 'Извините, не могу, начальник не отпускает 😀😀😀')
    elif message.text.lower() in ['поболтаем?',
                                'давай поболтаем?',
                                'поговорим?',
                                'поболтаем',
                                'давай поболтаем',
                                'поговорим',
                                'давай еще поболтаем',
                                  ]:
        bot.reply_to(message, 'Извините, не могу, я на работе 😀😀😀')
    elif message.text.lower() in ['адрес',
                                     'где вы находитесь',
                                     'режим работы',
                                  'телефон',

                                  ]:
        bot.reply_to(message, 'Позвоните нам:')
        bot.reply_to(message, f'☎️ Телефон: \n <code>{+78432666222}</code>', parse_mode='HTML')
    elif message.text.lower() in ['чо?',
                                  'и чо?',
                                  'чо',
                                  'и чо',
                                        ]:
        bot.reply_to(message, 'да ничо')
    elif message.text.lower() in ["привет, как тебя зовут?",
                                  'давай познакомимся',
                                  'как тебя зовут',
                                  'как тебя зовут?',
                                  'давай познакомимся?'
                                        ]:
        bot.reply_to(message, 'Я ЧатБот, очень приятно!')
    elif message.text.lower() in ["ты ж робот",
                                      'ты же робот',
                                      'ты же робот?',
                                      'ты ж робот?',
                                      'ты робот?',
                                      'ты робот']:
        bot.reply_to(message, 'Да, но стараюсь все делать по-человечески 🦾🦾🦾')
    else:


        bot.reply_to(message, 'Я, конечно, очень умный ЧатБот, но мне трудно Вас понять'
                              '🤔. \n Если Вы не нашли ответ на свой вопрос, позвоните нам:')
        bot.reply_to(message, f'☎️ Телефон: \n <code>{+78432666222}</code>', parse_mode='HTML')
    print(f'count_info={count_info}, count_photo = {count_photo}, count_calculator = {count_calculator}')
    return id_var, count_info, count_photo, count_calculator

