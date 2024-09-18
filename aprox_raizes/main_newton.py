import newton

#função que dá certo
#função f(x)
def f(x):
    return x**3 - 2*x - 5

#derivada de f(x)
def f_linha(x):
    return 3*x**2 - 2

#segunda derivada de f(x)
def f_linha_linha(x):
    return 6*x

#intervalo
a = 2.0
b = 3.0

print('Função: x^3 - 2x - 5, no intervalo [2, 3]')

#newton com tolerância
x_0 = a
tolerancia = 0.001
raiz = newton.newton_tolerancia(a, b, x_0, f, f_linha, f_linha_linha, tolerancia)

if raiz == None:
    print("Erro ao calcular a raiz.")
else:
    print("Raiz encontrada em newton (com tolerância = 0.001):", raiz)

#newton com repetição
repeticao = 5
raiz_repet = newton.newton_tolerancia(a, b, x_0, f, f_linha, f_linha_linha, repeticao)

if raiz_repet == None:
    print("Erro ao calcular a raiz.")
else:
    print("Raiz encontrada em newton (com 5 repetições):", raiz_repet)


'''
#função que dá errado
def f2(x):
    return x**3

def f2_linha(x):
    return 3*x**2

def f2_linha_linha(x):
    return 6*x

#intervalo
a2 = -1.0
b2 = 1.0

print('\n Função: x^3, no intervalo [-1, 1]')

#newton com tolerância
x2_0 = a2
tolerancia2 = 0.001
raiz2 = newton.newton_tolerancia(a2, b2, x2_0, f2, f2_linha, f2_linha_linha, tolerancia2)

if raiz2 == None:
    print("Erro ao calcular a raiz (com tolerancia).")
else:
    print("Raiz encontrada em newton (com tolerância = 0.001):", raiz2)

#newton com repetição
repeticao2 = 6
raiz_repet2 = newton.newton_tolerancia(a2, b2, x2_0, f2, f2_linha, f2_linha_linha, repeticao2)

if raiz_repet2 == None:
    print("Erro ao calcular a raiz (com repetição).")
else:
    print("Raiz encontrada em newton (com 5 repetições):", raiz_repet)
'''