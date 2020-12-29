a=[]
s = 0
i = 0
j = 0
print("Введите * для окончания ввода")
while(i!=1):
    if(s!=0):
        input("Для продолжения нажмите Enter")
    string1 = input("Введите строку с числами ")
    a = string1.split(" ")
    for j in a:
        if(j=="*"):
            i = 1
            break
        else:
            s = s + int(j)
    print("Сумма равна", s)
