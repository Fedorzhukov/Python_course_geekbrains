user_time = input('введите время в секундах: ')

sec_per_hour = 3600
sec_per_min = 60
user_time = int(user_time)
if user_time < 0:
    print('Ошибка! Ведите положительное число')
elif user_time == 0:
    print('00:00:00')
elif user_time > 0:
    # Hours
    user_time_hours = user_time // sec_per_hour
    user_time_hours_int = int(user_time_hours)
    if user_time_hours < 10:
        user_time_hours = '0' + str(user_time_hours)

    # Minutes
    sec_reminder = user_time - (sec_per_hour * int(user_time_hours))
    user_time_min = sec_reminder // sec_per_min
    user_time_min_int = int(user_time_min)
    if user_time_min < 10:
        user_time_min = '0' + str(user_time_min)

    # Seconds
    sec_reminder = user_time - (sec_per_hour * user_time_hours_int) - (sec_per_min * user_time_min_int)
    user_time_sec = sec_reminder
    if user_time_sec < 10:
        user_time_sec = '0' + str(user_time_sec)

    print(str(user_time_hours) + ':' + str(user_time_min) + ':' + str(user_time_sec))

#    Есть пара вопросов по реализации:

# 1) Хотел добавить проверку на то, что при введении есть хоть какой-то символ.
#    Попробовал так <user_time ! = ''>, но не получилось. Как правльно добавить эту проврку?
# 2) хотел доабавить проверку на ввод любых символов кроме цифр
#    Попробовал так <type(user_time) == 'int'>, но не получилось т.к. весь input это str. Как правильно добавить такую проверку?
