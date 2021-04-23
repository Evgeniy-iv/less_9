from time import sleep
import os

class TrafficLight:


    def running(self, *args):
        self.__color = list(args)
        t = 7
        list_light = []
        for color in self.__color:
            list_light.append(color)
            print("\r {}".format(color), end="")
            sleep(t)
            if t == 7:
                t = 2
            elif t == 2:
                t = 3
            else:
                print("\r {}".format(''), end="")
        assert (list_light == ['Красный', 'Желтый', 'Зеленый']), 'Светофор неисправен'


traffic_light = TrafficLight()
traffic_light.running('Красный', 'Желтый', 'Зеленый')



