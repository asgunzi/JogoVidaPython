# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 04:05:27 2020

@author: asgun
"""
import numpy as np
import matplotlib.pyplot as plt


size = 60
iteracoes = 100

def update(arrVal,N):
    arrValUpdate=np.zeros([N,N],dtype = int)
    for i in range(size):
        for j in range(size):
            somaVizinhos = 0
            if i==0 and j ==0:
                #Não tem vizinhos acima nem à esquerda
                somaVizinhos = arrVal[i][j + 1] + arrVal[i + 1][j] + arrVal[i + 1][j + 1]
            elif i==0 and j <N-1:
                #Não tem vizinhos acima
                somaVizinhos = arrVal[i][j - 1] + arrVal[i][j + 1] + arrVal[i + 1][j - 1] + arrVal[i + 1][j] + arrVal[i+ 1][j + 1]
            elif i == 0 and j == N-1: 
                #Não tem vizinhos acima nem à direita
                somaVizinhos = arrVal[i][j - 1] + arrVal[i + 1][j - 1] + arrVal[i + 1][j]
        
            elif  i > 0 and i < N-1 and j == 0:
                #Não tem vizinhos à esquerda
                somaVizinhos = arrVal[i - 1][j] + arrVal[i - 1][j + 1] + arrVal[i][j + 1] + arrVal[i + 1][j] + arrVal[i + 1][j + 1]
            elif i > 0 and i < N-1 and j > 0 and j < N-1:
                #Tem todos os vizinhos
                somaVizinhos = arrVal[i - 1][j - 1] + arrVal[i - 1][j] + arrVal[i - 1] [j+ 1] + arrVal[i][j - 1] + arrVal[i][j + 1] + arrVal[i + 1][j - 1] + arrVal[i + 1][j] + arrVal[i + 1][j + 1]
            elif i > 0 and i < N-1 and j == N-1:  
                #Não tem vizinhos à direita
                somaVizinhos = arrVal[i - 1][j - 1] + arrVal[i - 1][j] + arrVal[i][j - 1] + arrVal[i + 1][j - 1] + arrVal[i + 1][j]
        
        
            elif i ==N-1 and j == 0:
                #Não tem vizinhos abaixo e á esquerda
                somaVizinhos = arrVal[i - 1][j] + arrVal[i - 1][j + 1] + arrVal[i][j + 1]
            elif i == N-1 and j > 0 and j < N-1:
                #'Não tem vizinhos abaixo
                somaVizinhos = arrVal[i - 1][j - 1] + arrVal[i - 1][j] + arrVal[i - 1][j + 1] + arrVal[i][j - 1] + arrVal[i][j + 1]
            elif i == N -1 and j == N-1:
                #Não tem vizinhos abaixo e à direita
                somaVizinhos = arrVal[i - 1][j - 1] + arrVal[i - 1][j]+ arrVal[i][j - 1]

            #Qualquer célula viva com menos de dois vizinhos vivos morre de solidão.
            if arrVal[i][j] == 1 and somaVizinhos < 2:
                arrValUpdate[i][j] = 0
            
            #Qualquer célula viva com mais de três vizinhos vivos morre de superpopulação.
            if arrVal[i][j] == 1 and somaVizinhos > 3:
                arrValUpdate[i][j] = 0
            
            #Qualquer célula morta com exatamente três vizinhos vivos se torna uma célula viva.
            if arrVal[i][j] == 0 and somaVizinhos == 3:
                arrValUpdate[i][j] = 1
            
            
            #Qualquer célula viva com dois ou três vizinhos vivos continua no mesmo estado para a próxima geração.
            if arrVal[i][j] ==1 and (somaVizinhos== 2 or somaVizinhos== 3):
                arrValUpdate[i][j] = 1
            
    return(arrValUpdate)

#Inicializa
arrVal = np.random.randint(0,2,[size,size])


fig, ax = plt.subplots()
plt.axis(False)

for iter in range(iteracoes):
    arrVal = update(arrVal,size)

    im = ax.imshow(arrVal, cmap='Greys', interpolation='none')
    plt.show()
    #Mudar para a pasta de destino das imagens
    nameFig = 'C:\\Analytics\\Conway\\' + str(iter).zfill(3) + '.png'
    plt.savefig(nameFig)
