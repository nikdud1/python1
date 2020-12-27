a = []
i = 0
f = int(input("сколько товаров "))
for i in range(f):
    number = i + 1
    name = input("имя ")
    price = input("цена ")
    amount = input("кол-во ")
    unit = input("единицы измерения ")
    a.append({"номер": number,"имя":name,"цена":price,"кол-во":amount,"единицы измерения":unit})
print(a)
dictionary = {"номер":[],"имя":[],"цена":[],"кол-во":[],"единицы измерения":[]}
i = 0
for i in range(f):
    dictionary["номер"].append(i+1)
    dictionary["имя"].append(a[i]["имя"])
    dictionary["цена"].append(a[i]["цена"])
    dictionary["кол-во"].append(a[i]["кол-во"])
    dictionary["единицы измерения"].append(a[i]["единицы измерения"])
print(dictionary)