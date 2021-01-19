f = open("output.txt","w")
n = ""
k=1
while(k!=0):
    n = input("Введите строку ")
    if (n==""):
        k = 0
    else:
        f.write(n)
        f.write("\n")
f.close()
