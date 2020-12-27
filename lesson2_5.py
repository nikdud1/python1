my_list = [7, 5, 3, 3, 2]
a = int(input())
i = 0
while(a <= my_list[i]):
    i = i + 1
my_list.insert(i,a)
print(my_list)