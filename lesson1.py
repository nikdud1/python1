#1
a = int(input())
b = int(input())
print(a+b)
word = input()
print(word)
#2
time = int(input())
hours = time // 3600
minute = (time // 60) % 60
seconds = time % 60
if hours < 10:
    hours = str('0'+str(hours))
if minute < 10:
    minute = str('0'+str(minute))
if seconds < 10:
    seconds = str('0'+str(seconds))
print(hours,':',minute,':',seconds)
#3
number = (input())
sum = int(number)+int(number+number)+int(number + number + number)
print(sum)
#4
number1 = int(input())
max = 0
while number1>0:
    if(number1%10)>max:
        max = number1%10
    number1 = number1//10
print(max)
#5
proceeds = float(input())
costs = float(input())
profit = proceeds - costs
if profit<0:
    print('издержки больше выручки')
else:
    print('издержки меньше выручки')
    print('Рентабельность',profit/costs, "%")
print("Введите количество сотрудников")
k = int(input())
print("Выручка на одного сотрудника ", proceeds/k)
#6
run1 = float(input())
run2 = float(input())
day = 1
while(run1<run2):
    run1 = run1 * 1.1
    day = day + 1
print("на",day,"-й день спортсмен достиг результата — не менее", run2," км.")


