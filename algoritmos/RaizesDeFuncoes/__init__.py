
import pandas as pd, numpy as np
import matplotlib.pyplot as plt

def AvaliaSinalFunc(coeficientes,ValoresX=[-1,1],IsIntervalo = True):
    """Função que avalia os sinais de uma função em valores de x ou em dado intervalo
    Parâmetros:
    coeficientes: coeficientes da função
    valoresX: Intervalo ou valores de x que deverão ser considerado na análise da função. Por padrão considera o intervalo de -1 até 1.
    IsIntervalo: por padrão recebe True. Se false siginifica que o parâmetro intervalo se refere aos valores de X que deverão ser considerados na análise."""
    #contruir a função
    func = np.poly1d(coeficientes)
    analise={
        'x': ["f(x)"," sinal"]
    }
    desafio = {'x': ["f(x)"," sinal"]}
    if IsIntervalo :
        aux=list([func(ValoresX[0]), "+" if func(ValoresX[0]) > 0 else "-" ])# variável auxiliar pro desafio -> verificar apenas as trocas de sinal
        desafio[f'{ValoresX[0]}']=aux

        for x in range(ValoresX[0],ValoresX[1]):
            analise[f'{x}'] = list([func(x), "+" if func(x) > 0 else "-" ])
            
            if analise[f'{x}'][1] != aux[1]: # se tiver mudança de sinal
                #guardar o dicionário do desafio
                desafio[f'{x}'] = analise[f'{x}']
                aux=analise[f'{x}']

    else: 
        for x in ValoresX:
            analise[f'{x}'] = list([func(x), "+" if func(x) > 0 else "-" ])

            if analise[f'{x}'][1] != aux[1]: # se tiver mudança de sinal
                #guardar o dicionário do desafio
                desafio[f'{x}'] = analise[f'{x}']
                aux=analise[f'{x}']
    
    tabelaAnalise=pd.DataFrame(analise)
    tabelaDesafio = pd.DataFrame(desafio)
    ##retorno ao usuário
    print("{:#^60}".format("Análise do sinal da função"))
    print(f"\n f(x) = \n{func}\n")

    print("{:#^60}".format("Tabela de análise"))
    print(tabelaAnalise)
    print("{:#^60}".format("Tabela do desafio"))

    print(tabelaDesafio)

def ExercicioAvaliaSinalFunc():
    coeficientes=list(map(int,input("Insira valoresdos coeficientes da função separados por um espaço: ").split()))
    IsIntervalo = True if input("Insira 1 pra escolher a opção de inserir um intervalo ou 2 pra inserir os valores de x pra análise da função: ") == "1" else False
    ValoresX =( list(map(int,input("Insira valores do intervalo da função separados por um espaço: ").split())) 
                if IsIntervalo 
                else list(map(int,input("Insira valores de x separados por um espaço: ").split())) )
    AvaliaSinalFunc(coeficientes,ValoresX,IsIntervalo)



def ExercicioAvaliaGrafico():
    """exercicio de Gerar gráficos pra funções polinomiais"""

    coeficientes=list(map(int,input("Insira valoresdos coeficientes da função separados por um espaço: ").split()))
    valoresX =list(map(int,input("Insira valores do intervalo da função separados por um espaço: ").split()))

    print("########### Função f(x) ###########")
    GeraGraficoFx(coeficientes,valoresX)

def GeraGraficoFx(coeficientes,ValoresX) :
  """Gera gráficos pra funções polinomiais"""
  # Definindo conjunto de 1000 valores de x entre 0 e 3
  x = np.linspace(ValoresX[0],ValoresX[1],1000)
  # definindo vetor y nas mesmas dimensões que o vetor x
  y = np.array(x.shape)
  #definindo y, ou seja, aplicando x na função f(x) = x^3 - 2x^2 + 7
  y = np.poly1d(coeficientes)

  #tamanho da figura
  plt.figure(figsize = (10,4))
  #define X, Y, tipo de marcador(nenhum nesse caso) e cor
  plt.plot(x,y(x), marker = '', color = 'green')     
  #define título
  plt.title(f'Gráfico \n{y}')
  #define nome a mostrar no eixo x
  plt.xlabel('Eixo x')
  #define nome a mostrar no eixo y
  plt.ylabel('Eixo y')
  #faz a plotagem

  """Gera gráficos pra funções polinomiais equivalentes"""
  # Definindo conjunto de 1000 valores de x entre 0 e 3
  x = np.linspace(ValoresX[0],ValoresX[1],1000)
  # definindo vetor y nas mesmas dimensões que o vetor x
  y = np.array(x.shape) 
  coeficientes2=[-coeficientes[0]]
  for i in range(1,len(coeficientes)): coeficientes2.append(0)

  f1 = np.poly1d(coeficientes2)
  f2 = np.poly1d(coeficientes[1:])

  #tamanho da figura
  plt.figure(figsize = (10,4))
  #define X, Y, tipo de marcador(nenhum nesse caso) e cor
  plt.plot(x,f1(x), label =f'\n{f1}' ,marker = '', color = 'green')
  plt.plot(x,f2(x),label =f"\n{f2}" , marker = '', color = 'red')     
  #define título
  plt.title(f'Gráficos Equivalentes: \n h(x) = {f1}  \n g(x) ={f2} ')
  #define nome a mostrar no eixo x
  plt.xlabel('Eixo x')
  #define nome a mostrar no eixo y
  plt.ylabel('Eixo y')
  #faz a plotagem
  
  plt.legend()
  plt.show()

