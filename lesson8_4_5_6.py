class EquipmentWarehouse():
    price = ""
    amount = ""
    name = ""
    def sum (self, other1,other2):
        s = int(self.amount)*int(self.price)+int(other1.amount)*int(other1.price)+int(other2.amount)*int(other2.price)
        print("Общая стоимость инвентаря ",s)
    def add(self, amount):
        self.amount = int(self.amount) + int(amount)
    def sub(self,amount):
        self.amount = int(self.amount) + int(amount)
class Printer(EquipmentWarehouse):
    printertype = ""
    papersize = ""
    speedforminute = ""
    connection = ""
    cartridgeammount = ""
    def check(self):
        k = 0
        a = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"]
        if (not(self.papersize in a)):
            print("Неправильно введен формат бумаги")
        for i in self.price:
            if(i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0"):
                k=1
        if(int(self.price) < 1 and k==0):
            k = 1
        if (k==1):
            print("Неправильно введена цена")
        k = 0
        for i in self.amount:
            if(i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0"):
                k=1
        if (int(self.amount) < 1 and k == 0):
            k = 1
        if (k==1):
            print("Неправильно введено количество")
        k = 0
        for i in self.speedforminute:
            if(i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0"):
                k=1
        if (int(self.speedforminute) < 1 and k == 0):
            k = 1
        if (k==1):
            print("Неправильно введена скорость печати")
        k = 0
        for i in self.cartridgeammount:
            if(i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0"):
                k=1
        if (int(self.price) < 1 and k == 0):
            k = 1
        if (k==1):
            print("Неправильно введено количество катриджей")
        k = 0
    def __init__(self,price,amount,name,printertype,papersize,speedforminute,connection,catridgeammount ):
        self.price = price
        self.amount = amount
        self.name = name
        self.printertype = printertype
        self.papersize = papersize
        self.speedforminute = speedforminute
        self.connection = connection
        self.cartridgeammount = catridgeammount
class Scaner(EquipmentWarehouse):
    resolution = ""
    scanertype = ""
    papersize = ""
    connection = ""
    def check(self):
        a = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"]
        k = 0
        if (not(self.papersize in a)):
            print("Неправильно введен формат бумаги")
        for i in self.price:
            if(i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0"):
                k=1
        if (int(self.price) < 1 and k == 0):
            k = 1
        if (k==1):
            print("Неправильно введена цена")
        k = 0
        for i in self.amount:
            if(i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0"):
                k=1
        if (int(self.amount) < 1 and k == 0):
            k = 1
        if (k==1):
            print("Неправильно введено количество")
        k = 0
    def __init__(self,price,amount,name,scanertype,papersize,connection, resolution):
        self.price = price
        self.amount = amount
        self.name = name
        self.scanertype = scanertype
        self.connection = connection
        self.resolution = resolution
        self.papersize = papersize
class Xerox(EquipmentWarehouse):
    xeroxtype = ""
    papersize = ""
    speedforminute = ""
    connection = ""
    def check(self):
        k = 0
        a = ["A0","A1","A2","A3","A4","A5","A6","A7","A8","A9","A10"]
        if (not(self.papersize in a)):
            print("Неправильно введен формат бумаги")
        for i in self.price:
            if(i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0"):
                k=1
        if (int(self.price) < 1 and k == 0):
            k = 1
        if (k==1):
            print("Неправильно введена цена")
        k = 0
        for i in self.amount:
            if(i != "1" and i != "2" and i != "3" and i != "4" and i != "5" and i != "6" and i != "7" and i != "8" and i != "9" and i != "0"):
                k=1
        if (int(self.amount) < 1 and k == 0):
            k = 1
        if (k==1):
            print("Неправильно введено количество")
        k = 0
    def __init__(self,price,amount,name,xeroxtype,papersize,speedforminute,connection ):
        self.price = price
        self.amount = amount
        self.name = name
        self.xeroxtype = xeroxtype
        self.speedforminute = speedforminute
        self.connection = connection
        self.papersize = papersize
a = Printer("10000","100","HP","laser","A4","40","ethernet","1000")
a.check()
b = Scaner("5000","10","HP","laser","A3","cable", "1280*720")
b.check()
c = Xerox("20000","5","HP","laser","A1","100","ethernet")
c.check()
a.sum(b,c)