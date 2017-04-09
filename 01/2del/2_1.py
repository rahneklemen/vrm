import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh


##za sortiranje lastnih vrednosti in pripadajocih vektorjev:
# import numpy as np
# import numpy.linalg as linalg
#
# A = np.random.random((3,3))
# eigenValues,eigenVectors = linalg.eig(A)
#
# idx = eigenValues.argsort()[::-1]
# eigenValues = eigenValues[idx]
# eigenVectors = eigenVectors[:,idx]
##

##n vedno vecji od 5
def lastne_energije1(lamda,n):
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
    # idx = E.argsort()[::-1]
    return np.sort(E)

def lastne_energije2(lamda,n):
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


    E,vecorji=eigsh(H,k=n-1,which='SM')
    # print('zacetek----\n',eigsh(H),'\nkonec')

    # idx = E.argsort()[::-1]
    # print(E,idx)
    return np.sort(E)


n=20
alfa=np.arange(0,1,0.05)
energija_min1=[]
energija_min2=[]
for i in alfa:
    energija_min1.append(lastne_energije1(i,n))
    energija_min2.append(lastne_energije2(i,n))

plt.plot(alfa,energija_min1,'-')
plt.plot(alfa,energija_min2,'o')
plt.ylim(ymax=11)
plt.show()



