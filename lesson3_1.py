def div(a,b):
    if b==0:
        print("Деление на ноль!")
        while b == 0:
            b = float(input("Введите делитель заново "))
    return(float(a)/b)
c = float(input("Введите делимое "))
d = float(input("Введите делитель "))
e = div(c,d)
print(e)



