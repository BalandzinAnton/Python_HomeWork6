# МОРСКОЙ БОЙ
import random
from random import randint

# Создаем игровое поле
def add_playing_field(ships):
    matrix = [[i for i in range(10)] for j in range(10)]
    count = 0
    for i in range(10):
        for j in range(10):
            matrix[i][j] = 0

    # Заполняем поле кораблями
    while count < ships:
        x = int(randint(0, ships - 1))
        y = int(randint(0, ships - 1))
        if matrix[x][y] == 1:
            count -= 1
        else:
            matrix[x - 1][y - 1] = 1
        count += 1
    return matrix

# СТРЕЛЯЕМ
def our_shooting(shots, matrix_human, matrix_cpu):
    my_result = 0
    cpu_result = 0
    for i in range(shots):
        x_my = int(input("Введите координату x = "))
        y_my = int(input("Введите координату y = "))
        if matrix_cpu[x_my - 1][y_my - 1] == 1:
            print("Я ПОПАЛ")
            matrix_cpu[x_my - 1][y_my - 1] = 0
            my_result += 1
        else:
            print("Я ВЫСТРЕЛИЛ МИМО")
        x_cpu = int(randint(0, shots - 1))
        y_cpu = int(randint(0, shots - 1))
        if matrix_human[x_cpu][y_cpu] == 1:
            print("КОМПЬЮТЕР ПОПАЛ")
            matrix_human[x_cpu][y_cpu] = 0
            cpu_result += 1
        else:
            print("КОМПЬЮТЕР ВЫСТРЕЛИЛ МИМО")
    return [my_result, cpu_result]

results = our_shooting(10, add_playing_field(10), add_playing_field(10))

if results[0] > results[1]:
    print(f"Я сбил кораблей: {results[0]}, компьютер сбил кораблей: {results[1]}. ПОБЕДА!!!")
if results[0] == results[1]:
    print(f"Я сбил кораблей: {results[0]}, компьютер сбил кораблей: {results[1]}. НИЧЬЯ!!!")
if results[0] < results[1]:
    print(f"Я сбил кораблей: {results[0]}, компьютер сбил кораблей: {results[1]}. ПОРАЖЕНИЕ!!!")
