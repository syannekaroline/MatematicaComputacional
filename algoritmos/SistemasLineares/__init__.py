import numpy as np
import pandas as pd
import math

def precisao_maquina():
    """Função que calcula a precisão da máquina com referência igual a 1"""
    A=1
    S=2

    while(S>1):
        A=A/2
        S=1+A
    prec=2*A

    return prec
# Resolve o sistema triangular superior.
def SistemaTriangularSuperior(Ax,b):
  """Função que resolve um sistema linear triangular superior do tipo  𝐴𝑥 = b que recebe como parâmetro """
  n = len(b) #tamanho do vetor b
  x= [b[i]/Ax[i][i] if i == 0 else None for i in range(0,len(b))]

  x[n-1] = b[n-1]/Ax[n-1][n-1]
  iter = 0
  for i in list(range(n-1,0,-1)):
    iter+=1
    s = 0
    for j in list(range(i+1,n+1)):
      s = s + Ax[i-1][j-1]*x[j-1]

    x[i-1] = (b[i-1]-s)/(Ax[i-1][i-1])

  return [x,iter]

def EliminacaoDeGauss(A,b):
  """Função que resolve um sistema linear do tipo Ax = b que recebe como parâmetro
     Return : retorna o vetor x resultante"""
  
  # ELIMINAÇÃO DE GAUSS
  n = len(b)

  # Calculo dos pivos.
  for k in range(1,n+1):
    # PIVOTEAMENTO PARCIAL
    for i in range(k+1, len(A)+1):
      if (abs(A[i-1][k-1]) > abs(A[k-1][k-1])):
        [A[k-1], A[i-1]] = [A[i-1], A[k-1]]
        [b[k-1], b[i-1]] = [b[i-1], b[k-1]]

    # Calculo dos multiplicadores.
    for i in list(range(k+1,n+1)):
      m = A[i-1][k-1]/A[k-1][k-1]
      A[i-1][k-1] = 0
      
      # Atualizar demais valores da linha
      for j in list(range(k+1,n+1)):
        A[i-1][j-1] = A[i-1][j-1]-m*A[k-1][j-1]
      b[i-1] = b[i-1] - m*b[k-1]

  # print("depois da eliminação\n Ax =  ",Ax2,"\nb = ",b2)
  x = SistemaTriangularSuperior(A,b)
  return(x)

############################# LU
def formata_matriz(M):
  """Função que printa uma matriz formatando-a"""
  m = len(M) # número de linhas
  n = len(M[0]) # número de colunas
  s = ""
  for i in range(m):
      for j in range(n):
          s += "%9.3f " % M[i][j]
      s +=  "\n"
  return s

# Resolve o sistema triangular inferior.
def SistemaTriangularInferior(Ax,b):
  """Função que resolve um sistema triangular inferior"""
  n = len(b)
  
  y= [b[i]/Ax[i][i] if i == 0 else None for i in range(0,len(b))]
  iter = 0 
  for i in list(range(1,n+1,1)):
    iter+=1
    s = 0
    for j in list(range(1,i,1)):
      s = s + Ax[i-1][j-1]*y[j-1]

    y[i-1] = b[i-1] - s

  return y,iter

