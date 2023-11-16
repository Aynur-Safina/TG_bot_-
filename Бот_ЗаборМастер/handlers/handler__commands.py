from create_bot import bot
from telebot import types
from handlers import data_base

@bot.message_handler(commands=['start'])
def fun_start(message):
    first_name = message.chat.first_name  # Определяем автоматически имя пользователя
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    key_info = types.KeyboardButton(text='🔖Информация о нас')
    key_catalog = types.KeyboardButton(text='⚒ Примеры работ')
    key_calc = types.KeyboardButton(text='💵Рассчитать стоимость забора')
    markup.add(key_info, key_catalog, key_calc)
    data_base.db_create()
    data_base.db_insert_data(message)
    bot.send_message(message.chat.id, f'Здравствуйте, {first_name}!\n Выберите нужный пункт в меню:',
                     reply_markup=markup)
    return message
