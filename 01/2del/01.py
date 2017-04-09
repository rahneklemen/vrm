import numpy as np
import matplotlib.pyplot as plt

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
    return np.sort(E)

n=15

alfa=np.arange(0,1,0.01)
energija_min=[]
for i in alfa:
    energija_min.append(lastne_energije(i,n))

plt.plot(alfa,energija_min)
plt.ylim(ymax=26)
plt.grid()
plt.title(r'najnižje lastne energije z dodatnim potencialom $\lambda x^4$')

plt.ylabel(r'$E_N$')
plt.xlabel(r'$\lambda$')
# plt.savefig('najnizje_energije.png')
plt.show()



