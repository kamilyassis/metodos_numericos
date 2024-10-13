import numpy as np

def ajuste_quadratico(x):

    n = len(x)
    sum_x = np.sum(x)
    sum_x_2 = np.sum([i**2 for i in x])
    sum_x_3 = np.sum([i**3 for i in x])
    sum_x_4 = np.sum([i**4 for i in x])
    sum_y = np.sum([f(i) for i in x])
    sum_xy = np.sum([i * f(i) for i in x])
    sum_x_2_y = np.sum([i**2 * f(i) for i in x])

    A = np.array([
        [n, sum_x, sum_x_2],
        [sum_x, sum_x_2, sum_x_3],
        [sum_x_2, sum_x_3, sum_x_4]
    ])

    b = np.array([sum_y, sum_xy, sum_x_2_y])

    b0, b1, b2 = np.linalg.solve(A, b)

    return b0, b1, b2

f = lambda x: x/2 + 2

x = [-2, 0, 1, 4]
b0, b1, b2 = ajuste_quadratico(x)

'''print(f"b0 = {b0}, b1 = {b1}, b2 = {b2}")
print(f"y = {b0} + {b1}x + {b2}x^2")
'''
print(f"b0 = {round(b0, 4)}, b1 = {round(b1, 4)}, b2 = {round(b2, 4)}")
print(f"y = {round(b0, 4)} + {round(b1, 4)}x + {round(b2, 4)}x^2")