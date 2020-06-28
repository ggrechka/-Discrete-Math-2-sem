# -*- coding: utf-8 -*-
from os import system
import os


def gauss():
    i, j = 0, 0     # i - строка, j - столбец
    while i < n and j < n:
        # Поиск максимального элемента в j столбце, начиная с i-ой строки
        maxelem = 0.0
        for k in range(i, n):
            if abs(matrix[k][j]) > maxelem:
                l, maxelem = k, abs(matrix[k][j])   # l - номер строки, а maxelem - максимальный элемент
        if maxelem <= eps:  # если макс. элемент меньше либо равен погрешности, то зануляем весь столбец с i строки
            for k in range(i, n):
                matrix[k][j] = 0
            j += 1      # переходим на другой столбец
            continue    # и переходим к новой итерации
        if l != i: # если максимальный элемент не в текущей строке,то меняем строки местами
            for k in range(j, n):
                maxelem, matrix[i][k] = matrix[i][k], matrix[l][k]
                matrix[l][k] = maxelem * (-1)
        for k in range(i + 1, n):   # Обнуление j-й столбца, начиная со строки i+1, вместе с преобразованиями
            maxelem = (-1) * matrix[k][j] / matrix[i][j]
            matrix[k][j] = 0
            for l in range(j + 1, n):   # К k-й строке прибавляем i-ю, умноженную на макс.элемент
                matrix[k][l] += maxelem * matrix[i][l]
        i += 1
        j += 1


# Чтение из файла и запись матрицы в память
name_file1 = input("Введите название файла, в котором хранится матрица(без .txt): ")
if os.path.exists(name_file1+ ".txt"):
    with open(name_file1 + ".txt") as file:
        matrix = []
        for line in file:
            line = line.strip()
            line = list(map(float, line.split()))
            matrix.append(line)

    n = len(matrix)     # так как матрица квадратная, достаточно узнать кол-во строк
    det = 1     # определитель
    eps = 0.001     # точность

    gauss()
    # подсчёт определителя и округление элементов матрицы до 3х знаков после запятой
    for x in range(n):
        for g in range(n):
            if x == g:
                det *= matrix[x][g]
            matrix[x][g] = round(matrix[x][g], 3)

    # Вывод в файл
    name_file2 = input("Введите название файла, в который необходимо записать ответ(без .txt): ")
    k = max([len(str(j)) for i in matrix for j in i])   # ищем максимальную длину строки для красивого вывода
    with open(name_file2 + ".txt", 'w') as graph:
        graph.write('Преобразованная к треугольному виду матрица: '+ '\n')
        for g in range(n):
            for x in range(n):
                elem = str(matrix[g][x])    # преобразование элемента матрицы в строку
                graph.write(' ' + elem + ' ' * (k - len(elem)))     # запись элемента в файл с отступами
            graph.write('\n')
        graph.write('\n'+"Определитель матрицы с учётом погрешности = ")
        graph.write(str(round(det, 3)))     # запись в файл округлённого до 3х знаков после запятой определителя
        print("Результат записан в файл")
else:
    print("Файл с входными данными не найден")