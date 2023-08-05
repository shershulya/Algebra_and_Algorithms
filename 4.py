                                        # Задание 4: алгоритм Штрассена + быстрое возведение в степень

# Требуется написать программу, возводящую матрицу размера A ∈ {Z}_9^{n * n} в степень n.
# Число n может не быть степенью двойки (в этом случае можно дополнить матрицу в самом начале алгоритма «углом единичной матрицы»).
# Для умножения матриц нужно использовать алгоритм Штрассена со сложностью O(n^{log_2(7)}),
# а для возведения в степень — алгоритм, требующий O(log(n)) матричных умножений
# (либо другой алгоритм того же порядка сложности, дав ссылку на него в комментарии в коде).
# Вся арифметика производится над {Z}_9 то есть, например 5 + 6 = 2, 3 * 7 = 3, 4 - 8 = 5 и т.п..
# Обратите внимание, что {Z}_9 не является полем, поскольку не у каждого элемента есть обратный по умножению, однако нам это и не требуется:
# алгоритм Штрассена использует только сложения, вычитания и умножения, не используя деления, так что работает и в этом случае. 

# Ответом должна быть матрица, все элементы которой находятся в диапазоне {0, 1, ..., 8}.
# На вход (из стандартного потока ввода) подаётся квадратная матрица A, строка матрицы соответствует строке входа, элементы внутри строки разделяются пробелами.
# Пример входа:

# 2 0 1
# 4 2 7
# 3 5 5

# В стандартный поток вывода программа должна выводить в таком же формате матрицу A ^ n. Пример вывода:

# 1 0 5
# 2 1 8
# 6 7 7


from math import ceil, log
import sys

def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = (A[i][j] + B[i][j]) % 9
    return C

def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = (A[i][j] - B[i][j]) % 9
    return C

def strassen_rec(A, B):
    n = len(A)

    if n == 1:
        return [[(A[0][0] * B[0][0]) % 9]]
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

def binexp(A, deg):
    n = len(A)
    res = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        res[i][i] = 1
    while(deg):
        if deg % 2 == 1:
            res = strassen(res, A)
        A = strassen(A, A)
        deg = deg // 2
    return res

def printMatrix(matrix):
    for line in matrix:
        print(" ".join(str(x) for x in line))

def main():
    A = []
    for line in sys.stdin:
        A.append(list(map(int, line.split())))

    C = binexp(A, len(A))

    printMatrix(C)

main()