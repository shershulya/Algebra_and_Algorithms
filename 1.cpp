/*
На лекции для построения схемы логарифмической глубины для сложения чисел в двоичной записи мы использовали схему «параллельный префикс»:
быстрое одновременное вычисление всех выражений вида a_1 · a_2 · ... · a_k,(k = 1, 2, ..., n) для бинарной ассоциативной операции · и произвольных a_1, ..., a_n 
Вам предлагается реализовать такую схему, где в качестве · выступает дизъюнкция ∨.
Соответственно, в качестве функциональных элементов допускается использовать только двухвходовую дизъюнкцию (OR).
Входы схемы с номерами 0, 1, ..., n - 1 соответствуют значениям a_1, ..., a_n,
а выходы схемы с номерами 0, 1, ..., n - 1 соответствуют выражениям a_1, a_1 V a_2, a_1 V a_2 V a_3, ...
                                                                                      Ограничения на размер и глубину
Глубина схемы (максимум количества функциональных элементов на пути от входной до выходной вершины) должна быть не больше ⌈log_2(n)⌉,
а число элементов — не должно превосходить размера схемы, разобранной в лекции.

Формат выходных данных такой же, как и в примере выше для XOR. Входные данные — единственное число n; 2 ≤ n ≤ 200.
*/


#include <iostream>
#include <cmath>
#include <algorithm>

int main(void) {
    int n;
    std::cin >> n;
    int node_cnt = n;
    int *layer_prev = new int[n];
    int *layer_cur = new int[n];
    for (int i = 0; i < n; ++i) {
        layer_prev[i] = layer_cur[i] = i;
    }
    float tmp = std::log(n)/std::log(2);
    int depth = (int(tmp) == tmp ? int(tmp) : int(tmp + 1));
    for (int i = 0; i < depth; ++i) {
        int exp = std::pow(2, i);
        for (int j = exp; j < n; ++j) {
            std::cout << "GATE " << node_cnt << " OR " << layer_prev[j - exp] << " " << layer_prev[j] << std::endl;
            layer_cur[j] = node_cnt++;
        }
        std::copy(layer_cur, layer_cur + n, layer_prev);
    }
    for (int i = 0; i < n; ++i) {
        std::cout << "OUTPUT " << i << " " << layer_cur[i] << std::endl;
    }
    free(layer_prev);
    free(layer_cur);
    return 0;
}
