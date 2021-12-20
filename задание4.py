import numpy
from random import randint

#1. используя numpy посчитать сумму ряда 0,,100
x=numpy.array(range(101))
print(x)
print("Сумма ряда",sum(x))


#2. посчитать сумму ряда 0-input()
n = input ("Введите размер ряда: ")
x=numpy.array(range(int(n)))
print(x)
print("Сумма ряда",sum(x))

#3. среднее среди 100 случайных чисел
print("Вывод случайного целого числа ", randint(0, 9))
#x=numpy.array([randint(0,100) for i in range(100)])#альтернативный вариант реализации
x=numpy.random.randint(0, 1000, 100)#заполняем ряд из 100 элементов от 0 до 1000
print(x)
print("Среднее значение:",x.mean())