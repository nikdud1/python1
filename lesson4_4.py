from random import randint
a = []
for i in range(10):
    a.append(randint(0,10))
print(a)
new_list = []
i = 1
for el in a:
    if i == len(a):
        if (el not in a[0:(len(a)-1)]):
            new_list.append(el)
        break
    else:
        if (el not in a[i:len(a)] and el not in a[0:(i-1)]):
            new_list.append(el)
    i = i + 1
print(new_list)