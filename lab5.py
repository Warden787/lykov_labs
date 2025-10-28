print("Задание 1")
try:
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
except ValueError:
    print("Ошибка, введите число")
else:
    while a>b:
        a=a-b
    print("Незанятая часть отрезка =",a)
print("Задание 2")
from math import *
try:
    Xn=float(input("Введите начало отрезка "))
    Xk=float(input("Введите конец отрезка "))
    dx=float(input("Введите щаг "))
except ValueError:
    print("Ошибка, введите число")
else:
    x=Xn
    while x <=Xk:
        if x<0:
            z=x**2
        elif 0<x<1:
            z=sin(x)
        else:
            z=cos(x*3)
        print("Ответ = ",z)
        x=x+dx
print("Задание 3")
try:
    N=int(input())
except ValueError:
    print("Ошибка, введите число")
else:
    a=0
    b=1
    for i in range(N):
        a=a+b
        b=b+2
    print("Квадрат числа =",a)




