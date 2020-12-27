print("Вводите данные через пробел")
a = input().split()
print(a)
i = 0
if(len(a)%2==0):
    while(i<(len(a)-1)):
        change = a[i+1]
        a[i+1] = a[i]
        a[i] = change
        i = i + 2
else:
    while (i < (len(a) - 2)):
        change = a[i + 1]
        a[i + 1] = a[i]
        a[i] = change
        i = i + 2
print(a)