def LU_PivParc(A,b):
  """Função que resolve um sistema linear do tipo Ax = b usando o método de Fatoração LU com pivoteamento parcial 
     A = matriz de coeficientes
     b = vetor b resultante
     Retorna um vetor x calculado"""
  n = len(A)
  p=[0]*n
  

  ###### pivoteamento parcial 
  p = list(range(1,n+1)) #"matriz permutação"

  for k in range(1,n+1):
    pv = abs(A[k-1][k-1])
    Lpivo = k

    for i in range(k+1,n+1):
        if abs(A[i-1][k-1])> pv :
          pv = abs(A[i-1][k-1])
          Lpivo = i
  
    if pv == 0: 
      return None #matriz singular
      

    if Lpivo != k : # se for diferente então tem que realizar a permutação
      [p[k-1],p[Lpivo-1]] = [p[Lpivo-1],p[k-1]] # recurso guanabaristico
    
      for j in range(1,n+1):
          [A[k-1][j-1],A[Lpivo-1][j-1]] = [A[Lpivo-1][j-1],A[k-1][j-1]] 

  # resolução dos sistemas triangulares
  # Calculo dos pivos.
  for k in range(1,n+1):
    # Calculo dos multiplicadores.
    for i in range(k+1,n+1):
      m = A[i-1][k-1]/A[k-1][k-1]
      A[i-1][k-1] = m
      # Atualizar demais valores da linha
      for j in range(k+1,n+1,1):
        A[i-1][j-1] = A[i-1][j-1]-m*A[k-1][j-1]
  ### multiplicação da b pela "matriz permutação"
  c=[None for _ in range(0,len(b))]
  for i in range(1,n+1):
    Lpivo = p[i-1]
    c[i-1]=b[Lpivo-1]

  # resolução dos sistemas 
  y = SistemaTriangularInferior(A,c)
  x = SistemaTriangularSuperior(A,y[0])
  x[1] = y[1]+x[1]

  return x


#################################### gauss-jacobi
def TesteConvergencia(MatrizA):
    """Função que realiza teste de convergência pra uma matriz A
        Retorna True caso a seja convergente e False caso contrário"""
    Alfas=list()

    for i in range(len(MatrizA)):
        s=0
        for j in range(len(MatrizA)):
            if j!=i:
                s+=MatrizA[i][j]

        Alfas.append(s/MatrizA[i][i])
    # print(Alfas)
    # print(max(Alfas))

    if max(Alfas) < 1:
        return True
    else:
        return False
def criterioParada(x,xk,precisao=precisao_maquina()):
    """Função que compara x com x-1 verificando a precisão do método como um critério de parada"""
    soma = 0
    zip_object = zip(x, xk) # une as informações de duas variáveis
    for list1_i, list2_i in zip_object:
        soma = soma + math.fabs(list1_i-list2_i)

    if (soma < precisao):
        return True
    else:
        return False   
            
def GaussJacobi(MatrizA,b,max_iteracoes=300,precisao=precisao_maquina()):
    """Função que resolve um sistema linear do tipo Ax = b através do método iterativo de Gauss-Jacobi 
    Parâmetros:
        MatrizA = matriz de coeficientes do sistema linear
        b = vetor b
        max_iteracoes = npumero máximo de iterações
        precisao = precisão do erro
        
        retorno: tupla com
      vetor x resultante e com o número de iterações"""
    n= len(b) #tamanho de do vetor base

    X=b.copy() # copiando b pra x como chute inicial
    solucao = True
    # gerar chute inicial
    for i in list(range(1,n+1)): # percorre cada elemento de x de 1 até n
        # dividir pelo elemento da diagonal principal
        if math.fabs(MatrizA[i-1][i-1])> 0 :# verifica se é possível realizar divisão se a diagonal é diferente de zero
            X[i-1] = b[i-1]/MatrizA[i-1][i-1]
        else:
            solucao = False # não se pode calcular o chute inicial
            break
    if solucao and TesteConvergencia(MatrizA):
        # print("Iteração 0")
        # print("x = ",X)

        xk = X.copy()

        iter = 0
        
        # realiza o calculo de uma função iteração
        while (iter < max_iteracoes): # início das iterações
            iter = iter + 1
            for i in list(range(1,n+1)):
                s = 0

                #realiza o somatório
                for j in list(range(1,n+1)):
                    if ((i-1) != (j-1)):
                        s = s + MatrizA[i-1][j-1]*X[j-1] # somando os termos que não são da diagonal

                xk[i-1] = (1/MatrizA[i-1][i-1])*(b[i-1]-s) # equivale a 1/a(ii)*(bi - somatório de aij*xj)
                
            # print("Iteração: ",iter)
            # print("xk = ",xk)

            #verifica o critério de parada ->  O processo é repetido até ue x^k e x^k-1 eestejam suficientemente próximos
            if criterioParada(X,xk,precisao):
                X = xk.copy()
                break    
            X = xk.copy()
      
        return X,iter
    else:
        return None,None


