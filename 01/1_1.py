import numpy as np
import matplotlib.pyplot as plt


def dormalizacija(valovna,koordinata):
    vsota=0
    for i in range(len(valovna)):
        vsota+=np.absolute(valovna[i])

    return vsota/len(koordinata)/(koordinata[-1]-koordinata[0])



##explecit EULERJEVA metoda-zelo nestabilna AKA končne diference
tau=0.01
h=0.1
lamda=0.0
L=10

x=np.arange(-L,L,h)
pot=1/2*x**2+lamda*x**4



psi=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2))

psi2=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2),dtype=complex)
psi2[0]=0
psi2[-1]=0

for i in range(100):
    psi_temp=psi2
    for k in range(1,len(psi2)-1):
        psi2[k]=psi_temp[k]+tau*(0.5/(h**2)*(psi_temp[k-1]-2*psi_temp[k]+psi_temp[k+1])-pot[k]*psi_temp[k])*1j
    # print(i)




##normalizacija
vsota=0
for i in range(len(psi2)):
    vsota+=np.absolute(psi2)[i]
psi2=np.absolute(psi2)/vsota*len(psi2)/L





plt.plot(x,np.absolute(psi))
plt.plot(x,psi2,'o',label='num1')
plt.legend()
plt.show()






