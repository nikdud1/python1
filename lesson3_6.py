def up(word1):
    return(word1.title())
def up2(word2):
    word3=""
    a = word2.split(" ")
    for j in a:
        word3 = word3 + up(j) + " "
    return(word3)
word = input("Введите слово с маленькой буквы ")
print(up(word))
letter = input("Введите предложение ")
print(up2(letter))