def GaussSeidel(MatrizA,b,max_iteracoes=300,precisao=precisao_maquina()):
    """Função que resolve um sistema linear do tipo Ax = b através do método iterativo de Gauss-Seidel
      Parâmetros:
      MatrizA = matriz de coeficientes do sistema linear
      b = vetor b
      max_iteracoes = npumero máximo de iterações
      precisao = precisão do erro
      
      retorno: tupla com
      vetor x resultante e com o número de iterações """
    n= len(b) #tamanho de do vetor base

    X=b.copy() # copiando b pra x como chute inicial
    solucao = True
    # gerar chute inicial
    for i in list(range(1,n+1)): # percorre cada elemento de x de 1 até n
        # dividir pelo elemento da diagonal principal
        if math.fabs(MatrizA[i-1][i-1])> 0 :# verifica se é possível realizar divisão se a diagonal é diferente de zero
            X[i-1] = b[i-1]/MatrizA[i-1][i-1]
        else:
            solucao = False # não se pode calcular o chute inicial
            break
    if solucao and TesteConvergencia(MatrizA):
      # print("Iteração 0")
      # print("x = ",X)

      xk = X.copy()

      iter    = 0
      
      # realiza o calculo de uma função iteração
      while (iter < max_iteracoes): # início das iterações
        iter = iter + 1
        for i in list(range(1,n+1)):
          s = 0

          #realiza o somatório
          for j in list(range(1,n+1)):
            if ((i-1) > (j-1)): # se o índice da linha é maior que o da coluna
              s = s + MatrizA[i-1][j-1]*xk[j-1] # usa o xk que tem os valores atualizados
            elif ((i-1) < (j-1)): # se o índice da linha é maior que o da coluna
              s = s + MatrizA[i-1][j-1]*X[j-1] 

          xk[i-1] = (1/MatrizA[i-1][i-1])*(b[i-1]-s) # equivale a 1/a(ii)*(bi - somatório de aij*xj)
      
        # print("Iteração: ",iter)
        # print("xk = ",xk)

        #verifica o critério de parada ->  O processo é repetido até ue x^k e x^k-1 eestejam suficientemente próximos
        if criterioParada(X,xk,precisao):
          X = xk.copy()
          break    
        X = xk.copy()
     
      return X,iter
    else:
       return None,None


################ gerar matriz

def mudancaAleatoria(mat):

    n = mat.shape[0] 
    lin = np.random.randint(n)

    if(np.random.rand()>0.25):
        mat[lin,:] +=np.random.rand()*mat[np.random.randint(n),:] # 
    else:
        mat[lin,:]-=np.random.rand()*mat[np.random.randint(n),:]

def gerarSistema(n,Intervalo_round=[9,15]):
    """Função que gera um sistema linear do tipo Ax = b\n
      Parâmetros :\n
      n = Dimensão do sistema Linear\n
      Intervalo_round = intervalo que contém o número de mudanças Aleatórias que serão realizadas. É proporcional à densidade. 
      """
    mat = np.zeros((n,n+1)) # cria uma matriz zerada de dimensão n
    # print(mat)
    b= np.random.random(n) # gera um b aleatório
    mat[:,n]= b # adiciona esse b como última coluna da matriz
    # print(mat)
    mat[:,:-1] = np.identity(n) # cria uma matriz identidade 
    # print(mat)
    mat * np.random.randint(50,100)
    # print(mat)

    rounds = np.random.randint(Intervalo_round[0],Intervalo_round[1])
    while(rounds>0) :
        mudancaAleatoria(mat)
        rounds-=1
        # print("mudou")
        # print(mat)
    A = mat[:,:-1].tolist()
    x = b.tolist()
    newb = [element[0] for element in mat[: , -1:].tolist()]

    # print("Exemplos: ")
    # print("Matriz: \n",A)
    # print("x = ",x)
    # print("b = ",newb)

    return(A,x,newb)


