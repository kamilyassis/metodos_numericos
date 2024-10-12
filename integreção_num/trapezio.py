f = lambda x: 2 * x + 5

def trapezio(x):
    
    h = x[-1] - x[0]
    b = (f(x[0]) + f(x[-1])) / 2
    
    return b * h

def trapezio_repetido(x):

    a = x[0]
    b = x[-1]
    n = len(x) - 1
    
    h = (b - a) / n
    
    soma = f(a) + f(b)
    
    for i in range(1, n):

        soma += 2 * f(x[i])

    return soma * h / 2

#lista de pontos
x = [1, 2, 3, 4]

print("função associada: 2x + 5")
print("lista de X's: ", x)
print("lista de Y's: ", [f(i) for i in x])
print("Integração por Trapezio Simples: ", trapezio(x))
print("Integração por Trapezio Repetido: ", trapezio_repetido(x))