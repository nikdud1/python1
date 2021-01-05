from itertools import cycle, count
def numbers(a):
    for i in count(a):
        if i > 10:
            break
        else:
            print(i)
def choice(b):
    k = 0
    for j in cycle(b):
        if(k>10):
            break
        else:
            k = k + 1
            print(j)

