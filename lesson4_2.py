from random import randint
a = []
for i in range(10):
    a.append(randint(0,100))
print(a)
i = 1
new_list = []
for el in a:
    if i == len(a):
        break
    else:
        if(el<a[i]):
            new_list.append(a[i])
    i = i + 1
print(new_list)