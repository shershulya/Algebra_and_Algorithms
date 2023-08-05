                                        # Задание 10:  3-однородные множества и задача 3_≥7/8‑ВЫПОЛНИМОСТЬ

# Реализуйте алгоритм, который, используя построенное на лекции 3-однородное множество наборов, находит решение задачи 3_≥7/8‑ВЫПОЛНИМОСТЬ.
# На вход программы подаются через пробел два числа n и m — число переменных и число скобок соответственно, а далее подаются m строк, кодирующих клаузы, в формате:

# <neg>var1 <neg>var2 <neg>var3
# …

# где на месте <neg> может быть либо пустая строка, либо дефис, который означает отрицание соответствующей переменной. При этом на месте var1/var2/var3 стоят числа от 1 до n.

# На выходе программа выдаёт единственную строку, содержащую без пробелов информацию о том, какие битовые значения можно присвоить переменным, так,
# чтобы как минимум 7/8 * m клауз обратились в единицу (true).
# Проследите, что используемая для построения однородного множества наборов матрица в точности такая, как описано в лекции:
# столбцы упорядочены лексикографически; каждый столбец начинается с единицы, за которой следует двоичная запись номера столбца; нумерация ведётся с нуля.

# Ограничения задачи: 2 ≤ n ≤ 1024, 1 ≤ m ≤ 10000.

import numpy as np
import copy
from math import ceil, log

def comb_impl(table, seq, n):
    if n:
        for i in range(2):
            seq[-n] = i
            comb_impl(table, seq, n - 1)
    else:
        table.append(copy.copy(seq))

def truth_table(n):
    table = []
    seq = [0] * n
    comb_impl(table, seq, n)
    return np.array(table)

def main():
    inp = list(map(int, input().split()))
    N = inp[0]
    m = inp[1]
    clauses = []
    for _ in range(m):
        clause = input()
        clauses.append(list(map(int, clause.split())))

    k = int(ceil(log(N, 2)))
    n = 2 ** k

    table = truth_table(k).T
    g_matrix = np.ones((k + 1, n), dtype=int)
    g_matrix[1:, :] = table

    lin_comb = truth_table(k + 1)
    codes = []
    for i in range(lin_comb.shape[0]):
        tmp = np.zeros(n, dtype=int)
        for j in range(0, lin_comb.shape[1]):
            tmp = np.add(tmp, lin_comb[i][j] * g_matrix[j][:]) % 2
        codes.append(tmp)

    for code in codes:
        score = 0
        for clause in clauses:
            var0 = clause[0]
            var1 = clause[1]
            var2 = clause[2]

            if var0 > 0:
                x0 = code[var0 - 1]
            else:
                x0 = 1 - code[-var0 - 1]
            if var1 > 0:
                x1 = code[var1 - 1]
            else:
                x1 = 1 - code[-var1 - 1]
            if var2 > 0:
                x2 = code[var2 - 1]
            else:
                x2 = 1 - code[-var2 - 1]

            if x0 or x1 or x2:
                score += 1
        # if score / m >= 7 / 8:
            # print("".join(str(x) for x in code[:N]))
            # return
        if score > best_score:
            best_score = score
            best_set = code[:N]
    print(best_score)
    print(best_set)
    print("".join(str(x) for x in best_set))
    
main()