def GeraGraficos(f,g,h,legendas) :
  """Gera gráfico de uma função e de suas equivalentes que recebe como parâmetro"""
  plt.style.use("seaborn")
  x = np.linspace(0,4,1000)
  y = np.array(x.shape)

  #inserindo fução principal - GRÁFICO 1
  

  #configurando gráfico
  plt.figure(figsize = (10,4))
  plt.subplot(2, 1, 1)
  plt.title(f'Gráfico \nf(x)')
  plt.xlabel('Eixo x')
  plt.ylabel('Eixo y')

  #faz a plotagem
  plt.plot(x,f(x),label =legendas[0], marker = '', color = 'green') 
  plt.legend()    

  ########## GRÁFICO 2

  x = np.linspace(0,4,10)
  # definindo vetor y nas mesmas dimensões que o vetor x
  y = np.array(x.shape)
  #INSERINDO FUNÇÕES EQUIVALENTES
  plt.subplot(2, 1, 1)

  #CONFIGURANDO GRÁFICO
  plt.figure(figsize = (10,4))
  plt.title(f'Gráficos Equivalentes: \n h(x) e g(x) ')
  plt.xlabel('Eixo x')
  plt.ylabel('Eixo y')

  #faz a plotagem
  plt.plot(x,h(x), label =legendas[1],marker = '', color = 'green')
  plt.plot(x,g(x),label =legendas[2], marker = '', color = 'red')     
  plt.legend()
  plt.show()

############################################# Resolução ###############################################################################################
#GeraGraficos(lambda x : np.sqrt(x) - 5*np.exp(-x),lambda x: np.sqrt(x),lambda x:  5*np.exp(-x),["np.sqrt(x) - 5*np.exp(-x)","np.sqrt(x)","5*np.exp(-x)"])


def bisseccao(funcao,intervalo,erro):
  """Função que realiza o método da bissecção pra achar a raiz real de uma função.
  Parâmetros:
  função : função pro cálculo ex: função = lambda x:x**3-9*x+3 
  intevalo: lista contendo o intervalo considerado da função. ex: [-1,1]
  erro: critério de parada pra precisão requerida ex:  0.000000001 """

  ai = intervalo[0] 
  bi = intervalo[1]
  i = 0 # variável q armazena o número de iterações realizadas ( bissecções realizadas)
  # verificar se o método se aplica a função
  if funcao(ai)*funcao(bi)< 0:

    while abs(bi-ai) > erro: # testa o critério de parada: enquanto a diferença entre intervalo for maior que o erro -> enquanto f(pi) > precisão
      #calcula o ponto médio
      pi = (ai + bi)/2
      #print("a{}: {};  b{}: {};  p{}: {};".format(i,ai,i,bi,i,pi)) # Mostre todos os passos do algoritmo com os valores de 𝑎𝑖, 𝑏𝑖 e 𝑝i

      # realiza a bissecção no intervalo verificando o sinal das extremidades na função
      if funcao(ai)*funcao(pi)<0: # significa que a raíz pertence a esse intervalo -> está mais a esquerda de bi
          bi = pi
      else: # a raiz está mais a direita de ai -> diminui o intervalo fazendo ai receber o ponto médio calculado
          ai = pi
      i+=1
    return (pi,funcao(pi),i)
  else:
    print("Não existe raíz real neste intervalo!")
#print(bisseccao(lambda x: 31 - ((9.8*x)/13)* (1. - math.exp(-6.0*(13.0/x))), [52, 55], 10**-4))
