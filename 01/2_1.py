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

psi2=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-(x-3)**2/2),dtype=complex)

A=np.array([np.zeros(len(psi),dtype=complex) for i in range(len(psi))],dtype=complex)

psi_0=psi2

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

cas=[]
norma=[]
for t in range(500):
    cas.append(t)
    psi2=metoda3(psi2,C)
    norma.append(normalizacija(psi2,x))

    if t==100:
        psi_1=psi2
    if t==250:
        psi_2=psi2


plt.title(r'$\lambda=0$')
plt.plot(x,np.absolute(psi_0),label='t=0')
plt.plot(x,np.absolute(psi_1),label='t=100')
plt.plot(x,np.absolute(psi_2),label='t=250')
# plt.plot(x,np.absolute(psi),label='')
plt.grid()
plt.legend()
plt.ylabel(r'$<\psi | \psi>$')
plt.savefig('casovni_razvoj_izmika.png')
plt.show()

plt.plot(cas,norma)
plt.ylim([0,2])
plt.grid()
plt.xlabel('čas')
plt.ylabel(r'$<\psi | \psi>$')
plt.savefig('ohranjanje_delcev.png')
plt.show()



