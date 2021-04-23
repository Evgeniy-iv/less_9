class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Машина поехала')
    def stop(self):
        print(f'Машина остановилась')
    def turn(self, to):
        print(f'Машина повернула {to}')

    def show_speed(self):
        print(f'Скорость {self.speed}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print(f'Вы превысили скорость')
class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f'Вы превысили скорость')


if __name__ == '__main__':
        work_car = WorkCar(50, 'синяя', 'газель', True)
        work_car.go()
        work_car.show_speed()

        town_car = TownCar(70, 'белая', 'маршрутка', True)
        town_car.go()
        town_car.show_speed()






