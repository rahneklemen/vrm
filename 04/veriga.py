import numpy as np
import matplotlib.pyplot as plt




def stanje(n):
    T=1
    N=10**5
    fi=np.random.rand(n)*2*np.pi
    theta=np.arccos(2*np.random.rand(n)-1)
    rand_st=np.random.rand(N)
    for i in range(N):
        j=np.random.randint(0,n-3)
        delta=-2*(np.sin(theta[j])*np.sin(theta[j+1])*np.cos(fi[j]-fi[j+1])+np.cos(theta[j])*np.cos(theta[j+1]))
        delta+=-2*(np.sin(theta[j+2])*np.sin(theta[j+3])*np.cos(fi[j+2]-fi[j+3])+np.cos(theta[j+2])*np.cos(theta[j+3]))
        # print(delta)
        if rand_st[i]>np.exp(delta/T):
            theta[j+1]=np.pi-theta[j+1]
            fi[j+1]=fi[j+1]+np.pi
            theta[j+2]=np.pi-theta[j+2]
            fi[j+2]=fi[j+2]+np.pi
    return fi, theta

def korelacija_single(phi,theta):
    phi0=phi[0]
    theta0=theta[0]
    kor=np.zeros(len(phi))
    for i in range(len(phi)):
        kor[i]=np.sin(theta0)*np.sin(theta[i])*np.cos(phi0-phi[i])+np.cos(theta0)*np.cos(theta[i])
    return kor


def korelacija():
    M=30
    korel_dolzina=np.zeros(M)
    for iteracija in range(10**2):
        a,b=stanje(M)
        korel_dolzina+=korelacija_single(a,b)
        print(iteracija)

    return korel_dolzina

plt.plot(korelacija())
plt.grid()
plt.show()



