class Road:

    def weight(self, length, width):
        self._length = length
        self._width = width
        print("Масса асфальта в тоннах равна",self._length*self._width*25*5*0.001)
a = Road()
length1 = float(input("Введите длину дороги "))
width1 = float(input("Введите ширину дороги "))
a.weight(length1,width1)