my_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}

fl_ru = open('Test_file3_RUS.txt', 'a')
with open('Test_file3_ENG.txt') as fl_en:
    lines = fl_en.readlines()
    for line in lines:
        if line == '\n':
            continue
        else:
            name, vales = line.split(' — ')
            line_ru = str(my_dict[name] + ' — ' + vales + '\n')
        fl_ru.write(line_ru)
fl_ru.close()

