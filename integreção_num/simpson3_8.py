f = lambda x: 2 * x + 5

def simpson3_8(x):
        
    if len(x) == 4:

        h = (x[-1] - x[0]) / (len(x) - 1)

        soma = f(x[0]) + 3*(f(x[1]) + f(x[2])) + f(x[-1])

        return soma * h * 3 / 8
    
    else:
        print("Número de pontos inválido. Utilize 4 pontos, ou outro método.")


f = lambda x: 2 * x + 5

x = [1, 2, 3, 4]

print("função associada: 2x + 5")
print("lista de X's: ", x)
print("lista de Y's: ", [f(i) for i in x])
print("Integração por Simpson 3/8 Simples: ", simpson3_8(x))