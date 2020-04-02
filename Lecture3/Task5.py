accumulated_sum = 0


def sum_func(x):
    s = 0
    for i in x:
        s += int(i)
    return s


while True:
    decision = (input('Нажмите Q для выхода. Введите строку чисел с пробелами: ')).upper()
    if decision == 'Q':
        break
    x_list = decision.split(' ')
    x_sum = sum_func(x_list)
    accumulated_sum += x_sum
    print('общая сумма = ', accumulated_sum)
