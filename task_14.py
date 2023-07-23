# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

N = int(input("Введите число N: "))
if N == 0:
    print("Нет целых степеней двойки, не превосходящих число N.")

integer_degrees = 1

while integer_degrees <= N:
    print(integer_degrees)
    integer_degrees *= 2