class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Start drawing')

class Pen(Stationery):
    def draw(self):
        print(self.title, 'starts drawing')

class Pencil(Stationery):
    def draw(self):
        print(self.title, 'starts drawing')

class Handle(Stationery):
    def draw(self):
        print(self.title, 'starts drawing')


test1 = Pen('pen1')
test1.draw()

test2 = Pencil('pencil1')
test2.draw()