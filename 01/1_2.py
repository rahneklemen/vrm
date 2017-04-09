import numpy as np
import matplotlib.pyplot as plt
import scipy.misc as misc


##explecit AKA skiki s končnim propagatorjem

tau=0.001
h=0.1
lamda=0.0
L=10

x=np.arange(-L,L,h)
pot=1/2*x**2+lamda*x**4



psi=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2))

psi2=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2),dtype=complex)
psi2[0]=0
psi2[-1]=0


for i in range(10):
    psi_temp=psi2
    for j in range(1,len(psi2)-1):
        vsota=0
        for k in range(5):
            vsota+=(-1j*tau)**k/(misc.factorial(k))*(-0.5/(h**2)*(psi_temp[j-1]-2*psi_temp[j]+psi_temp[j+1])+pot[j]*psi_temp[j])**k
        psi2[j]=vsota
    print(i)







plt.plot(x,np.absolute(psi))
plt.plot(x,np.absolute(psi2),'o',label='num1')
plt.legend()
plt.show()






