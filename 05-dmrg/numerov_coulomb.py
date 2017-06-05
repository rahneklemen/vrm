import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from scipy import optimize


def potencial(x):
    pot=np.zeros(len(x))
    pot[0]=-5000
    for i in range(1,len(x)):
        pot[i]=-1/x[i]
    return pot

def matrika_odvod(vekt,x):
    E=0.5
    return [vekt[1],-2*(E-potencial(x))*vekt[0]]

def poisci_nicle():
    x=np.arange(0,100,0.01)
    vektor0=[1,0]
    resitev = integrate.odeint(matrika_odvod,vektor0,x)
    plt.plot(x,abs(resitev[:,0])**2)
    # plt.plot(resitev[0])
    plt.grid()
    plt.show()
    # print(resitev)

def inetegracija(N,x_max,energija):
    h=x_max/N
    x=np.arange(0,x_max,h)
    k=2*(energija-potencial(x))
    # plt.plot(x,potencial(x))
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.show()
    fi=np.zeros(N+1)
    fi[0]=0
    fi[1]=1
    fi[2]=((2-5/6*k[1]*h**2))/(1+k[2]/12*h**2)*fi[1]
    for i in range(3,N+1):
        fi[i]=((2-5/6*k[i-1]*h**2)*fi[i-1]-(1+k[i-2]/12*h**2)*fi[i-2])/(1+k[i]/12*h**2)
    print(fi)
    normalizacija=sum(fi)
    fi = fi/normalizacija
    plt.plot(x,fi)
    plt.grid()
    plt.show()

inetegracija(100000,15,-0.5)

