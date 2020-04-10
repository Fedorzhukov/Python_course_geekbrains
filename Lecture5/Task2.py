with open('Test_file.txt') as fl:
    lines = fl.readlines()
    print('Всего строк в файле: {}'.format(len(lines)))
    for num, value in enumerate(lines):
        print('Длина {}-ой строки: {}'.format(num+1, len(value)))


