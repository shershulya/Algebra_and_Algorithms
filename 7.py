                                        # Задание 7: Конструкция Пэли и коды Боуза—Шриханде

# Реализуйте алгоритм построения кодов Боуза—Шриханде второго типа, которые построены по матрице Адамара, построенной в свою очередь на основе конструкции Пэли.
# На вход программы подаётся единственное целое число n. Гарантируется, что n делится на 4 без остатка, и что (n - 1) — простое число.
# Программа должна выдать 2n строчек длины n, содержащих нули и единицы.
# Строчки должны быть все различны, причём количество различных позиций в любой паре различных строчек должно быть не менее n/2.

# Вычислительной оптимальности не требуется, но полезно, например, предвычислить таблицу значений символа Лежандра.


from collections import deque

def printMatrix(matrix):
    for line in matrix:
        print(" ".join(str(x) for x in line))

def Legendre_symbols(p):
    mod_squares = []
    for i in range(1, p):
        mod_squares.append((i * i) % p)
    leg_sym = [-1]
    for i in range(1, p):
        if i in mod_squares:
            leg_sym.append(1)
        else:
            leg_sym.append(-1)
    return leg_sym

def main():
    n = int(input())
    p = n - 1

    leg_sym = Legendre_symbols(p)

    row = deque(leg_sym)
    first_row = [1] * (len(leg_sym) + 1)
    Hadamard_matrix = [first_row]
    for _ in range(p):
        Hadamard_matrix.append([1] + list(row))
        row.rotate(1)
    
    inv_Hadamard_matrix = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(- Hadamard_matrix[i][j])
        inv_Hadamard_matrix.append(row)

    for i in range(n):
        for j in range(n):
            if Hadamard_matrix[i][j] == -1:
                Hadamard_matrix[i][j] = 0
            if inv_Hadamard_matrix[i][j] == -1:
                inv_Hadamard_matrix[i][j] = 0

    printMatrix(Hadamard_matrix)
    printMatrix(inv_Hadamard_matrix)
    
main()