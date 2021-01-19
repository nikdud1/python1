a = open("lesson5_4_input.txt","r")
b = open("lesson5_4_output.txt","w")
array = ["Ноль","Один","Два","Три","Четыре","Пять","Шесть","Семь","Восемь","Девять"]
c = a.readlines()
for i in c:
    d = i.split(" ")
    k = int(d[2])
    n = str(array[k]) + " - " + str(k)
    b.write(n)
    b.write("\n")
a.close()
b.close()