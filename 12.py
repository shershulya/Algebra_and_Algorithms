                                        # Задание 12: Алгоритмы подсчёта попарных расстояний на основе матричного умножения — Seidel

# Реализуйте вычисление попарных расстояний между вершинами неориентированного невзвешенного графа с помощью алгоритма Зейделя.
# На входе программы список рёбер неориентированного графа (через пробел). Вершины графа — целые числа, необязательно последовательные.
# Гарантируется, что граф связный. Не используйте явно псевдокод из Википедии, чтобы избежать ложноположительных срабатываний автопроверки на плагиат.
# Ознакомьтесь с теорией алгоритма Зейделя, а затем напишите свой код «из головы».

# Программа должна выдать список возможных попарных расстояний и для каждого расстояния через пробел количество неупорядоченных пар различных вершин,
# находящихся ровно на таком расстоянии. См. примеры.

# Ваш алгоритм должен иметь теоретическую оценку сложности O(n^{2.9}), что можно достичь, используя внутри алгоритма Зайделя быстрое умножение матриц.

# Sample Input 1:

# 0 1
# 0 3
# 0 2
# 3 4
# 4 5

# Sample Output 1:

# 1 5
# 2 5
# 3 3
# 4 2

import sys
import numpy as np
from math import ceil, log

def normalize(A):
    n = len(A)
    for i in range(0, n):
        A[i][i] = 0
        for j in range(0, n):
            if A[i][j] > 0:
                A[i][j] = 1

def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = (A[i][j] + B[i][j])
    return C

def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = (A[i][j] - B[i][j])
    return C

def strassen_rec(A, B):
    n = len(A)

    if n == 1:
        return [[(A[0][0] * B[0][0])]]
    n_div_2 = n // 2

    a11 = [[0 for j in range(0, n_div_2)] for i in range(0, n_div_2)]
    a12 = [[0 for j in range(0, n_div_2)] for i in range(0, n_div_2)]
    a21 = [[0 for j in range(0, n_div_2)] for i in range(0, n_div_2)]
    a22 = [[0 for j in range(0, n_div_2)] for i in range(0, n_div_2)]

    b11 = [[0 for j in range(0, n_div_2)] for i in range(0, n_div_2)]
    b12 = [[0 for j in range(0, n_div_2)] for i in range(0, n_div_2)]
    b21 = [[0 for j in range(0, n_div_2)] for i in range(0, n_div_2)]
    b22 = [[0 for j in range(0, n_div_2)] for i in range(0, n_div_2)]

    for i in range(0, n_div_2):
        for j in range(0, n_div_2):
            a11[i][j] = A[i][j]
            a12[i][j] = A[i][j + n_div_2]
            a21[i][j] = A[i + n_div_2][j]
            a22[i][j] = A[i + n_div_2][j + n_div_2]

            b11[i][j] = B[i][j]
            b12[i][j] = B[i][j + n_div_2]
            b21[i][j] = B[i + n_div_2][j]
            b22[i][j] = B[i + n_div_2][j + n_div_2]

    p1 = strassen_rec(add(a11, a22), add(b11, b22))
    p2 = strassen_rec(add(a21, a22), b11)
    p3 = strassen_rec(a11, subtract(b12, b22))
    p4 = strassen_rec(a22, subtract(b21, b11))
    p5 = strassen_rec(add(a11, a12), b22)
    p6 = strassen_rec(subtract(a21, a11), add(b11, b12))
    p7 = strassen_rec(subtract(a12, a22), add(b21, b22))

    c11 = subtract(add(add(p1, p4), p7), p5)
    c12 = add(p3, p5)
    c21 = add(p2, p4)
    c22 = subtract(add(add(p1, p3), p6), p2)

    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n_div_2):
        for j in range(0, n_div_2):
            C[i][j] = c11[i][j]
            C[i][j + n_div_2] = c12[i][j]
            C[i + n_div_2][j] = c21[i][j]
            C[i + n_div_2][j + n_div_2] = c22[i][j]
    return C


def strassen(A, B):
    n = len(A)
    m = 2 ** int(ceil(log(n, 2)))
    A_padded = [[0 for i in range(m)] for j in range(m)]
    B_padded = [[0 for i in range(m)] for j in range(m)]
    for i in range(n):
        for j in range(n):
            A_padded[i][j] = A[i][j]
            B_padded[i][j] = B[i][j]

    C_padded = strassen_rec(A_padded, B_padded)
    C = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = C_padded[i][j]
    return C

def main():
    edges = []
    for edge in sys.stdin:
        edges.append(list(map(int, edge.split())))

    n = 0
    for edge in edges:
        if edge[0] > n:
            n = edge[0]
        if edge[1] > n:
            n = edge[1]
    n = n + 1

    adj = np.zeros((n, n), dtype=int).tolist()
    for edge in edges:
        adj[edge[0]][edge[1]] += 1
        adj[edge[1]][edge[0]] += 1


    adj_list = []
    adj_list.append(adj)
    adj_prev = adj
    ones = (np.ones((n, n), dtype=int) - np.eye(n, dtype=int)).tolist()
    log_n = int(ceil(log(n, 2)))
    for _ in range(log_n):
        adj_new = strassen(adj_prev, adj_prev)
        adj_new = add(adj, adj_new)
        normalize(adj_new)
        adj_list.append(adj_new)
        if ones == adj_new:
            break
        adj_prev = adj_new

    dist_prev = adj_list[-1]
    for k in reversed(range(log_n - 1)):
        degree = [sum(adj_list[k][i][j] for j in range(n)) for i in range(n)]
        sums = strassen(dist_prev, adj_list[k])
        dist = dist_prev
        for i in range(n):
            for j in range(n):
                if sums[i][j] < dist[i][j] * degree[j]:
                    dist[i][j] = 2 * dist_prev[i][j] - 1
                else:
                    dist[i][j] = 2 * dist_prev[i][j]
        dist_prev = dist

    uniq_vals, uniq_counts = np.unique(dist_prev, return_counts=True)
    for i in range(1, uniq_vals.shape[0]):
        print(uniq_vals[i], uniq_counts[i] // 2)
    
main()