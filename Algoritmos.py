import math
import math

def Area_Cicunferencia(raio=1, Prec=2):
    """Função que cálcula a área de um círculo recebendo como parâmetros de entrada o valor do raio (metros) e da precisão de pi
        Dependendo da precisão considerada o resultado será diferente"""

    # decimal.getcontext().prec=Prec#define a precisão do resultado
    pi = float(str(math.pi)[:Prec])
    area = pi*raio**2
    print(f"Considerando pi = {pi} -> Área= {area}")
    return (area)


def precisao_maquina():
    """Função que calcula a precisão da máquina  com reerência de precisão igual a 1"""
    A = 1
    S = 2

    while (S > 1):
        A = A/2
        S = 1+A
    prec = 2*A

    return prec

def somatorio(X=1.0, K=1, N=1):
    """Função pra calcular o somatório de X K-N vezes"""
    S = 0.0
    for i in range(K, N+1):
        S += X
    return (S)


def exercicio01(X=1.0, K=1, N=1):
    """1. Escreva um programa que obtenha os seguintes resultados:
        S = 10000 − **Somatório de X para valores inteiros de 1 até n**"""
    S = 0.0
    for i in range(K, N+1):
        S += X

    result = 10000-S  # aqui representa o valor esperado menos o valor aproximado calculado no for -> ou seja, o erro absoluto do somatório em si

    return (result)


def ErroAbsoluto(exato, aproximado):
    """Cálculo do erro absoluto = módulo da diferença entre o valor exato e o valor aproximado"""
    return math.fabs(exato-aproximado)


def ErroRelativo(exato, aproximado):
    """Função que recebe o valor exato e o valor aproximado de um número e retorna seu erro relativo
        Erro relativo -> Erro absoluto dividido pelo valor exato"""
    try:
        E_relativo = math.fabs(exato-aproximado)/math.fabs(exato)
        return E_relativo

    except ZeroDivisionError:
        return 'divisao impossível -> Sem Erro Relativo'


def precisao_maquina_ref():
    """Função que calcula a precisão da máquina, o número positivo em aritmética de ponto flutuante 𝜀, tal que 1 + 𝜀 >1. recebendo como parâmetro o número de referência da precisão"""
    ref = int(input("Insira o valor de referência da precisão: "))
   # passo 1
    A = 1
    S = ref+A
    # passo 2
    while (S > ref):
        A = A/2
        S = ref+A
    prec = 2*A  # passo 3
    return prec
    # print(f"Precisão da máquina: {prec}")


def SerieDeTaylor(X=1, N=1):
    """Função que calcula o valor da série de taylor recebendo X e N como parâmetro
    Série de taylor: e^x = somatório de X**k/k! N vezes"""
    if X < 0:
        y = -X
        return 1/SerieDeTaylor(y,N)
    result = 0.0
    for k in range(0, N+1):
        SAux = X**k/math.factorial(k)
        # somatório
        result += SAux
    return (result)


def ExercicioSerieTaylor():
    """Exercício pra receber os parâmetros X e N da série de taylor do usuário e mostrar o resultado"""

    print("{:#^60}".format("\nSérie de Taylor\n"))
    X = int(input("Insira o valor de X da série de taylor: "))
    N = int(input("Insira o valor de N da série de taylor: "))
    print(
        f"Para X = {X} e N = {N}, o cálculo da série de taylor é {SerieDeTaylor(X,N)}")


def SerieDeTaylor_NoOverflow(X=1, N=1):
    """Função que calcula a série de Taylor recebendo X e N como parâmetros e evitando a ocorrência de Overflow"""

    if X < 0:
        y = -X
        return 1/SerieDeTaylor_NoOverflow(y)
    result = 0.0
    try:
        for k in range(0, N+1):
            Xk = X**k
            K_factor = math.factorial(k)
            # print(Xk)
            # print(K_factor)
            SAux = Xk/K_factor
            # somatório
            result += SAux
        return (result)
    except:
        print(
            f"\n \033[31mNúmero máximo de interações (valor de N máximo que a máquina foi capaz de calcular) = {k}\033[m")
        print(
            f" Máximo Valor Aproximado para X = {X} e N = {k-2} -> ", SerieDeTaylor_NoOverflow(X, k-2))
        
def ExercicioSerieTaylor_NoOverflow():
    """Exercício pra receber os parâmetros X e N da série de taylor do usuário e mostrar o resultado"""
    print("{:#^60}".format("Série de Taylor - Sem Overflow"))
    X = int(input("Insira o valor de X da série de taylor: "))
    N = int(input("Insira o valor de N da série de taylor: "))
    print(f"Para X = {X} e N = {N}, o cálculo da série de taylor é {SerieDeTaylor_NoOverflow(X,N)}")
    print("#"*75,"\n")
    
def SerieDeTaylorAprox(X,N):
    "Função que calcula a série de taylor. Em caso de overflow o máximo valor que a máquina conseguiu armazenar é retornado"

    if X < 0:
        y = -X
        return 1/SerieDeTaylor(y)
    result = 0.0
    try :
        for k in range(0, N+1):
            SAux = X**k/math.factorial(k)
            # somatório
            result += SAux
        return result
    except:
        print('\n\033[31m ############ OVERFLOW ##################### \033[m \n')
        print(f"Número máximo de iterações (valor de N máximo que a máquina foi capaz de calcular) = {k}")
        aprox = SerieDeTaylor(X, k-2) #valor aproximado
        print(f" Máximo Valor Aproximado para X = {X} e N = {k-2} -> ", aprox)
        return aprox