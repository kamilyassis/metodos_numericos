def simpson1_3(x):
        
    if len(x) == 3:

        h = (x[-1] - x[0]) / (len(x) - 1)

        soma = f(x[0]) + 4*f(x[1]) + f(x[-1])

        return soma * h / 3
    
    else:
        print("Número de pontos inválido. Utilize 3 pontos, ou outro método.")


def simpson1_3_repetido(x):

    if len(x) % 3 == 0:

        n = len(x) - 1
        h = (x[-1] - x[0]) / (n)
        soma = f(x[0]) + f(x[-1])
        
        for i in range(1, n):
            
            if i % 2 == 0:                
                soma += 4 * f(x[i])             
                
            else:
                soma += 2 * f(x[i])
                         
        return soma * h / 3
    
    else:
        print("Número de pontos inválido. Utilize múltiplos de 3, ou outro método.")


f = lambda x: 2 * x + 5

x = [1, 2, 3]
x_2 = [1, 2, 3, 4, 5, 6]

print("função associada: 2x + 5")
print("lista de X's: ", x)
print("lista de Y's: ", [f(i) for i in x])
print("Integração por Simpson 1/3 Simples: ", simpson1_3(x))

print("lista de X's: ", x_2)
print("lista de Y's: ", [f(i) for i in x_2])
print("Integração por Simpson 1/3 Repetido: ", simpson1_3_repetido(x_2))