from functools import reduce
new_l = [i for i in range(100, 105) if i % 2 == 0]


def my_f(n1, n2):
    return n1 * n2


print(reduce(my_f, new_l))



# Можно ли как-то в генераторе списков обновлять записываемую переменную?
# new_l = [i for i in range(100, 105) if i % 2 == 0]
# mult = 1
# mult = [i * mult for i in new_l]

# Таким образом, чтобы переменная mult каждый раз умножалась на элемент i. У меня так не получилось
