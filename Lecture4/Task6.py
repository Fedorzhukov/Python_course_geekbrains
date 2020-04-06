import itertools
start = int(input('Введите стартовое число: '))
# А
for i in itertools.count(start, 1):
    print(i)

# В
init_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in itertools.cycle(init_list):
    print(i)
