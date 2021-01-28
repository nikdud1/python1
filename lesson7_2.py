from abc import abstractclassmethod, ABC
class Clothes(ABC):
    def __init__(self,parametr):
        self.parametr = int(parametr)
    @property
    @abstractclassmethod
    def calculation(self):
        pass
    def __add__(self, other):
        return (self.calculation + other.calculation)

class Coat(Clothes):
    @property
    def calculation(self):
        self.sum = self.parametr/6.5 + 0.5
        return self.sum
class Costume(Clothes):
     @property
     def calculation(self):
         self.sum = self.parametr * 2 + 0.3
         return self.sum

coat1 = Coat(100)
costume1 = Costume(170)
print("Расход такни на пальто равен ", coat1.calculation)
print("Расход такни на костюм равен ", costume1.calculation)
print("Общий расход ткани равен ", coat1 + costume1)
