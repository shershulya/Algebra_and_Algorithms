                                        # Задание 6: НВП-разложение

# Требуется написать программу, строящую НВП-разложение матрицы из {Z}_2^{n * n}
# (т.е. матрица булева и вся арифметика производится над {Z}_2, то есть 1 + 1 = 0, 1 = -1).

# Алгоритм должен иметь гарантированную теоретическую оценку времени работы O(n^{2.9}), где n — размерность входной матрицы (можно быстрее, но нельзя O(n^3)).
# Использование сторонних библиотек для линейно-алгебраических вычислений не допускается, за исключением numpy для хранения данных.
# Если Вы используете для справки какой-либо из «низкоуровневых» псевдокодов алгоритма НВП, либо вообще готовый исходник,
# то нужно это делать так: разобраться в псевдокоде, затем закрыть его и написать с нуля свою программу.
# В противном случае система проверки решений на наличие плагиата будет негодовать.

# На вход (из стандартного потока ввода) подаётся квадратная невырожденная матрица A,
# строка матрицы соответствует строке входа, элементы внутри строки разделяются пробельными символами. Пример входа:

# 1 0 1
# 1 1 0
# 1 1 1

# В стандартный поток вывода программа должна выводить в таком же формате три квадратные матрицы:
# сначала нижнетреугольную L, затем верхнетреугольную U, затем матрицу перестановки P, такие, что A = LUP. Пример вывода:

# 1 0 0
# 1 1 0
# 1 1 1

# 1 0 1
# 0 1 1
# 0 0 1

# 1 0 0
# 0 1 0
# 0 0 1


from math import ceil, log
import sys

import numpy as np

MOD = 2

def printMatrix(matrix):
    for line in matrix:
        print(" ".join(str(x) for x in line))

def printMatrixPad(matrix, n):
    for i in range(n):
        for j in range(n - 1):
            print(matrix[i][j], ' ', sep='', end='')
        print(matrix[i][n - 1])

