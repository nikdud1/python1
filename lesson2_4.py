print("Вводите данные через пробел")
a = input().split()
g = 1
for i in a:
    if len(i)>10:
        print(g, i[0:10],"\n")
    else:
        print(g, i,"\n")
    g = g + 1
