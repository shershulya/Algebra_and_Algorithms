                                        # Задание 9: Разрез минимальной плотности

# Реализуйте приближённый алгоритм поиска разреза минимальной плотности
# (алгоритм на основе собственного вектора, соответствующего второму по величине собственному значению лапласиана графа).
# На вход программы подаются рёбра неориентированного графа в виде:

# <количество рёбер>
# <id начала ребра> <id конца ребра>
# <id начала ребра> <id конца ребра> 
# …

# id вершин — натуральные числа (необязательно последовательные), изолированных вершин нет.
# Выход программы — разделённые пробельными символами и упорядоченные по возрастанию номера вершин, включённых в наименьшую по мощности компоненту разреза.
# Если есть разные полученные в строгом соответствии с алгоритмом ответы, имеющие одинаковую плотность, то нужно вывести лексикографически минимальный из них.
# (Минимальный как список чисел, а не как строку, например, из разрезов “1 2 3 112” и “1 2 3 12” нужно вывести именно “1 2 3 12”.)

import numpy as np

def dense_cut(cut, adj, n):
    number_of_edges = 0
    for vertex in cut:
        for i in range(n):
            if adj[vertex][i]:
                if i not in cut:
                    number_of_edges += 1

    return n * number_of_edges / (cut.size * (n - cut.size))

def main():
    E = int(input())
    edges = []
    for _ in range(E):
        edge = input()
        edges.append(list(map(int, edge.split())))

    n = 0
    for edge in edges:
        if edge[0] > n:
            n = edge[0]
        if edge[1] > n:
            n = edge[1]
    n = n + 1

    adj = np.zeros((n, n), dtype=int)
    for edge in edges:
        adj[edge[0]][edge[1]] += 1
        adj[edge[1]][edge[0]] += 1
    deg = np.sum(adj, axis=1)
    Laplacian = np.diag(deg) - adj
    vals, vecs = np.linalg.eigh(Laplacian)
    Fisher_val = vals[1]
    Fisher_vec = vecs[:, 1]
    sorted_vec = np.argsort(Fisher_vec)[::-1]
    
    best_cuts = []
    best_dense = 1000000000
    for i in range(n // 2):
        cut = sorted_vec[:i + 1]
        dense = dense_cut(cut, adj, n)
        if dense < best_dense:
            best_dense = dense
            best_cuts = [cut]
        elif dense == best_dense:
            best_cuts.append(cut)

    for i in range(n // 2, n - 1):
        cut = sorted_vec[i + 1:]
        dense = dense_cut(cut, adj, n)
        if dense < best_dense:
            best_dense = dense
            best_cuts = [cut]
        elif dense == best_dense:
            best_cuts.append(cut)

    sorted_cuts = sorted(best_cuts)
    print(" ".join(str(x) for x in sorted_cuts[0]))
    
main()