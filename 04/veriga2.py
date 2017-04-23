import numpy as np
import matplotlib.pyplot as plt




def stanje(n,T):
    N=10**4
    fi=np.random.rand(n)*2*np.pi
    theta=np.arccos(2*np.random.rand(n)-1)
    rand_st=np.random.rand(N)
    for i in range(N):
        j=np.random.randint(0,n-3)
        delta=2*(np.sin(theta[j])*np.sin(theta[j+1])*np.cos(fi[j]-fi[j+1])+np.cos(theta[j])*np.cos(theta[j+1]))
        # print(delta)
        if rand_st[i]>np.exp(delta/T):
            theta[j+1]=np.pi-theta[j+1]
            fi[j+1]=fi[j+1]+np.pi
    return fi, theta

def korelacija_single(phi,theta):
    phi0=phi[0]
    theta0=theta[0]
    kor=np.zeros(len(phi))
    for i in range(len(phi)):
        # samo z komponenta spina
        kor[i]=np.sin(theta0)*np.sin(theta[i])*np.cos(phi0-phi[i])+np.cos(theta0)*np.cos(theta[i])
    return kor


def korelacija(temperatura):
    M=20
    st_povprecenj=10**2
    korel_dolzina=np.zeros(M)
    for iteracija in range(st_povprecenj):
        a,b=stanje(M,temperatura)
        korel_dolzina+=korelacija_single(a,b)
        print(iteracija)

    return korel_dolzina/st_povprecenj

T1=10
T2=0.01

plt.plot((korelacija(T1)),'o-',label="T1")
# plt.plot((korelacija(T2)),'o-',label='T2')
plt.grid()
plt.legend()
plt.show()



