# Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму 
# двух целых неотрицательных чисел. Из всех арифметических операций 
# допускаются только +1 и -1. Также нельзя использовать циклы.

def summa(a, b):
    if b == 0:
        return a
    return summa(a + 1, b - 1)

a = int(input('Enter Number a: '))
b = int(input('Enter Number b: '))
print(f'Sum {a} + {b} is {summa(a, b)}')


