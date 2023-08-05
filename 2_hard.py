                                        # Задание 2': 3-2-трюк с более сильными ограничениями на схему

# Задание полностью повторяет Задание 2.

# Размер схемы должен быть не больше (12 * n + 1), а глубина не больше 5.

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
