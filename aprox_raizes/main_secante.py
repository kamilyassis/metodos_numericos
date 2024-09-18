import secante

#função f(x)
def f(x):
    return x**3 - 2*x - 5

#intervalo
a = 2.0
b = 3.0

print('Função: x^3 - 2x - 5, no intervalo [2, 3]')

#secante com tolerância
x_0 = a
x_1 = b

tolerancia = 0.001
raiz, iteracoes = secante.secante(a, b, x_0, x_1, f, tolerancia)

if raiz == None:
    print("Erro ao calcular a raiz.")
else:
    print("Raiz encontrada em secante (com tolerância = 0.001):", raiz)
    print(iteracoes, " iterações foram necessárias!")