'''
Perguntas:

é para fazer o metodo de Regula Falsi tbm? (para secante)
a unica exigencia da secante é bolzano e o intervalo mesmo?
é para fazer uma função que derive? (newton)


'''

import bissecao, newton, secante

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

#outras informações
x_0 = a
x_1 = b
tolerancia = 0.001

print('Função: x^3 - 2x - 5, no intervalo [2, 3]')

#bissecao
raiz_b = bissecao.bissecao(a, b, f, tolerancia)

if raiz_b == None:
    print("Erro ao calcular a raiz com método da bisseção.")
else:
    print("Raiz encontrada com bisseção (com tolerância = 0.001):", raiz_b)


#secante
raiz_s, iteracoes_s = secante.secante(a, b, x_0, x_1, f, tolerancia)

if raiz_s == None:
    print("Erro ao calcular a raiz com metodo secante.")
else:
    print("Raiz encontrada com secante (com tolerância = 0.001):", raiz_s)
    print(iteracoes_s, " iterações foram necessárias!")

#newton
#newton com tolerância
raiz_n = newton.newton_tolerancia(a, b, x_0, f, f_linha, f_linha_linha, tolerancia)

if raiz_n == None:
    print("Erro ao calcular a raiz.")
else:
    print("Raiz encontrada em newton (com tolerância = 0.001):", raiz_n)

#newton com repetição
repeticao = 2
raiz_n_repet = newton.newton_repeticao(a, b, x_0, f, f_linha, f_linha_linha, repeticao, tolerancia)

if raiz_n_repet == None:
    print("Erro ao calcular a raiz.")
else:
    print("Raiz encontrada em newton (com", repeticao, "repetições):", raiz_n_repet)
