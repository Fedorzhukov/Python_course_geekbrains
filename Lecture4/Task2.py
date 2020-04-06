test_list = [1, 2, 3, 4, 5, 6, 0, -1, 1, -5, 10]
new_list = [i for num, i in enumerate(test_list) if test_list[num] > test_list[num-1]]

print(new_list)


# Получилось, но если в конце листа поставить элемент, который будет меньше первого элекмента листа, то получится,
# что первый элемент стравнивается с последним, первый больше  итоже выведется в финальный лист. Как это обойти?
# Надо как-то ограничить num, но не могу понять как

test_list = [0, 1, -1]
new_list = [i for num, i in enumerate(test_list) if test_list[num] > test_list[num-1]]

print(new_list)