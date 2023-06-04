import numpy as np
import pandas as pd
import sympy as sym
from exercicioPratico01 import precisao_maquina
from SistemasLineares import EliminacaoDeGauss

def getMatrizJacobiana(F,n_variaveis):
    """Função que gera a matriz jacobiana de uma matriz de funções que recebe como parâmetro\n
    Parâmetros:\n
    F = matriz principal da qual se quer gerar a jacobiana\n
    N_variaveis = número de variáveis\n
    Retorno:\n Matriz Jaconiana de F"""

    # pega a dimensao da matriz
    n = len(F)
    m = len(F[0])
    # gera as variáveis
    symbols = sym.symbols(f"x1:{n_variaveis+1}")
    matrizJacobiana=list()# vriável que guardará o retorno da função

    # print(n,m)
    # print(symbols)
    # percorre a matriz F
    for i in range(n):
        listaux=list()
        for j in range(m):
            f = F[i][j]
        
            # print(f"Função= {f}")

            derivadas_list =list()
            #calculo da derivada pra cada variável
            for variable in symbols:
                #calculo da derivada parcial
                derivative = f.diff(variable)
                # print(f"Derivada de {variable} :{derivative}")
                derivadas_list.append(derivative)
              
            
            listaux.append(derivadas_list)
        # print("Lista de derivadas parciais = ",listaux)
        matrizJacobiana.append(listaux)

    return matrizJacobiana

def Newton_N_Lineares(F,J,x0,e1=precisao_maquina(),e2=precisao_maquina(),it_max=10000,nw_modificado=False):
    """Função que resolve um sistema não linear\n
        Parâmetros\n
        F = F(X) contendo as funções do sistema
        J = Matriz Jacobiana F(X) contendo as derivadas parciais de F(x)\n
        e1 e e2 = precisões de erro, o defaut é a precisão da máquina\n
        it_max = número de iterações máximas\n
        nw_moficado = boleano que representa de o método deve ser o tipo newton modificado ou não
        RETORNOS:\n
        tupla contendo o vetor x resultante e o número de iterações que foram realizadas respectivamente\n"""  
    verifica_precisao =np.max(F(x0)) 

    if verifica_precisao < e1:
        return(x0,0)
    xk=x0
    # print("Chute Inicial : ",F(x0))
    k=0

    while(verifica_precisao>e2 and k<it_max):
        # print(f"\n{k}\n")
        # print(f"J(x{k}) = ",J(xk).tolist())
        # print(f"-F(x{k})",(-F(xk)[0]).tolist()[0])

        s= np.matrix(EliminacaoDeGauss(J(x0).tolist(),(-F(xk)[0]).tolist()[0])[0]) if nw_modificado else np.matrix(EliminacaoDeGauss(J(xk).tolist(),(-F(xk)[0]).tolist()[0])[0])

        # print("s = ",s)
        xk=np.matrix(xk)
        xkp1=xk+s # calcula 0 x^k+1
        # print(f"x{k+1} = {xkp1}")

        if abs(np.max(np.abs(xkp1-xk))) < e2:
            # print("menor")
            return xkp1.tolist()[0],k
        
        # print(f"{np.max(np.abs(xkp1-xk))}> e2")
        k+=1
        xk=xkp1.tolist()[0] # atualiza o xk pra ser xk+1
        # print(xk)
        verifica_precisao=np.max(F(xk))

    return xk,k