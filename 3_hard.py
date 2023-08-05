                                        # Задание 3': Универсальный многополюсник для n = 4

# Хардкодинг схем в программе при n>1n>1 не допускается. Программа должна строить схему алгоритмически!

# Задание полностью совпадает с предыдущим, разница лишь в том, что теперь Ваша программа должна корректно работать при 1 ≤ n ≤ 4 и есть ограничение на глубину.
# Подумайте, как использовать идеи с лекции и реализации функций не только в виде ДНФ, но и в виде КНФ (конъюнкция элементарных дизъюнкций),
# чтобы глубина оптимального по размеру многополюсника порядка n не превышала max{2, n + ⌈log_2(n)⌉}.
# Соответственно, например, для n = 4 многополюсник должен иметь сложность 65532 и глубину не более 6.

# Sample Input:
#   1

# Sample Output:
#   GATE 1 NOT 0
#   GATE 2 AND 0 1
#   GATE 3 OR 0 1
#   OUTPUT 0 0
#   OUTPUT 1 1
#   OUTPUT 2 2
#   OUTPUT 3 3

n = int(input())
node_cnt = n
layer_prev = list(range(n))
if n == 1:
    depth = 2
    one = 0b11
    value_in_gates = [0b01]
if n == 2:
    depth = 3
    one = 0b1111
    value_in_gates = [0b0011, 0b0101]
if n == 3:
    depth = 5
    one = 0b11111111
    value_in_gates = [0b00001111, 0b00110011, 0b01010101]
if n == 4:
    depth = 6
    one = 0b1111111111111111
    value_in_gates = [0b0000000011111111, 0b0000111100001111,
                        0b0011001100110011, 0b0101010101010101]

for _ in range(depth):
    layer_cur_values = []
    layer_cur = []
    for i in enumerate(layer_prev):
        inv = one - value_in_gates[i[1]]
        if inv not in value_in_gates:
            layer_cur_values.append(inv)
            print('GATE', node_cnt, 'NOT', i[1])
            layer_cur.append(node_cnt)
            node_cnt += 1

    for cur in value_in_gates:
        values_without_cur = [value for value in value_in_gates if value != cur]
        for other in values_without_cur:
            conj = cur & other
            if (conj not in value_in_gates and conj not in layer_cur_values):
                print('GATE', node_cnt, 'AND', value_in_gates.index(cur), value_in_gates.index(other))
                layer_cur.append(node_cnt)
                node_cnt += 1
                layer_cur_values.append(conj)

    for cur in value_in_gates:
        values_without_cur = [value for value in value_in_gates if value != cur]
        for other in values_without_cur:
            dis = cur | other
            if (dis not in value_in_gates and dis not in layer_cur_values):
                print('GATE', node_cnt, 'OR', value_in_gates.index(cur), value_in_gates.index(other))
                layer_cur.append(node_cnt)
                node_cnt += 1
                layer_cur_values.append(dis)

    for x in layer_cur_values:
        value_in_gates.append(x)
    layer_prev = layer_cur

for item in enumerate(value_in_gates):
    print('OUTPUT', item[0], item[0])