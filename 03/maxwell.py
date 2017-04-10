import numpy as np
import matplotlib.pyplot as plt

def odvod(tabela,lamda):
    m=len(tabela)
    n=int(m/2)

    tabela_odvod=tabela

    tabela_odvod[:n]=tabela[n:]

    tabela_odvod[n]=-1*(2*tabela[0]-tabela[1]+lamda*tabela[0]**3)
    tabela_odvod[-1]=-1*(2*tabela[n-1]-tabela[n-2]+lamda*tabela[n-1]**3)

    for i in range(1,n-1):
        tabela_odvod[n+i]=-1*(3*tabela[i]-tabela[i-1]-tabela[i+1]+lamda*tabela[i]**3)

    return tabela_odvod





