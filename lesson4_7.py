def factorial(h):
    s = 1
    a = []
    for i in range (1, h + 1):
        s = s * i
        a.append(s)
    return a
def generator(m):
    for i in factorial(m):
        yield i
n = input("Введите n ")
a = generator(int(n))
print(a)
for i in a:
    print(i)

