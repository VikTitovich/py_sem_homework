# Задача 26: Напишите программу, которая на вход принимает два числа A и B, 
# и возводит число А в целую степень B с помощью рекурсии.

def power(number, degree):
    if degree == 0:
        return 1
    return number * power(number, degree - 1)

n = int(input('Enter Number: '))
d = int(input('Enter Degree: '))
print(f'Number {n} in degree {d} is {power(n, d)}')