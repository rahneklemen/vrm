import numpy as np
import matplotlib.pyplot as plt

N=100
dt=0.1


##stanje [q,p]
def kin(stanje,koef):
    return np.array([stanje[0]+stanje[1]*dt*koef,stanje[1]])

def pot(stanje,koef):
    return np.array([stanje[0],stanje[1]-stanje[0]*dt*koef])


def s2(stanje):

    a1=0.5
    stanje = kin(stanje,a1)
    # stanje=stanje*a1
    b1=1
    stanje =pot(stanje,b1)


    a2=0.5
    stanje=kin(stanje,a2)

    return stanje


def s4(stanje):

    x0=-(2)**(1/3)/(2-2**(1/3))
    x1=1/(2-2**(1/3))


    stanje = kin(stanje,x1/2)

    stanje =pot(stanje,x1)

    stanje=kin(stanje,(x1+x0)/2)

    stanje = pot(stanje, x0)

    stanje = kin(stanje, (x1 + x0) / 2)

    stanje = pot(stanje, x1)

    stanje = kin(stanje, x1 / 2)


    return stanje





x=[]
v=[]

x1=[]
v1=[]


vektor=np.array([1,0])
vektor1=np.array([1,1])


x.append(vektor[0])
v.append(vektor[1])
x1.append(vektor1[0])
v1.append(vektor1[1])

for i in range(N):
    vektor = s2(vektor)
    x.append(vektor[0])
    v.append(vektor[1])
    vektor1 = s4(vektor1)
    x1.append(vektor1[0])
    v1.append(vektor1[1])

# print(len(x))
# print(x)
plt.plot(x,v)
plt.plot(x1,v1)
plt.xlabel('položaj')
plt.ylabel('hitrost')
plt.grid()
plt.show()






