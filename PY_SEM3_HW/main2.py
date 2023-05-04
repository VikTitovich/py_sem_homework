# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

N = int(input('Enter the Number of Items in the List A: '))
Enter_A = input('Enter the Items in the List, Separated by the Space Bar: ').split()
Num_A = list(map(int, Enter_A))
if len(Num_A) != N or N == 0:
    print('Enter the Correct Number of Items.')
else:
    X = int(input('Enter Number X: '))
    min = abs(X - Num_A[0])
    j = 0
    for i in range(1, N):
        k = abs(X - Num_A[i])
        if k < min:
            min = k
            j = i
    print(f'Number {Num_A[j]} in the List A ~ {X}')
          