def add(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = (A[i][j] + B[i][j]) % MOD
    return C

def subtract(A, B):
    n = len(A)
    C = [[0 for j in range(0, n)] for i in range(0, n)]
    for i in range(0, n):
        for j in range(0, n):
            C[i][j] = (A[i][j] - B[i][j]) % MOD
    return C

def strassen_rec(A, B):
    n = len(A)

    if n == 1:
        return [[(A[0][0] * B[0][0]) % MOD]]
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
    height = A.shape[0]
    depth = A.shape[1]
    width = B.shape[1]
    if (height != depth or depth != width):
        n = width
        m = 2 ** int(ceil(log(n, 2)))
        A_padded = [[0 for i in range(m)] for j in range(m)]
        B_padded = [[0 for i in range(m)] for j in range(m)]
        for i in range(height):
            for j in range(depth):
                A_padded[i][j] = A[i][j]
        for i in range(depth):
            for j in range(width):
                B_padded[i][j] = B[i][j]

        C_padded = strassen_rec(A_padded, B_padded)
        C = [[0 for i in range(width)] for j in range(height)]
        for i in range(height):
            for j in range(width):
                C[i][j] = C_padded[i][j]
        return np.array(C)
    else:
        n = len(B)
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
        return np.array(C)

def matrix_mul(A, B):
    n = A.shape[0]
    m = B.shape[1]
    C = np.zeros([n, m], dtype=int)
    for i in range(n):
        for j in range(m):
            tmp=0
            for k in range(A.shape[1]):
                tmp += A[i][k] * B[k][j]
            C[i][j] = (C[i][j] + tmp) % MOD
    return C

def matrix_sub(A, B):
    n = A.shape[0]
    m = A.shape[1]
    C = np.zeros([n, m], dtype=int)
    for i in range(n):
        for j in range(m):
            C[i][j] = (A[i][j] - B[i][j]) % MOD
    return C

def inverse_lower_triangular(A):
    n = A.shape[0]
    A_inv = np.zeros([n, n], dtype=int)
    if n == 1:
        return A
        # x = A[0][0]
        # if x == 0:
        #     A_inv[0][0] = 0
        # else:
        #     A_inv[0][0] = 1 / A[0][0]
        # return A_inv
    n_in_half = n >> 1
    B = A[:n_in_half, :n_in_half]
    C = A[n_in_half:, :n_in_half]
    D = A[n_in_half:, n_in_half:]
    B_inv = inverse_upper_triangular(B)
    D_inv = inverse_upper_triangular(D)
    

    A_inv[:n_in_half, :n_in_half] = B_inv
    A_inv[n_in_half:, :n_in_half] = strassen(strassen(D_inv, C), B_inv)
    A_inv[n_in_half:, n_in_half:] = D_inv
    return A_inv

def inverse_upper_triangular(A):
    n = A.shape[0]
    A_inv = np.zeros([n, n], dtype=int)
    if n == 1:
        return A
        # x = A[0][0]
        # if x == 0:
        #     A_inv[0][0] = 0
        # else:
        #     A_inv[0][0] = 1 / A[0][0]
        # return A_inv
    n_in_half = n >> 1
    B = A[:n_in_half, :n_in_half]
    C = A[:n_in_half, n_in_half:]
    D = A[n_in_half:, n_in_half:]
    B_inv = inverse_upper_triangular(B)
    D_inv = inverse_upper_triangular(D)
    

    A_inv[:n_in_half, :n_in_half] = B_inv
    A_inv[:n_in_half, n_in_half:] = strassen(strassen(B_inv, C), D_inv)
    A_inv[n_in_half:, n_in_half:] = D_inv
    return A_inv


def LUP_Decomposition(A, m, p):
    if m == 1:
        L = np.eye(1, dtype=int)
        P = np.eye(p, dtype=int)
        for c in range(p):
            if A[0][c] != 0:
                P[0][0] = 0
                P[0][c] = 1
                P[c][c] = 0
                P[c][0] = 1
                break
        U = matrix_mul(A, P)
        return L, U, P
    else:
        m_in_half = m >> 1
        B, C = np.vsplit(A, 2)
        
        L1, U1, P1 = LUP_Decomposition(B, m_in_half, p)
        
        P1_inv = np.array([[row[i] for row in P1] for i in range(P1.shape[0])])
        D = matrix_mul(C, P1_inv)
        E = U1[:m_in_half, :m_in_half]
        F = D[:m_in_half, :m_in_half]
        E_inv = inverse_upper_triangular(E)
        FE = strassen(F, E_inv)
        G = matrix_sub(D, strassen(FE, U1))
        G_value = G[:, m_in_half:]
        
        L2, U2, P2 = LUP_Decomposition(G_value, m_in_half, p - m_in_half)
        
        I3 = np.eye(m_in_half)
        P3 = np.zeros([p, p], dtype=int)
        P3[:m_in_half, :m_in_half] = I3
        P3[m_in_half:, m_in_half:] = P2
        P3_inv = np.array([[row[i] for row in P3] for i in range(P3.shape[0])])
        H = matrix_mul(U1, P3_inv)

        L = np.zeros([m, m], dtype=int)
        L[:m_in_half, :m_in_half] = L1
        L[m_in_half:, :m_in_half] = FE
        L[m_in_half:, m_in_half:] = L2

        U = np.zeros([m, p], dtype=int)
        U[:m_in_half, :] = H
        U[m_in_half:, m_in_half:] = U2

        P = strassen(P3, P1)

        # print('Params A - ' + str(m) + ' ' + str(p))
        # print('\nL1')
        # printMatrix(L1)
        # print('\nU1')
        # printMatrix(U1)
        # print('\nP1')
        # printMatrix(P1)
        # print('\nD')
        # printMatrix(D)
        # print('\nE')
        # printMatrix(E)
        # print('\nF')
        # printMatrix(F)
        # print('\nG')
        # printMatrix(G)
        # print('\nG_value')
        # printMatrix(G_value)
        # print('\nL2')
        # printMatrix(L2)
        # print('\nU2')
        # printMatrix(U2)
        # print('\nP2')
        # printMatrix(P2)
        # print('\nP3')
        # printMatrix(P3)
        # print('\nH')
        # printMatrix(H)
        # print('\nL')
        # printMatrix(L)
        # print('\nU')
        # printMatrix(U)
        # print('\nP')
        # printMatrix(P)
        # print('-----')
        # print()
        return L, U, P

def generator (N_tests):
    for i in N_tests:
        pass

def main():
    A = []
    for line in sys.stdin:
        A.append(list(map(int, line.split())))

    n = len(A)
    m = 2 ** int(ceil(log(n, 2)))
    A = np.array(A)
    A_padded = np.zeros([m, m], dtype=int)
    A_padded[:A.shape[0], :A.shape[1]] = A

    L, U, P = LUP_Decomposition(A_padded, len(A_padded), len(A_padded))

    print('\nL')
    printMatrixPad(L, n)
    print('\nU')
    printMatrixPad(U, n)
    print('\nP')
    printMatrixPad(P, n)
main()