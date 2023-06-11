
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