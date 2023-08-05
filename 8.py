                                        # Задание 8: Вершинное покрытие графа

# Реализуйте приближённый алгоритм поиска минимального взвешенного вершинного покрытия графа
# (ошибающийся по весу не более чем вдвое) на основе описанной на лекции схемы «решаем задачу ЛП и округляем».
# Использовать решение задачи ЛП обязательно.
# В программах допускается (и рекомендуется) не реализовывать самостоятельно, а использовать сторонние решатели задачи ЛП, доступные на Stepik.
# В частности, на Python допускается использовать scipy.optimize.linprog.

# На вход программы подаются веса вершин и рёбра в виде:

# <количество вершин N>
# <вес вершины 0>
# …
# <вес вершины (N-1)>
# <количество рёбер>
# <id начала ребра> <id конца ребра>
# <id начала ребра> <id конца ребра> 
# …

# Веса вершин — положительные целые числа. Выход программы — разделённые пробельными символами номера вершин, включённых в покрытие.


from scipy.sparse import csr_matrix
from scipy.optimize import linprog

import numpy as np

def main():
    N = int(input())
    wt = []
    for _ in range(N):
        wt.append(int(input()))

    E = int(input())
    edges = []
    for _ in range(E):
        edge = input()
        edges.append(list(map(int, edge.split())))

    row = []
    col = []
    data = []
    for i in range(E):
        row.append(i)
        row.append(i)
        col.append(edges[i][0])
        col.append(edges[i][1])
        data.append(1)
        data.append(1)

    A = csr_matrix((data, (row, col)), shape=(E, N))
    res_lp = linprog(wt, A_ub=-A, b_ub=-np.ones(E), bounds=(0.0, 1.0),
                options={"tol": 0.05, "sparse": True}, method='interior-point').x

    result = []
    for idx, val in enumerate(res_lp):
        if val >= 0.5:
            result.append(idx)
    print(" ".join(str(x) for x in result))
    
main()