def bissecao_test_convergencia(a, b, f):
    
    #bolzano
    if f(a) * f(b) >= 0:
        print("A função não tem um intervalo válido.")
        return False
    
    return True

def bissecao(a, b, f, tolerancia, max_interacao=10):
    
    if not bissecao_test_convergencia(a, b, f):
        return None

    iteracao = 0
    while iteracao < max_interacao:  
        #ponto médio
        p_1 = (a + b) / 2.0      

        if f(p_1) == 0:
            return p_1
        #se tiver o mesmo sinal que f(a)
        elif f(p_1) * f(a) > 0:
            a = p_1
        #se tiver o mesmo sinal que f(b)
        else:
            b = p_1

        #comprimento do intervalo
        comp_inter = (b - a) / 2.0

        if comp_inter < tolerancia:
            return (a + b) / 2.0
        
        iteracao += 1

    print("Raiz mais próxima após",
          max_interacao, "iterações.")

    raiz = (a + b) / 2.0
    return raiz
