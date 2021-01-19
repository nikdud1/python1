g = open("lesson5_6.txt","r")
dict = dict()
number1 = ""
number = 0
for i in g:
    a = i.split(":")
    b = a[1].split(" ")
    b.pop(0)
    for j in b:
        for y in j:
            if (y=="0"or y=="1"or y=="2"or y=="3"or y=="4"or y=="5"or y=="6"or y=="7"or y=="8"or y=="9"):
                number1 = number1 + y
        number = int(number1) + number
        number1=""
    dict[a[0]]=number
    number = 0
print(dict)
g.close
