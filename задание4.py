import numpy
from random import randint

x=numpy.array(range(100));
print(x)
print("Сумма ряда",sum(x))

#n = input ("Введите размер ряда: ")
#x=numpy.array(range(int(n)));
#print(x)
#print("Сумма ряда",sum(x))

print("Вывод случайного целого числа ", randint(0, 9))