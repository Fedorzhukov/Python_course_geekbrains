with open('Test_file.txt', 'w') as fl:
    x = 0
    while True:
        x += 1
        line = (input('Введите {}-ую строку: ').format(x))
        print(('Введите {}-ую строку: ').format(x))
        if line == '':
            break
        else:
            fl.write(line + '\n')
# Вопрос:
# в строке 5 .format не работает, он работает только в строке 6 с print. Как сделать чтобы при запросе данных у пользователя
# через input работал format?