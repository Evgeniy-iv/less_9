class Stationery:

    def __init__(self, title):
        self.title = title
    def draw(self):
        print('Запуск отрисовки')
class Pen(Stationery):
    def draw(self):
        print('Пишем ручкой')
class Pencil(Stationery):
    def draw(self):
        print('Рисуем карандашом')
class Handle(Stationery):
    def draw(self):
        print('Черкаем маркером')

if __name__ == '__main__':

    stationery_instance = Stationery('Канцелярская принадлежность')
    stationery_instance.draw()

    pen_instance = Pen('Ручка')
    pen_instance.draw()

    pencil_instance = Pencil('Карандаш')
    pencil_instance.draw()

    handle_instance = Handle('Маркер')
    handle_instance.draw()


