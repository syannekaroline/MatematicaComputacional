import numpy as np
import math
from numpy.linalg import solve
import matplotlib.pyplot as plt
import pandas as pd


class MQ:
  def __init__(self):
    self.alfas = []

  def fit_exp(self, x, y,GExp=[lambda x:1, lambda x:x],printValues=False):
    self.alfas=[]
    self.Gexp=GExp
    z = np.log(y)# calcula o vetor z ln(y)
    # linearização
    self.fit(x, z, self.Gexp) # calcula os valores de alfa com vetor z g1=1 e g2 = x
    self.alfas[0] = math.e**self.alfas[0] # calcula o a1

    if printValues:
      print("Valores do sistema linear Criado:")
      print(f"Alfas: {self.alfas}")

    self.alfas[1] = -self.alfas[1] # calcula o a2

  def fit_hip(self, x, y,Ghip,printValues=False):
    self.alfas = []
    self.Ghip= Ghip
    z = 1/y
    self.fit(x,z,self.Ghip)

    if printValues:
      print("Valores do sistema linear Criado:")
      print(f"Alfas: {self.alfas}")

  def fit(self,x,y,G,printValues=False):
    """método que calcula os valores deo vetor de alfas.\n
      Parâmetros:\n
      x= vetor de valores de xi tabelados\n
      y= vetor de valores de yi tabelados\n
      G= Vetor com as n funções g1(x),...gn(x), ex: [lambda x:1, lambda x:x,lambda x:x**2].\n\n 
      
      Retorno:\n
      calcula os valores de alfas
      printa os valores dos alfas calculados."""
    self.G=G
    A=[]
    B=[]
    j=0
    for g_lin in G:
      b=0
      for i in range(0,len(x)):
        b+=g_lin(x[i])*y[i]
      B.append(b)
      A.append([])
      for g_col in G:
        a=0
        for i in range(0,len(x)):
          a+=g_lin(x[i])*g_col(x[i])
        A[j].append(a)
      j+=1

    mat = np.append(A, np.array([B]).T,axis=1)
    #Valores do sistema linear Criado.
    self.alfas = solve(A, B)
    
    if printValues:
      print("Valores do sistema linear Criado:")
      print('A: ', A)
      print('B: ', B)
      print('Matriz:\n', mat)
      print(f"Alfas: {self.alfas}")

  def calc(self, x):
    """Calcula o somatório do valor de x aplicado em cada função vo vetor de funções g."""
    s = 0
    # print(self.alfas)
    for i in range(0,len(self.G)):
      s+=self.alfas[i]*self.G[i](x)
    return s
  
  def calc_exp(self, x):
    """retorna o valor da função phi no ponto x para casos não lineares."""
    # calculo da phi pra um ponto x
    return self.alfas[0]*(math.e**(-self.alfas[1]*x))
  
  def plotPontos(self,x,y):
    """Método que plota o gráfico dos pontos tabelados"""
    plt.plot(x, y,'ro')# plota como pontos
    plt.title('Gráfico dos pontos tabelados')

    plt.grid()
    plt.show()

  def PrintAjusteCurva(self,x,y,Linear=True,NaoLinear=False):
    """Método que mostra o gráfico do ajuste de curva.Os alfas já devem ter sido calculados com o método fit."""
    x_line = np.linspace(min(x)-0.0001, max(x)+0.0001, 100)

    if Linear:
      self.fit(x,y,self.G)
      y_line = list(map(lambda x: self.calc(x), x_line))
      plt.plot(x_line,y_line,'g-',label= 'Função linear')
    plt.title('Gráfico Ajuste de Curva')
    if NaoLinear:
      self.fit_exp(x,y,self.Gexp)
      y_nlinear = list(map(lambda x: self.calc_exp(x), x_line))
      plt.plot(x_line,y_nlinear,'b-',label= 'Função Não linear')
    plt.plot(x, y,'ro')# plota como pontos 
    plt.legend()
    plt.grid()
    plt.show()


def MinimoQuadrado(xi, yi):
  """Função que Calcula os valores do vetor de alfas com o mínimo Quadrado.\n
      Parâmetros:\n
      xi= vetor de valores de xi tabelados\n
      yi= vetor de valores de yi tabelados\n\n
      
      Retorno:\n
      Vetor a com os valores calculados 'alfas' por meio da resolução do sistema linear."""
  
  V = np.array([xi**2,xi**1,xi**0]).transpose()
  a = ((np.linalg.inv((V.transpose()).dot(V))).dot(V.transpose())).dot(yi)
    
  return a