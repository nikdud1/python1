f = open("lesson5_3.txt","w")
s = 0
n = input("Введите числа через пробел ")
f.write(n)
f.close()
f = open("lesson5_3.txt","r")
a = f.read()
numbers = a.split(" ")
for i in numbers:
    s = s + int(i)
print("Сумма равна ", s)
f.close