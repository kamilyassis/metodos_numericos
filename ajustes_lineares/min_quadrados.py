import numpy as np

def min_quadrados(x):

    n = len(x)
    sum_x = np.sum(x)
    sum_x_2 = np.sum([i**2 for i in x])
    sum_y = np.sum([f(i) for i in x])
    sum_xy = np.sum([i * f(i) for i in x])

    A = np.array([[n, sum_x], [sum_x, sum_x_2]])
    B = np.array([sum_y, sum_xy])

    a, b = np.linalg.solve(A, B)

    return a, b

def qualidade_ajuste(x, a, b):

    n = len(x)
    sum_y = np.sum([f(i) for i in x])
    sum_y_2 = sum_y**2
    u = [a + (b*i) for i in x]
    distancia = np.sum([(f(x[i]) - u[i])**2 for i in range(n)])

    r_2 = abs(1 - (distancia / (sum_y_2 - 1*sum_y**2/n)))
    var = distancia / (n - 2)

    return r_2, var

f = lambda x: x/2 + 2

x = [-2, 0, 1, 4]
a, b = min_quadrados(x)

print(f"b0 = {a}, b1 = {b}")
print(f"y = {a} + {b}x")
print(f"R^2 = {qualidade_ajuste(x, a, b)[0]}")
print(f"Var = {qualidade_ajuste(x, a, b)[1]}")

