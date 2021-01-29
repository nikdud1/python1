class OwnError(Exception):
    def __init__(self,txt):
        self.txt = txt
while(1):
    a= input("Введите делимое ")
    b = input("Введите делитель ")
    try:
        a = int(a)
        b = int(b)
        if b == 0:
            raise OwnError("Делитель равен 0, введите заново")
    except ValueError:
        print("Вы ввели не число")
    except OwnError as err:
        print(err)
    else:
        print("Все хорошо ")
        print(a/b)
        break


