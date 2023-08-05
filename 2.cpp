                                        // Задание 2': 3-2-трюк с более сильными ограничениями на схему

#include <iostream>

int main(void) {
    int n;
    std::cin >> n;
    //int stride = n;
    int node_cnt = 3 * n;
    //std::cout << "GATE " << node_cnt++ << " NOT " << 0 << "\n";
    //std::cout << "GATE " << node_cnt++ << " AND " << 0 << " " << node_cnt - 2 << "\n";
    int zero_node;
    //zero_node = node_cnt - 1;
    int output[2 * n + 2];
    //output[n] = zero_node;
    //std::cout << "OUTPUT " << n << " " << zero_node << "\n";
    for (int i = 0; i < n; ++i) {
        std::cout << "GATE " << node_cnt++ << " AND " << i << " " << i + n << "\n";
        std::cout << "GATE " << node_cnt++ << " AND " << i << " " << i + 2 * n << "\n";
        std::cout << "GATE " << node_cnt++ << " OR " << node_cnt - 3 << " " << node_cnt - 2 << "\n";
        
        std::cout << "GATE " << node_cnt++ << " AND " << i + n << " " << i + 2 * n << "\n";
        std::cout << "GATE " << node_cnt++ << " OR " << node_cnt - 3 << " " << node_cnt - 2 << "\n";
        //std::cout << "OUTPUT " << n + 2 + i  << " " << node_cnt - 1 << "\n";
        output[n + 2 + i] = node_cnt - 1;
        
        std::cout << "GATE " << node_cnt++ << " NOT " << node_cnt - 2 << "\n";
        
        
        
        std::cout << "GATE " << node_cnt++ << " OR " << i << " " << i + n << "\n";
        std::cout << "GATE " << node_cnt++ << " OR " << i + 2 * n << " " << node_cnt - 2 << "\n";
        
        std::cout << "GATE " << node_cnt++ << " AND " << node_cnt - 4 << " " << node_cnt - 2 << "\n";
        
        std::cout << "GATE " << node_cnt++ << " AND " << i << " " << node_cnt - 7 << "\n";
        
        std::cout << "GATE " << node_cnt++ << " OR " << node_cnt - 3 << " " << node_cnt - 2 << "\n";
        //std::cout << "OUTPUT " << i << " " << node_cnt - 1 << "\n";
        output[i] = node_cnt - 1;
        
        if (i == 0) {
            std::cout << "GATE " << node_cnt++ << " AND " << node_cnt - 8 << " " << node_cnt - 7 << "\n";
            zero_node = node_cnt - 1;
        }
        
    }
    output[n] = zero_node;
    output[n + 1] = zero_node;
    for (int i = 0; i < 2 * n + 2; ++i) {
        std::cout << "OUTPUT " << i << " " << output[i] << "\n";
    }
    //std::cout << "OUTPUT " << n + 1 << " " << zero_node << "\n";
    return 0;
}
