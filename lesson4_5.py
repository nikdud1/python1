from functools import reduce
def sum(a,b):
    return(a+b)
list = [el for el in range(100,1001) if (el % 2 == 0)]
print(list)
s = reduce(sum,list)
print(s)