                                        # Задание 5: совершенное паросочетание

# Требуется написать программу, которая с помощью вероятностного алгоритма (оценка вероятности ошибки которого основана на лемме Липтона—деМилло—Шварца—Зиппеля)
# проверяет, есть ли в заданном графе совершенное паросочетание.
# На самом деле, считать определитель необязательно: достаточно любым относительно быстрым способом проверить невырожденность соответствующей матрицы,
# ведь для ответа в задаче нужна только эта информация; можно воспользоваться обычным исключением Гаусса.
# ВАЖНО! Как мы обсуждали на лекции, чтобы ошибки округления/переполнения не приводили к ложному положительному ответу,
# нужно работать не с числами с плавающей точкой, а с вычетами по какому-нибудь достаточно большому простому модулю. Это обязательное требование к программе.

# На вход (из стандартного потока ввода) подаётся список рёбер двудольного графа без изолированных вершин с равномощными долями.
# Вершины каждой доли графа занумерованы последовательными целыми неотрицательными числами, начиная с нуля. Формат входа:

# <количество рёбер>
# <номер вершины из левой доли> <номер вершины из правой доли>
# …
# <номер вершины из левой доли> <номер вершины из правой доли>

# Программа должна вывести в стандартный поток вывода единственное слово yes, если в графе есть совершенное паросочетание, и no в противном случае.
# Общее количество вершин графа не превосходит 200.


import sys
import numpy as np
import random as rnd

mod = 10000019


def binpow(a, n):
    res = 1
    while n:
        if n % 2 == 1:
            res = (res * a) % mod
        a = (a * a) % mod
        n = n // 2
    return res


def Gauss(matrix, n):
    det = 1
    for i in range(n):
        idx = i
        for j in range(i + 1, n):
            if abs(matrix[i][i]) < abs(matrix[i][j]):
                idx = j

        if idx != i:
            det = -det
            for j in range(i, n):
                temp = matrix[j][i]
                matrix[j][i] = matrix[j][idx]
                matrix[j][idx] = temp

        for k in range(i + 1, n):
            coeff = (matrix[k][i] * binpow(matrix[i][i], mod - 2)) % mod
            for j in range(i, n):
                matrix[k][j] = (matrix[k][j] - (matrix[i][j] * coeff) % mod) % mod

    for i in range(n):
        det = (det * matrix[i][i]) % mod

    if det:
        print('yes')
    else:
        print('no')

    return det


def EdmondsMatrix(edges):
    max_v = np.max(np.array([v for v, u in edges])) + 1
    matrix = np.zeros((max_v, max_v), dtype=int)

    for v, u in edges:
        matrix[v][u] = rnd.randint(1, mod - 1)

    return matrix, max_v


def main():
    edges = []
    n_edges = input()
    for line in sys.stdin:
        edges.append(list(map(int, line.split())))

    matrix, n = EdmondsMatrix(edges)

    Gauss(matrix, n)

main()
