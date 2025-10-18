#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>


struct LinearProgrammingProblem {
    std::vector<std::vector<double>> A; 
    std::vector<double> b; 
    std::vector<double> c; 
};

std::vector<double> interiorPointMethod(const LinearProgrammingProblem& problem) {
    int n = problem.c.size(); 
    int m = problem.b.size();

    double epsilon = 1e-6; 
    double t = 0.1; 
    double alpha = 0.1; 
    int max_iter = 100; 

    std::vector<double> x(n, 1); 
    std::vector<double> s(m, 1); 
    std::vector<double> lambda(m, 0); 

    int k = 0; 
    while (k < max_iter) {
        std::vector<double> mu(m); 
        for (int i = 0; i < m; i++) {
            mu[i] = s[i] * lambda[i];
        }

        std::vector<double> grad(n);
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                grad[i] += problem.A[j][i] * lambda[j];
            }
            grad[i] -= problem.c[i];
        }

        double duality_gap = 0;
        for (int i = 0; i < m; i++) {
            duality_gap += mu[i];
        }
        duality_gap /= m;

        if (duality_gap < epsilon) {
            break; 
        }

        std::vector<double> rhs(m);
        for (int i = 0; i < m; i++) {
            rhs[i] = -s[i] + t / lambda[i];
        }

        std::vector<double> dx(n);
        std::vector<double> ds(m);
        std::vector<double> dlambda(m);

        /
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dx[i] += problem.A[j][i] * rhs[j];
            }
            dx[i] -= grad[i];
        }

        for (int i = 0; i < m; i++) {
            ds[i] = -s[i] * lambda[i] - rhs[i];
            dlambda[i] = (t - lambda[i] * s[i]) / lambda[i];
        }

        
        for (int i = 0; i < n; i++) {
            x[i] += alpha * dx[i];
        }

        for (int i = 0; i < m; i++) {
            s[i] += alpha * ds[i];
            lambda[i] += alpha * dlambda[i];
        }

        k++;
    }

    return x;
}

int main() {
    
    LinearProgrammingProblem problem;
    problem.A = {{-1, -2}, {-3, 1}, {1, -1}};
    problem.b = {-4, 3, -2};
    problem.c = {1, 1};

        
    std::vector<double> solution = interiorPointMethod(problem);

    
    std::cout << "Optimal solution: ";
    for (double value : solution) {
        std::cout << value << " ";
    }
    std::cout << std::endl;

    return 0;
}
