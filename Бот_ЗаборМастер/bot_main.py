import telebot
from create_bot import bot
from handlers import handler__commands, handler__message_text, handler__call_data

import sqlite3
print('Бот запущен')


bot.polling(none_stop=True, interval=0)
# Запуск бота





