
# implementação de métodos de refinamento - matemática computacional
import math
import numpy as np
# MÉTODO 1 - MÉTODO DA POSIÇÃO FALSA:


def posicaoFalsa(funcao, intervalo, erro1, erro2,it_max = 10000):
    """Função que realiza o método da posição falsa pra achar aproximação da raiz real de uma função.
    Parâmetros:
    função : função pro cálculo ex: função = lambda x:x**3-9*x+3 
    intevalo: lista contendo o intervalo considerado da função. ex: [-1,1]
    erro: critério de parada pra precisão requerida ex:  0.000000001 """
    ai = intervalo[0]
    bi = intervalo[1]
    x= (ai*funcao(ai) - bi*funcao(bi))/(funcao(bi) - funcao(ai))  # média ponderada
    # variável q armazena o número de iterações realizadas ( bissecções realizadas)
    i = 1

    # verificar se o método se aplica a função
    if funcao(ai)*funcao(bi) < 0:

        while abs(bi-ai) > erro1 and abs(funcao(x)) > erro2 and i < it_max:  # testa o critério de parada: enquanto a diferença entre intervalo for maior que o erro -> enquanto f(pi) > precisão
            # calcula o ponto médio ponderado
            x = (ai*funcao(ai) - bi*funcao(bi))/(funcao(bi) - funcao(ai))  # média ponderada
            # Mostre todos os passos do algoritmo com os valores de 𝑎𝑖, 𝑏𝑖 e 𝑝i
            #print("a{}: {};  b{}: {};  x{}: {};".format(i, ai, i, bi, i, x))

            if abs(funcao(x)) < erro2 :
                return (x, funcao(x), i)
            
            elif funcao(ai)*funcao(x) > 0:
                ai = x
            else:  # a raiz está mais a direita de ai -> diminui o intervalo fazendo ai receber o ponto médio calculado
                bi = x
            i += 1
        return (x, funcao(x), i)
    else:
        print("Não existe raíz real neste intervalo!")

print(posicaoFalsa(lambda x: 31 - ((9.8*x)/13)* (1. - math.exp(-6.0*(13.0/x))), [52, 55], 10**-4,10**-4))
# print(posicaoFalsa(lambda x : math.exp(-x**2) - math.cos(x),[1,2],10**-4))
# MÉTODO DO PONTO FIXO


def pontoFixo(f, phi, x0, e1=0.000001, e2=0.000001, it_max=1000000):
    """Função que calcula a raiz de uma função f recebida por parâmetro pelo método do ponto fixo.
    PArâmetros:
    f -> função 
    phi -> função equivalente tal que phi(X) = X -> veio de f(x)= 0 e depois de isolar x.
    x0 -> aproximação inicial 
    e1 e e2 -> precisões
    it_max -> número de iterações máximas.
    Retorna uma tupla contendo a raiz, o y na raiz e o número de iterções realizadas, respectivamente.
    """
    if (abs(f(x0)) < e1):
        return x0

    x = phi(x0)
    k = 1

    while (abs(f(x)) > e2 and abs(x - x0) > e1 and k < it_max):
        print("x{}: {}; f(x) : {}; ".format(k, x, f(x)))

        x0 = x
        x = phi(x)
        k += 1

    return (x, f(x), k)


# print(pontoFixo(lambda x: (x**3) - 9*x + 3,lambda x: (x**3/9) + (1/3), 0.5, 5*10**-4, 5*10**-4))

# método newton-raphson


def derivada(coeficientesf):
    f = np.poly1d(coeficientesf)
    return f.deriv()

# print(derivada([1,-9,3]))


def newton_raphson(f, fdx, x0, e1=0.000001, e2=0.000001, it_max=100000):
    """Função que calcula a raiz de uma função f polinomial usando o método de newton-raphson
    parâmetros :
    f -> função f(x).
    fdx -> função derivada de f
    x0 -> aproximação inicial
    e1 e e2 -> precisões
    it_max -> número de iterações máximas.
    Retorna uma tupla contendo a raiz, o y na raiz e o número de iterções realizadas, respectivamente.
    """
    if (abs(f(x0)) < e1):
        return x0

    x = x0 - (f(x0)/fdx(x0))
    print("x{}: {}; f(x) : {}; ".format(0, x0, f(x0)))
    k = 1

    while (abs(f(x)) > e2 and abs(x - x0) > e1 and k < it_max):
        # print("x{}: {}; f(x) : {}; ".format(k, x, f(x)))
        x0 = x
        x = x - (f(x)/fdx(x))
        k += 1

    return (x, f(x), k)
# print(newton_raphson(lambda x: x**3 - 9*x +3,lambda x: 2*x - 9,0.5,0.0001,0.0001,11))

# método de secante.


def metodoSecante(f, x0, x1, e1=0.000001, e2=0.000001, it_max=1000000):

    if (abs(f(x0)) < e1):
        return (x0, f(x0), 0)

    if (abs(f(x1)) > e1 or abs(x1 - x0) > e1):
        return (x1, f(x1), 0)

    x2 = x1 - (f(x1) / (f(x1)-f(x0))) * x1-x0
    k = 1
    while (abs(f(x2)) > e1 and abs(x2 - x1) > e2 and k < it_max):
        x2 = x2 - ((f(x1) / (f(x1)-f(x0))) * (x1-x0))
        x0 = x1
        x1 = x2
        k += 1
        # Mostre todos os passos do algoritmo com os valores de 𝑎𝑖, 𝑏𝑖 e 𝑝i
        # print("x{}: {}; f(x) : {}; ".format(k, x2, f(x2)))
    return (x2, f(x2), k)
