class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def cal(self):
        print((self._length * self._width * 25 * 5)/1000, 'тонн')

test = Road(5000, 20)
test.cal()


