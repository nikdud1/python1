from json import dump
dict1 = dict()
dict2 = dict()
f = open("lesson5_7_input.txt","r")
k = 0
s = 0
n = 0
for i in f:
    name = i.split()[0]
    income = int(i.split(" ")[2])
    costs = int(i.split(" ")[3])
    profit = income - costs
    if(profit>0):
        s = s + profit
        n = n + 1
    dict1[name]=profit
s = float(s/n)
dict2["average_profit"] = s
with open("lesson5_7_output.json", "w", ) as h:
    dump([dict1, dict2], h)
f.close()
