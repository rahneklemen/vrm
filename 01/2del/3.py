import numpy as np
import matplotlib.pyplot as plt

def lastne_energije(lamda,n):
    H=np.array([np.zeros(n) for i in range(n)])

    for i in range(n):
        if i-4>-1:
            j=i-4
            H[i][j]=1/4*np.sqrt((j+1)*(j+2)*(j+3)*(j+4))*lamda
        if i-2>-1:
            j=i-2
            H[i][j]=0.5*np.sqrt((j+1)*(j+2))*(2*j+3)*lamda
        j=i
        H[i][j]=i+0.5+3/4*(2*i**2+2*i+1)*lamda

        if i+2<n:
            j=i+2
            H[i][j]=0.5*np.sqrt(j*(j-1))*(2*j-1)*lamda
        if i+4<n:
            j=i+4
            H[i][j]=0.25*np.sqrt(j*(j-1)*(j-2)*(j-3))*lamda


    E,vecorji=np.linalg.eig(H)
    return np.sort(E)[:10]


alfa=[0,0.1,0.25,0.5,0.7,1]
energije=[]
velikost=np.arange(15,250,5)

for j in velikost:
    print(j)
    energije.append(lastne_energije(0.1,j))


plt.plot(velikost,energije,'o-')
plt.show()
