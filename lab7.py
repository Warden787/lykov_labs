print("Задание 1")
print("Самое длинное слово в тексте")
a=input("Введите текст:")
w=""
long=""
for c in a:
    if c!=" ":
        w+=c
    else:
        if len(w) > len(long):
            long=w
        w=""
if len(w) > len(long):
    long=w
print("Самое длинное слово:", long)

print("Задание 2")
print("Количество слов в строке")
a=input("Введите строку:")

w=0
flag=1
for c in a:
    if c!=" " and flag == 1:
        w+=1
        flag=0
    if c==" ":
        flag=1
print("Количество слов :",w)

print("Задание 3")
print("Работа со списком чисел")
try:
    size=int(input("Введите количество элементов списка: "))
except ValueError:
    print("Ошибка, введите число")
else:
    a=[]
    for i in range(size):
        try:
            x=float(input("Введите эллемент:"))
        except ValueError:
            print("Ошибка, введите число")
            break
        else:
            a.append(x)
    print("Список: ", a)

    s=0
    for x in a:
        if x>0:
            s=s+x
    print("Сумма положительных чисел:", s)

    maxi=0
    mini=0
    for i in range(len(a)):
        if abs(a[i]) > abs(a[maxi]):
            maxi = i
        if abs(a[i]) < abs(a[mini]):
            mini = i

    if maxi < mini:
        c=maxi +1
        d=mini
    else:
        c=mini+1
        d=maxi

    if c>=d:
        print("Между ними нет элементов")
    else:
        p=1
        for i in range(c,d):
            p=p*a[i]
        print("Произведение элементов =",p)

