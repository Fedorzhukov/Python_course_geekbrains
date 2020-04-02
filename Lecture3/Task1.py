while True:
    decision = (input('Нажмите Q для выхода. Любую клавишу для продолжения.')).upper()
    if decision == 'Q':
        break

    def my_func(x, y):
        try:
            result = x / y
        except ZeroDivisionError:
            result = 'На ноль делить нельзя'
        return result

    x = int(input('введите первое делимое: '))
    y = int(input('введите первое делитель: '))

    ratio = my_func(x, y)
    print(ratio)