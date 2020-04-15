class Worker:
    def __init__(self, speed, color, name, is_police, turn_ch):
        self.max_speed_towncar = 60
        self.max_speed_workcar = 40
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police
        self.turn = turn_ch

    def go(self):
        print('Car goes')

    def stop(self):
        print('Car stops')

    def turn_m(self):
        print('Car turns', self.turn)

    def show_speed(self):
        print(self.speed, 'km/h')


class TownCar(Worker):
    def show_speed(self):
        if self.speed > self.max_speed_towncar:
            print('ALARM! Slow down! You exceed speed limit by {} km/h'.format(self.speed - self.max_speed_towncar))
        else:
            print(self.speed, 'km/h')

class SportCar(Worker):
    pass

class WorkCar(Worker):
    def show_speed(self):
        if self.speed > self.max_speed_workcar:
            print('ALARM! Slow down! You exceed speed limit by {} km/h'.format(self.speed - self.max_speed_workcar))
        else:
            print(self.speed, 'km/h')

class PoliceCar(Worker):
    pass

car1 = Worker(100, 'red', 'car1', False, 'left')
car1.go()
car1.turn_m()
car1.show_speed()
car1.stop()

car2 = WorkCar(60,'blue', 'car2', False, 'right')
car2.show_speed()

# А как