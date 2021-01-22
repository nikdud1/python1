import time
class TrafficLight:
    def running(self):
        self.__color = "Красный"
        time1 = time.time()
        red = 7.00
        yellow = 2.00
        green = 7.00
        print(self.__color)
        while(time.time()-time1 < red):
            continue
        self.__color = "Желтый"
        print(self.__color)
        time1 = time.time()
        while (time.time() - time1 < yellow):
            continue
        self.__color = "Зеленый"
        print(self.__color)
        time1 = time.time()
        while (time.time() - time1 < green):
            continue
a = TrafficLight()
a.running()
