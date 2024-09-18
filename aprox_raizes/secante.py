def teste_converg_secante(a, b, x_0, x_1, f):

    #bolzano
    if f(a) * f(b) >= 0:
        print("A função não tem um intervalo válido")
        return False
    
    elif x_0 == x_1:
        print("Os pontos iniciais são iguais. Não há inclinação")
        return False

    return True

#secante com tolerância
def secante(a, b, x_0, x_1, f, tolerancia):

    if not teste_converg_secante(a, b, x_0, x_1, f):
        return None
    
    x = x_0
    x_anterior = x_1
    n = 0
    
    while (abs(f(x)) and abs(x - x_anterior)) > tolerancia:
        try:
            x_novo = x - f(x) * (x - x_anterior) / (f(x) - f(x_anterior))
        except ZeroDivisionError:
            print("Uma divisão por zero interrompeu a execução.")
            return None

        x_anterior = x
        x = x_novo
        n += 1

    return x, n


