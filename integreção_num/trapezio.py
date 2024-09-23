'''
Quando usar a integração Númerica?

- A função não é conhecida
OU
- A função é muito díficil
OU
- A função é não-integrável


Pré-requisito Trapezio (aprox por reta):

- A tabela de coordenadas (x, y) em um intervalo [a, b]
OU 
- Uma função f(x) conhecida para criarmos a tabela de coordenadas
'''

class trapezio:

    def __init__(self, f):
        self.f = f

    def trapezio_simples(self, a, b, f):
        return (b-a)*(f(a)+f(b))/2
    
    def trapezio_composto(self, a, b, n, f):
        h = (b-a)/n
        s = 0
        for i in range(1, n):
        
            s += f(a+i*h)
        
        return h*(f(a)+2*s+f(b))/2
    

# Exemplo de uso
f = lambda x: 3*x/10 + 50

t = trapezio(f)

print(t.trapezio_simples(0, 30, f))

#ajustar o composto
print(t.trapezio_composto(0, 30, 1000, f))
