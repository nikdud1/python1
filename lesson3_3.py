def sum(a,b,c):
    min = 0
    if(a<b):
        min = a
    else:
        min = b
    if(c<min):
        min = c
    return(a+b+c-min)
number1 = float(input("Введите число "))
number2 = float(input("Введите число "))
number3 = float(input("Введите число "))
summa = sum(number1,number2,number3)
print(summa)