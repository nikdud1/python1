f = open("lesson5_3.txt","w")
n = ""
a = []
min = []
s = 0
k=1
number = 0
while(k!=0):
    n = input("Введите фамилию и зарплату, чтобы закончить, введите пустую строку ")
    if (n==""):
        k = 0
    else:
        number = number + 1
        f.write(n)
        f.write("\n")
        a = n.split(" ")
        s = s + int(a[1])
        if(int(a[1])> 20000):
            min.append(n)
print("Список тех, у кого зарплата выше 20000")
print(min)
print("Средняя зарплата равна:", float(s/number))
f.close()