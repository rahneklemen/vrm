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
    # return np.zeros(len(x))


def integracija(energija):
    x_max=15
    h=10**-4
    # print(h)
    x=np.arange(0,x_max,h)
    k=2*(energija-potencial(x))
    # plt.plot(x,potencial(x))
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.show()
    fi=np.zeros(len(x))
    fi[0]=0
    fi[1]=0.001
    fi[2]=((2-5/6*k[1]*h**2))/(1+k[2]/12*h**2)*fi[1]
    for i in range(3,len(x)):
        fi[i]=((2-5/6*k[i-1]*h**2)*fi[i-1]-(1+k[i-2]/12*h**2)*fi[i-2])/(1+k[i]/12*h**2)
    # normalizacija=sum(fi)
    # fi = fi/normalizacija
    # plt.plot(x,fi)
    # plt.grid()
    # plt.show()
    return fi[-1]

def coulomb_vf(energija):
    x_max=15
    h=10**-4
    # print(h)
    x=np.arange(0,x_max,h)
    k=2*(energija-potencial(x))
    # plt.plot(x,potencial(x))
    # plt.yscale('log')
    # plt.xscale('log')
    # plt.show()
    fi=np.zeros(len(x))
    fi[0]=0
    fi[1]=0.001
    fi[2]=((2-5/6*k[1]*h**2))/(1+k[2]/12*h**2)*fi[1]
    for i in range(3,len(x)):
        fi[i]=((2-5/6*k[i-1]*h**2)*fi[i-1]-(1+k[i-2]/12*h**2)*fi[i-2])/(1+k[i]/12*h**2)
    #todo uredi pravo normalizacijo
    normalizacija=sum(fi**2)
    fi = fi/np.sqrt(normalizacija*x_max)
    norma=sum(fi**2)*x_max
    print(norma)
    return fi,x




a=optimize.newton(integracija,-1)
#a=0.499999996601
# 0.5-a = 3.3990000258832254e-09 --> tocno na 8 decimalk
#r_max=15

valovna_norm,prostor_os = coulomb_vf(a)

plt.plot(prostor_os,valovna_norm)
plt.grid()
plt.show()


