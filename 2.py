                                        # Задание 2: 3-2-трюк
# На лекции для построения схемы логарифмической глубины для умножения чисел в двоичной записи мы использовали «3-2-трюк»:
# быстрое построение по тройке чисел пары чисел, такой, что сумма пары равняется сумме тройки.
# Вам предлагается реализовать схему, которая осуществляет указанное преобразование.
# На входе схемы 3n битовых значений (в схеме они имеют номера соответственно от 0 до 3n-1), в таком порядке:
# a_0, ..., a_{n-1}, b_0, ..., b_{n-1}, c_0, ..., c_{n-1}. Эти значения кодируют соответственно числа A, B, C;
# при этом a_0, b_0, c_0 — это самые младшие разряды двоичных записей, а a_{n-1}, b_{n-1}, c_{n-1} — самые старшие.
# В схеме ровно 2 * (n + 1) вершин должны быть помечены как выходные и соответствовать битовым записям x_0, ..., x_n и y_0, ...,y_n
# (именно в таком порядке, т.е., например, выходу схемы с порядковым номером n + 2 соответствует бит y_1) чисел X и Y, таких, что X + Y = A + B + C.
# В качестве функциональных элементов допускается использовать: отрицание (NOT), двухвходовую конъюнкцию (AND), двухвходовую дизъюнкцию (OR).


# Размер схемы (общее число невходных вершин) должен быть не больше 20 * (n + 1), а глубина
# (максимум количества функциональных элементов на пути от входной до выходной вершины) не больше 10.
# (ВНИМАНИЕ! Загляните также на следующий шаг, там задание отличается только ограничениями на размер/глубину схемы.
# Если сразу представляете, как делать, сдавайте одну и ту же программу на следующем и на текущем шаге.)

# Формат выходных данных такой же, как и в примере для XOR. Входные данные — единственное число n, 1 ≤ n ≤ 1000.

n = int(input())
node_cnt = 3 * n
zero_node = 0
output = []
for i in range(n):
    print('GATE', node_cnt, 'NOT', i + 2 * n)
    node_cnt += 1
    
    print('GATE', node_cnt, 'AND', i, i + n)
    node_cnt += 1
    print('GATE', node_cnt, 'OR', i, i + n)
    node_cnt += 1
    
    print('GATE', node_cnt, 'NOT', node_cnt - 2)
    node_cnt += 1
    print('GATE', node_cnt, 'NOT', node_cnt - 2)
    node_cnt += 1
    
    print('GATE', node_cnt, 'AND', node_cnt - 3, node_cnt - 2)
    node_cnt += 1
    print('GATE', node_cnt, 'OR', node_cnt - 5, node_cnt - 2)
    node_cnt += 1
    
    print('GATE', node_cnt, 'AND', i + 2 * n, node_cnt - 2)
    node_cnt += 1
    print('GATE', node_cnt, 'OR', node_cnt - 7, node_cnt - 1)
    output.insert(n + 2 + i, node_cnt)
    node_cnt += 1
    
    print('GATE', node_cnt, 'AND', i + 2 * n, node_cnt - 3)
    node_cnt += 1
    print('GATE', node_cnt, 'AND', node_cnt - 10, node_cnt - 5)
    node_cnt += 1
    print('GATE', node_cnt, 'OR', node_cnt - 2, node_cnt - 1)
    output.insert(i, node_cnt)
    node_cnt += 1
    
    if i == 0:
        print('GATE', node_cnt, 'AND', i + 2 * n, 3 * n)
        zero_node = node_cnt
        node_cnt += 1

output.insert(n, zero_node)
output.insert(n + 1, zero_node)
for i in range(0, 2 * n + 2):
    print('OUTPUT', i, output[i])