with open('Test_file2.txt') as fl:
    lines = fl.readlines()
    dictionar = {}
    for line in lines:
        name, salary = line.split(' ')
        dictionar.update({name: salary.strip()})

    total_salary = [int(i) for i in dictionar.values()]
    print('Средняя ЗП: {} рублей в месяц'.format(sum(total_salary)/len(dictionar)))

    print([i for i in dictionar.keys() if int(dictionar[i]) < 20000])
