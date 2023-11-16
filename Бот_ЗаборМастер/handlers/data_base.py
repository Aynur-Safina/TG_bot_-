import sqlite3

def db_create():
    base = sqlite3.connect('ЗаборМастер_Бот.db') # Создаем таблицу
    cur = base.cursor()#
    cur.execute("""CREATE TABLE IF NOT EXISTS data_user 
                (user_id INT PRIMARY KEY, 
                first_name_user TEXT, 
                last_name_user TEXT, 
                username_user TEXT,
                info INT,
                photo INT,
                calculator INT)""")
    base.commit()


def db_insert_data(message):
    count_info = 0
    count_photo = 0
    count_calculator = 0
    base = sqlite3.connect('ЗаборМастер_Бот.db') # В каждой функции вызываем таблицу заново,
    # потому что вызов таблицы будет только один раз в данном файле,
    # а вызов функции будет из другого файла(handlers__message_text), выдаст ошибку
    cur = base.cursor()
    first_name = message.from_user.first_name  # Определяем автоматически имя пользователя
    last_name = message.from_user.last_name
    username = message.from_user.username
    id_var = message.chat.id
    cur.execute(
        """INSERT or IGNORE INTO data_user (user_id, first_name_user, last_name_user, username_user,info,photo,calculator) VALUES (?,?,?,?,?,?,?)""",
        (id_var, first_name, last_name, username, count_info, count_photo, count_calculator))  # Записываем данные в таблицу
    base.commit()
    print('База данных создана')
    print('id пользователя', id_var)
    print('имя пользователя', first_name)
    print('фамилия пользователя', last_name)
    print('никнейм пользователя', username)

    return id_var


def get_info(id_var):
    base = sqlite3.connect('ЗаборМастер_Бот.db')
    # В каждой функции вызываем таблицу заново,
    # потому что вызов таблицы будет только один раз в данном файле,
    # а вызов функции будет из другого файла(handlers__message_text), выдаст ошибку
    cur = base.cursor()
    count_info_list = cur.execute(f"SELECT info FROM data_user WHERE user_id=={id_var} ")  # Получаем данные из таблицы по ИД пользователя
    for el in count_info_list:
        count_info = int(el[0]) # Полученные из таблицы данные преобразуем в целое число
        print(count_info)
        return count_info


def get_photo(id_var):
    base = sqlite3.connect('ЗаборМастер_Бот.db')
    # В каждой функции вызываем таблицу заново,
    # потому что вызов таблицы будет только один раз в данном файле,
    # а вызов функции будет из другого файла(handlers__message_text), выдаст ошибку
    cur = base.cursor()
    count_photo_list = cur.execute(f"SELECT photo FROM data_user WHERE user_id=={id_var}") # Получаем данные из таблицы по ИД пользователя
    for el in count_photo_list:
        count_photo = int(el[0])# Полученные из таблицы данные преобразуем в целое число
        return count_photo


def get_calculator(id_var):
    base = sqlite3.connect('ЗаборМастер_Бот.db')
    # В каждой функции вызываем таблицу заново,
    # потому что вызов таблицы будет только один раз в данном файле,
    # а вызов функции будет из другого файла(handlers__message_text), выдаст ошибку
    cur = base.cursor()
    count_calculator_list = cur.execute(f"SELECT calculator FROM data_user WHERE user_id=={id_var}")
    for el in count_calculator_list: # Получаем данные из таблицы по ИД пользователя9-
        count_calculator = int(el[0])# Полученные из таблицы данные преобразуем в целое число
        return count_calculator


def db_update_count(id_var, count_info, count_photo, count_calculator):
    base = sqlite3.connect('ЗаборМастер_Бот.db')# В каждой функции вызываем таблицу заново,
    # потому что вызов таблицы будет только один раз в данном файле,
    # а вызов функции будет из другого файла(handlers__message_text), выдаст ошибку
    cur = base.cursor()

    cur.execute(
        f'UPDATE data_user SET info={count_info}, photo= {count_photo}, calculator= {count_calculator} WHERE user_id== {id_var}')
    # Обновляем значение счетчика после каждого нажатия кнопки
    base.commit()