import math,decimal

################################## EXERCÍCIO PRÁTICO 01 #####################################
def Area_Cicunferencia(raio=1,PrecPi=2):
    """Função que cálcula a área de um círculo recebendo como parâmetros de entrada o valor do raio (metros) e da precisão de pi
        Dependendo da precisão considerada o resultado será diferente"""
    decimal.getcontext().prec =PrecPi#define a precisão de pi
    pi=decimal.Decimal(math.pi)
    print(f"Pi usado = {pi}")
    area=pi*raio**2
    print(f"Area = {area} m^2")
'''
Area_Cicunferencia(100,3)
Area_Cicunferencia(100,5)
Area_Cicunferencia(100,10)
'''
def precisao_maquina():
    """Função que calcula a precisão da máquina com referência igual a 1"""
    A=1
    S=2

    while(S>1):
        A=A/2
        S=1+A
    prec=2*A

    return prec
#print(f"Precisão da máquina: {precisao_maquina()}")

def somatorio(X=1.0,K=1,N=1):
    """Função pra calcular o somatório de X K-N vezes"""
    S=0.0
    for i in range(K,N+1) :
        S+=X
    return(S)

def exercicio01(X=1.0,K=1,N=1):

    S=0.0
    for i in range(K,N+1) :
        S+=X

    result=10000-S # aqui representa o valor esperado menos o valor aproximado calculado no for -> ou seja, o erro absoluto do somatório em si

    return(result)

def ErroAbsoluto(exato,aproximado):
    """Calculo do erro absoluto = módulo da diferença entre o valor exato e o valor aproximado"""
    return math.fabs(exato-aproximado)

def ErroRelativo(exato,aproximado):
    """Função que recebe o valor exato e o valor aproximado de um número e retorna seu erro relativo
        Erro relativo -> Erro absoluto dividido pelo valor exato"""
    try:
        E_relativo=math.fabs(exato-aproximado)/math.fabs(exato)
        return E_relativo

    except ZeroDivisionError:
       return 'divisao impossível -> Sem Erro Relativo'

def precisao_maquina_ref():
    """Função que calcula a precisão da máquina, o número positivo em aritmética de ponto flutuante 𝜀, tal que 1 + 𝜀 >1. recebendo como parâmetro o número de referência da precisão"""
    ref=int(input("Insira o valor de referência da precisão: "))
   #passo 1
    A=1
    S=ref+A
    #passo 2
    while(S>ref):
        A=A/2
        S=ref+A
    prec=2*A #passo 3
    return prec
    #print(f"Precisão da máquina: {prec}")

def SerieDeTaylor(X=1,N=1):
    """Função que calcula a série de taylor (e^x).\nParâmetros:\nX= valor de x espoente do número de euler\nN = o limite superior do cálculo da série de taylor\nRetorna o resultado da série de taylor"""

    if X <0:
        y=-X
        return 1/math.exp(y)
    result=0.0
    for k in range(0,N+1):
        SAux=X**k/math.factorial(k)
        #somatório
        result+=SAux
    return(result)

def SerieDeTaylor_NoOverflow(X=1,N=1):
    """Exercício que calcula a série de taylor"""

    if X <0:
        y=-X
        return 1/math.exp(y)
    result=0.0
    try:
        for k in range(0,N+1):
            Xk = X**k
            K_factor=math.factorial(k)
            #print(Xk)
            #print(K_factor)
            SAux=Xk/K_factor
            #somatório
            result+=SAux
        return(result)
    except:
        print(f"\n \033[31mNúmero máximo de iterações (valor de N máximo que a máquina foi capaz de calcular) = {k}\033[m")
        result=SerieDeTaylor_NoOverflow(X,k-2)
        print(f" Máximo Valor Aproximado para X = {X} e N = {k-2} -> ",result)
        return result

def ExercicioSerieTaylor():
    """Exercício que calcula a série de taylor recebendo o valor de x e N do usuário."""

    print("{:#^60}".format("\nSérie de Taylor\n"))
    X=int(input("Insira o valor de X da série de taylor: "))
    N = int(input("Insira o valor de N da série de taylor: "))
    print(f"Para X = {X} e N = {N}, o cálculo da série de taylor é {SerieDeTaylor(X,N)}")