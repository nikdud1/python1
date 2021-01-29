class Complex():
    real = 0
    imagine = 0
    def __add__(self, other):
        sum = complex(self.real, self.imagine) + complex(other.real, other.imagine)
        print(sum)
    def sub(self, other):
        sum = complex((self.real*other.real-self.imagine*other.imagine), (self.real*other.imagine+self.imagine*other.real))
        print(sum)
a = Complex()
b = Complex()
a.real = int(input("Введите вещественную часть 1 числа "))
a.imagine = int(input("Введите мнимую часть 1 числа "))
b.real = int(input("Введите вещественную часть 2 числа "))
b.imagine = int(input("Введите мнимую часть 2 числа "))
a+b
a.sub(b)