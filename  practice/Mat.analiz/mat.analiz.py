# -*- coding: utf-8 -*-
from os import system
import os
import matplotlib.pyplot as plt
from numpy import exp, sqrt, sin, log, linspace, array, seterr, nanmin, \
    nanmax, inf

seterr(divide='ignore', invalid='ignore')

func = [lambda x: 1 / x,
        lambda x: x / (x ** 2 - 4 * x + 3),
        lambda x: x ** 2 / (x ** 2 - 4),
        lambda x: sqrt(x ** 2 - 1),
        lambda x: (x ** 2 + 1) / sqrt(x ** 2 - 1),
        lambda x: (exp(-x ** 2) + 2),
        lambda x: (1 / (1 - exp(x))),
        lambda x: (exp(1 / x)),
        lambda x: (sin(x) / x),
        lambda x: (log(1 + x))]

h = [0, 0, 1, None, None, 2, 0, 1, 0, None]
line = [None, None, None, lambda x: x, lambda x: x, None, None, None, None, None]
v = [[0], [1, 3], [-2, 2], [], [-1, 1], [], [0], [0], [0], []]
name = [r'$y = \frac{1}{x}$', r'$y = \frac{x}{x ^ 2 - 4 \cdot x + 3}$', r'$y = \frac{x ^ 2}{x ^ 2 - 4}$',
        r'$y = \sqrt{x ^ 2 - 1}$', r'$y = \frac{x ^ 2 + 1}{\sqrt{x ^ 2 - 1}}$', r'$y = e^{-x ^ 2} + 2$',
        r'$y = \frac{1}{1 - e^x}$', r'$y = e^{\frac{1}{x}}$', r'$y = \frac{\sin(x)}{x}$', r'$y = \ln(1 + x)$']


def select_function_number():
    print("Список доступных функций:")
    print("0. Завершить работу", "1. y = 1/x ", "2. y = x / (x ^ 2 - 4 * x + 3)", "3. y = x ** 2 / (x ^ 2 - 4)",
          "4. y = sqrt(x ^ 2 - 1)", "5. y = (x ^ 2 + 1) / sqrt(x ^ 2 - 1) ", "6. y = exp(-x ^ 2) + 2",
          "7. y = 1 / 1 - exp(x)", "8. y = exp(1 / x)", "9. y = sin(x) / x", "10. y = log(1 + x)", sep="\n")
    number = int(input("Выберите номер функции: "))
    while number not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
        number = int(input("Номер функции некорректный, попробуйте снова: "))
    return number - 1


print("Добро пожаловать!")
number = select_function_number()
while number != -1:
    action = -1
    while action != 2:
        print("Выберите действие: ")
        print("1. Выбрать точку ", "2. Вернуться к списку функций", sep="\n")
        action = int(input())
        while action != 2 and action != 1:
            action = int(input("Номер действия некорректный, введите 1 или 2: "))
        if action == 1:
            try:
                x0 = float(input("Введите точку: "))
                if (number == 3 or number == 4) and -1 < x0 < 1:
                    print('В этой точке функция не существует')
                    continue
                if number == 9 and x0 <= -1:
                    print('В этой точке функция не существует')
                    continue
            except ValueError:
                print("Неверный ввод точки. Введите inf или число")
                continue

            if x0 == float('inf'):  # отрисовка наклонных и горизонтальных асимптот
                x = linspace(-10, 10, 101)
                if not (line[number] is None):  # отрисовка наклонных асимптот
                    y = line[number](x)
                    plt.plot(x, y, color='#939393')
                y = func[number](x)
                if not (h[number] is None):  # отрисовка горизонтальных асимптот
                    plt.hlines(h[number], nanmin(x[x != -inf]), nanmax(x[x != inf]))
            else:
                if x0 in v[number]:  # отрисовка вертикальных асимптот
                    x = linspace(-10, 10, 101)
                    y = func[number](x)
                    for i in range(len(v[number])):
                        plt.vlines(v[number][i], nanmin(y[y != -inf]), nanmax(y[y != inf]))
                else:  # отрисовка графика функции в окрестности точки х0
                    x = linspace(x0 - 1, x0 + 1, 101)
                    y = func[number](x)

            plt.plot(x, y, color='#b23dff')
            plt.grid()
            plt.title('График функции ' + name[number])
            plt.show()
    number = select_function_number()

print("До свидания!")
system("pause")