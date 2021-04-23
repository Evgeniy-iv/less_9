class Road:
    def __init__(self, length, width, height):
        self._length = length
        self._width = width
        self._height = height
    def road(self):
        mass = self._length*self._width*self._height*25/1000
        print(f'{mass} т.')

if __name__ == '__main__':

    mass_road = Road(15000, 20, 5)
    mass_road.road()





