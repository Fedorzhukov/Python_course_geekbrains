import time
import itertools


class TrafficLight:
    __color = ['green', 'yellow', 'red']
    __waiting_time = {'green': 5, 'yellow': 2, 'red': 7}

    def running(self):
        for num, value in enumerate(itertools.cycle(self.__color[::-1])):
            time.sleep(self.__waiting_time[value])
            print(value)
            if num == 15:
                break

example = TrafficLight()
example.running()


# Не понял как условнять. Что значит проверка порядка режимов, если они всегда в одном порядке. Или пользователь сам
# выбирает какой режим включить?


# class TrafficLight:
#     __color = ['green', 'yellow', 'red']
#     __waiting_time = {'green': 5, 'yellow': 2, 'red': 7}
#
#     def running(self):
#         while True:
#             cur_color = input('1-Green, 2-Yellow, 3-Red. Enter-quit')
#             if cur_color == '':
#                 break
#             print(self.__waiting_time.keys())
#
#
#
# example = TrafficLight()
# example.running()