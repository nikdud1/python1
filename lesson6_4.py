class Car:
    speed = 0
    color = ""
    name = ""
    is_police = False
    def go(self):
        print("Машина поехала ")
    def stop(self):
        print("Машина остановилась ")
    def turn(self,direction):
        print("Машина повернула ", direction)
    def show_speed(self, speed):
        Car.speed = speed
        print("Скорость равна ", Car.speed, " км/ч")
    def Name(self,name,color):
        self.name = name
        self.color = color

class Town_car(Car):
    def show_speed(self, speed):
        Car.speed = speed
        print("Скорость равна ", Car.speed, " км/ч")
        if(Car.speed> 60):
            print("ПРЕВЫШЕНИЕ СКОРОСТИ")
class Sport_car(Car):
    def sport_car(self):
        print("Увеличьте скорость")
class Work_car(Car):
    def show_speed(self, speed):
        Car.speed = speed
        print("Скорость равна ", Car.speed, " км/ч")
        if (Car.speed > 40):
            print("ПРЕВЫШЕНИЕ СКОРОСТИ")
class Police_car(Car):
    def police_car(self):
        Car.is_police = True
        print("Поймайте преступников")
a = Town_car()
color = "green"
speed = 80
name = "golf"
a.go()
a.show_speed(speed)
b = Sport_car()
speed = 200
b.stop()
b.show_speed(speed)
c = Work_car()
speed = 90
c.turn("Направо")
c.show_speed(speed)
d = Police_car()
speed= 100
d.go()
d.show_speed(speed)