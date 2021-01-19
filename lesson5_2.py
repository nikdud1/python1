f = open("lesson5_2.txt","r")
words = 0
lines = 0
a = []
a = f.readlines()
for i in a:
    lines = lines + 1
    b = i.split(" ")
    words = words + len(b)
print("lines: ", lines)
print("words: ", words)
f.close()