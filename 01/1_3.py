import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc


##implicitna

def normalizacija(valovna,polozaj):
    vsota=0
    for i in range(len(valovna)):
        vsota+=np.absolute(valovna[i])**2
    return vsota/len(valovna)*(polozaj[-1]-polozaj[0])

tau=0.01
h=0.1
lamda=0.5
L=10

x=np.arange(-L,L,h)
pot=1/2*x**2+lamda*x**4


psi=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2))

psi2=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2),dtype=complex)

A=np.array([np.zeros(len(psi),dtype=complex) for i in range(len(psi))],dtype=complex)


H=np.identity(len(A),dtype=complex)


for i in range(len(H)):
    if i==0:
        H[0][0]=1-1j*tau*(1/h**2+pot[i])
        H[0][1]=1j*tau/h**2
    if i+1==len(H):
        H[i][i]=1-1j*tau*(1/h**2+pot[i])
        H[i][i-1] = 1j * tau / h ** 2
    else:
        H[i][i]=1-1j*tau*(1/h**2+pot[i])
        H[i][i-1] = 1j * tau / h ** 2
        H[i][i+1] = 1j * tau / h ** 2


C=np.dot(np.linalg.inv(np.conjugate(H)),H)
# C=np.dot(np.linalg.inv(A),B)


def metoda1(valovna):
    valovna[0] = 0
    valovna[-1] = 0

    psi_temp=valovna
    for k in range(1,len(valovna)-1):
        valovna[k]=psi_temp[k]+tau*(0.5/(h**2)*(psi_temp[k-1]-2*psi_temp[k]+psi_temp[k+1])-pot[k]*psi_temp[k])*1j
    return valovna

def metoda2(valovna,K):
    valovna[0] = 0
    valovna[-1] = 0

    psi_temp = valovna
    for j in range(1, len(valovna) - 1):
        vsota = 1
        for k in range(1,K):
            vsota += (-1j * tau) ** k / (misc.factorial(k)) * (-0.5 / (h ** 2) * ( psi_temp[j - 1] - 2 * psi_temp[j] + psi_temp[j + 1]) + pot[j] * psi_temp[j]) ** k
        valovna[j] = vsota
    return valovna

def metoda3(valovna, matrika):
    return np.dot(matrika,valovna)



valovna1=psi2
valovna2=psi2
valovna3=psi2

vrednost1=[]
vrednost2=[]
vrednost3=[]
for t in range(100):
    valovna1=metoda1(valovna1)
    # valovna2=metoda2(valovna2,10)
    valovna3=metoda3(valovna3,C)

    vrednost1.append(normalizacija(valovna1,x))
    # vrednost2.append(normalizacija(valovna2,x))
    vrednost3.append(normalizacija(valovna3,x))
    print(t)


plt.plot(vrednost1,label=r'eksplecitna Eulerjeva, $\lambda=0.5$')
# plt.plot(vrednost2)
plt.plot(vrednost3,label=r'implicitna, $\lambda =0$')
# plt.ylim([0,10**20])
plt.legend(loc=2)
plt.grid()
# plt.yscale('log')
# plt.xscale('log')
plt.xlabel('čas')
plt.ylabel(r'$<\psi | \psi>$')
plt.ylim([0,5])
# plt.savefig('primerjava1.png')
plt.show()







