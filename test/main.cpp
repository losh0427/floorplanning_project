#include <iostream>
#include <vector>
#include <algorithm>

struct edge {
    double a;
    double b;
};

bool edgeComparator(const edge& e1, const edge& e2) {
    if (e1.a == e2.a)
        return e1.b < e2.b;
    return e1.a < e2.a;
}
void f( double& aa, double& bb){
    double t = aa; 
    aa = bb;
    bb =t;
    return;
}
int main() {
    std::vector<edge> Cv_list = { {2.5, 1.0}, {1.2, 3.0}, {2.5, 1.0}, {3.5, 2.0}, {1.2, 3.0} };

    // Step 1: Sort the vector
    std::sort(Cv_list.begin(), Cv_list.end(), edgeComparator);

    // Step 2: Remove duplicates
    auto it = std::unique(Cv_list.begin(), Cv_list.end(), [](const edge& e1, const edge& e2) {
        return (e1.a == e2.a) && (e1.b == e2.b);
    });
    Cv_list.erase(it, Cv_list.end());

    // Print the unique edges
    for ( auto& e : Cv_list) {
        f(e.a,e.b);
        std::cout << "Edge: a = " << e.a << ", b = " << e.b << std::endl;
    }

    return 0;
}
