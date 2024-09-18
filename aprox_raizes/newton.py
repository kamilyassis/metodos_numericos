#baseado na aula (método de newton 
#ou baseado em tangente)

#teste de convergência
def teste_converg_newton(a, b, x_0, f, f_linha, f_linha_linha):

    #bolzano
    if f(a) * f(b) >= 0:
        print("A função não tem um intervalo válido.")
        return None
    
    if not ((f_linha(a) > 0 and f_linha(b) > 0) or (f_linha(a) < 0 and f_linha(b) < 0)):
        
        if not ((f_linha_linha(a) > 0 and f_linha_linha(b) > 0) or (f_linha_linha(a) < 0 and f_linha_linha(b) < 0)):
            print("Não há evidências claras de que a função converge.")
            return None

        return None
    
    if x_0 < a or x_0 > b:
        print("O chute inicial (x_0) não está no intervalo.")
        return None

    return True

#newton com tolerância
def newton_tolerancia(a, b, x_0, f, f_linha, f_linha_linha, tolerancia):
    if not teste_converg_newton(a, b, x_0, f, f_linha, f_linha_linha):
        return None

    x = x_0
    n = 0

    while True:
        x_novo = x - (f(x) / f_linha(x))
        n += 1

        if abs(x_novo - x) < tolerancia:
            break

        x = x_novo

    return x_novo

#newton com repetição
def newton_repeticao(a, b, x_0, f, f_linha, f_linha_linha, repeticao, tolerancia):
    if not teste_converg_newton(a, b, x_0, f, f_linha, f_linha_linha):
        return None

    x = x_0

    while repeticao > 0:
        x_novo = x - (f(x) / f_linha(x))

        #tolerancia de 0 pre-definida par ao caso de achar antes
        #de completar as repetições
        if abs(x_novo - x) <= tolerancia: 
            break

        x = x_novo

        repeticao -= 1

    return x_novo

