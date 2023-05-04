# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь
# в первой строке вводит натуральное число N – количество элементов в массиве. В последующих строках
# записаны N целых чисел Ai. Последняя строка содержит число X
# n = 5
# 1 2 3 4 5
# x = 3

# -> 1

N = int(input('Enter the Number of Items in the List A: '))
Enter_A = input('Enter the Items in the List, Separated by the Space Bar: ').split()
Num_A = list(map(int, Enter_A))
if len(Num_A) != N:
    print('Enter the Correct Number of Items.')
else:
    X = int(input('Enter Number X: '))
    k = 0
    for i in range(N):
        if Num_A[i] == X:
            k += 1
    print(f'Number X={X} in the List A = {k}') 
    
    

    
    