def GetExemploSistemasLineares(Dimensao_n,it_max=300,precisao=precisao_maquina(),metodos=[1,2,3,4]):
    """FUNÇÃO QUE GERA UM EXEMPLO DE SISTEMA LINEAR DE DIMENSÃO RECBIDA POR PARÂMETRO E RESOLVE POR MÉTODOS DIRETOS E ITERATIVOS COMPARANDO OS RESULTADOS\n
        Parâmetros\n
        Dimensao_n = Dimensão da matriz de exemplo\n
        it_max : número máximo de iterações pros métodos iterativos\n
        precisao: precisão a ser utilizada nos métodos iterativos\n
        metodos : lista com os números dos métodos a serem utilizados [1(Eliminação de Gauss),2(LU com piv parc),3(Gauss-Jacobi),4(Gauss-Seidel)]
        """

    Ax,x,b = gerarSistema(Dimensao_n)
    results={"X":x}
    if 1 in metodos:
          results["Eliminação de Gauss"]=EliminacaoDeGauss(Ax,b)[0]
    if 2 in metodos:
          results["Fatoração LU e Piv Parc:"]=LU_PivParc(Ax,b)[0]
    if 3 in metodos:        
        resultJacobi,iteracoes = GaussJacobi(Ax,b,it_max,precisao)
        results[f"Gauss-Jacobi {iteracoes} iterações:"] = resultJacobi
    if 4 in metodos:  
        resultSeidel,iteracoes = GaussSeidel(Ax,b,it_max,precisao)
        results[f"Gauss-Seidel {iteracoes} iterações:"]=resultSeidel

    print("\nCOMPARAÇÃO RESULTADOS: \n")

#     print("X por eliminação de gauss: ",EliminacaoDeGauss(Ax,b))
#     print("X por Fatoração LU com pivoteamento parcial: ",LU_PivParc(Ax,b))
#     print(f"X por Gauss-Jacobi: {resultJacobi}, com {iteracoes} iterações") 
#     print(f"X por Gauss-Seidel: {resultSeidel}, com {iteracoes2} iterações")

    tabela = pd.DataFrame(results)
    display(tabela)

    return Ax,b,results


def ResolveSistemasLineares(Ax,x,b,it_max=300,precisao=precisao_maquina(),metodos=[1,2,3,4]):
    """RESOLVE POR MÉTODOS DIRETOS E ITERATIVOS COMPARANDO OS RESULTADOS\n
        Parâmetros\n
        Ax = Matriz de coeficientes\n
        b= vetor b
        x= resolução do sistema linear pra comparação com os métodos
        it_max : número máximo de iterações pros métodos iterativos\n
        precisao: precisão a ser utilizada nos métodos iterativos\n
        metodos : lista com os números dos métodos a serem utilizados [1(Eliminação de Gauss),2(LU com piv parc),3(Gauss-Jacobi),4(Gauss-Seidel)]
        """
    results={"X":x}
    if 1 in metodos:
          results["Eliminação de Gauss"]=EliminacaoDeGauss(Ax,b)[0]
    if 2 in metodos:
          results["Fatoração LU e Piv Parc:"]=LU_PivParc(Ax,b)[0]
    if 3 in metodos:        
        resultJacobi,iteracoes = GaussJacobi(Ax,b,it_max,precisao)
        results[f"Gauss-Jacobi {iteracoes} iterações:"] = resultJacobi
    if 4 in metodos:  
        resultSeidel,iteracoes = GaussSeidel(Ax,b,it_max,precisao)
        results[f"Gauss-Seidel {iteracoes} iterações:"]=resultSeidel

    print("\nCOMPARAÇÃO RESULTADOS: \n")

#     print("X por eliminação de gauss: ",EliminacaoDeGauss(Ax,b))
#     print("X por Fatoração LU com pivoteamento parcial: ",LU_PivParc(Ax,b))
#     print(f"X por Gauss-Jacobi: {resultJacobi}, com {iteracoes} iterações") 
#     print(f"X por Gauss-Seidel: {resultSeidel}, com {iteracoes2} iterações")

    tabela = pd.DataFrame(results)
    display(tabela)