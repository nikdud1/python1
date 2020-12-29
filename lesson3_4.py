import math
def degree1(a,b):
    return(a**b)
def degree2(c,d):
    i = 0
    s = 1
    if(d>0):
        while(i<d):
            s = s * c
            i=i+1
    if(d<0):
        while (i < abs(d)):
            s = s / c
            i = i + 1
    return s
x = float(input())
y = float(input())
print(degree1(x,y))
print(degree2(x,y))