import json
total_income = 0
num = 0
my_dict1 = {}
my_dict2 = {}
with open('Test_file6.txt') as fl:
    for i, line in enumerate(fl.readlines()):
        income = int((line.split(' '))[-2])
        expenses = (line.split(' '))[-1]
        expenses = expenses.replace('.', '')
        expenses = int(expenses.strip())
        print('Фирма номер {}: доходы {}, расходы {}'. format(i+1, income, expenses))
        if expenses < income:
            num += 1
            total_income += income
        my_dict1[(line.split(' '))[0]] = income
    print('Средняя прибыль по {} компаниям составила {}'.format(num, total_income/num))
    my_dict2['Average profit'] = total_income/num
    lst = [my_dict1, my_dict2]

with open('Test_file7.txt', 'w') as fl2:
    json.dumps(lst)

"""
Почему-то не появилась запись в новом файле
"""