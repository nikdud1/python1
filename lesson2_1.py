a=[]
a.append(2)
a.append(2.3)
a.append("hello")
a.append(True)
a.append(complex(1,2))
i = 0
for i in a:
    print(i," Type ",type(i))
