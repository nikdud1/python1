class Cell():
    def __init__(self, numbers):
        self.numbers = int(numbers)
    def __add__(self, other):
        return self.numbers + other.numbers
    def __sub__(self, other):
        if(self.numbers - other.numbers>0):
            return self.numbers - other.numbers
        else:
            print("Разность количества ячеек меньше нуля")
    def __mul__(self, other):
        return self.numbers * other.numbers
    def __truediv__(self, other):
        return self.numbers // other.numbers
    def make_order(self,order):
        k = self.numbers
        s = ""
        while(k>order):
            s = s + ("*"*order)+ (r"\n")
            k = k - order
        s = s + "*"*k
        return s
cell1 = Cell(15)
cell2 = Cell(12)
print(cell1+cell2)
print(cell1-cell2)
print(cell1*cell2)
print(cell1/cell2)
print(cell1.make_order(5))
print(cell1.make_order(3))

