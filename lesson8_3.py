class OwnError(Exception):
    def __init__(self,txt):
        self.txt = txt
b = []
s = ""
k=0
while(1):
    a = input("Введите число,если хотите закончить ввод напишите stop ")
    if a == "stop":
        break
    else:
        try:
            for i in a:
                if ((i!="1"and i!="2" and i!="3" and i!="4" and i!="5" and i!="6"and i!="7"and i!="8" and i!="9" and i!="0")):
                    raise OwnError("Вы ввели не число")
                    k=1
                    break

            if k==0:
                b.append(int(a))
        except OwnError as err:
            print(err)
print(b)



