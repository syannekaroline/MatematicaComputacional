
import numpy as np
import math
from numpy.linalg import solve
import matplotlib.pyplot as plt
import pandas as pd


def plotar_grafico(funcao, intervalo_x,pontos=[],label=""):
    """Plota o gráfico de uma função em determina intervalo.\n
    Parâmetros:\n
    função = função a ser plotada. ex :lambda x: np.sin(x).zn
     Intervalo_x =  Intervalo a ser considerado. ex: (-np.pi, np.pi) """
    x = np.linspace(intervalo_x[0], intervalo_x[1], 1000)  # Gera 100 pontos igualmente espaçados no intervalo x
    y = funcao(x)  # Avalia a função para cada valor de x
    
    pontosDestaquey=funcao(pontos)
    plt.plot(x, y,label=label)  # Plota o gráfico
    
    # Configurações adicionais (opcional)
    plt.xlabel('x')
    plt.ylabel('y')
    if len(pontos) :
        plt.plot(pontos, pontosDestaquey,'ro')# plota como pontos 
    plt.title('Gráfico da função')
    
    plt.grid(True)  # Adiciona linhas de grade ao gráfico
    plt.legend()
    plt.show()  # Mostra o gráfico
# # Exemplo de uso:
# def minha_funcao(x):
#     return np.sin(x)  # Exemplo de função (seno)

# intervalo = (-np.pi, np.pi)  # Exemplo de intervalo de x (-pi a pi)

# plotar_grafico(minha_funcao, intervalo)



############ Trapézio

def trapezio(f,a,b):
  """Função que calcula a regra do trapézio/ integral de uma função f no intervalo [a,b]."""
  h = b - a
  b = (f(a) + f(b))/2
  y = b*h 
  return y

# a = inicio, b = fim, m = iteração
def trapezioR(f, LimInferior, LimSuperior, N_Iteracoes):
  """Função que calcula a regra dos trapézios/ Integral de uma função f no intervalo recebido por parâmetro.\n
  Parâmetros:\n
  f -> Função pro calculo da integral.\n
  LimInferior -> limite inferior da integral\n
  LimSuperior -> limite superior da integral.\n
  N_Interações -> número de iterações."""

  H = LimSuperior-LimInferior
  h = H/N_Iteracoes
  sum = f(LimInferior)+f(LimSuperior)
  sum_aux= 0
  for i in range(1, N_Iteracoes):
    sum_aux+=f(LimInferior+i*h)
  sum += 2*sum_aux
  sum*=h/2
  return sum

def GetIntegral(f, limInf, LimSup, N_pontos):
  """Função que calcula a integral em pontos igualmente espaçados.\n
  Parâmetros:\n
  f -> função pro calculo da integral.\n
  limInf -> limite inferior pro calculo da integral.\n
  limSup -> limite superior pro calculo da integral.\n
  N_pontos -> Número de pontos entre o intervalo.\n
  Retorna uma lista com os valores da integral pros pontos x.\n
  """

  p = 1e-10
  x = np.linspace(limInf, LimSup, N_pontos)
  result = []
  for e in x:
    result.append(trapezioR(f, e, e+p, 10000))

  return result

def simpsonR(f,x):
  n = len(x)
  soma = f(x[0]) + f(x[n-1])
  for i in range(1,n-1):
    if (i % 2 == 1):
      soma = soma + 4*f(x[i])
    else:
      soma = soma + 2*f(x[i])   
  
  h = (x[1]-x[0])/3
  y = soma*h
  return y