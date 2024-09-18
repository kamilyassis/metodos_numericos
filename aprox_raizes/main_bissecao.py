import bissecao

#função f(x)
def f(x):
    return x**3 - 2*x - 5

#intervalo
a = 2.0
b = 3.0

print('Função: x^3 - 2x - 5, no intervalo [2, 3]')

tolerancia = 0.001
raiz = bissecao.bissecao(a, b, f, tolerancia)

if raiz == None:
    print("Erro ao calcular a raiz.")
else:
    print("Raiz encontrada em bisseção (com tolerância = 0.001):", raiz)