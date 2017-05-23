import numpy as np
import matplotlib.pyplot as plt

def odvod(tabela,lamda):
    m=len(tabela)
    n=int(m/2)
    # print(m,n)
    tabela_odvod=np.zeros(2*n)

    tabela_odvod[:n]=tabela[n:]

    tabela_odvod[n]=-1*(2*tabela[0]-tabela[1]+lamda*tabela[0]**3)
    tabela_odvod[-1]=-1*(2*tabela[n-1]-tabela[n-2]+lamda*tabela[n-1]**3)

    for i in range(1,n-1):
        tabela_odvod[n+i]=-1*(3*tabela[i]-tabela[i-1]-tabela[i+1]+lamda*tabela[i]**3)
    # print(tabela_odvod)
    return tabela_odvod


# def odvod2(tabela,lamda):
#     return -1*tabela



def rk4(iteracij,dt,lam,n):
    data=[]
    zacetek=np.ones(2*n)
    data.append(zacetek)
    for i in range(iteracij):

        k1=odvod(zacetek,lam)
        k2=odvod(zacetek+dt/2*k1,lam)
        k3=odvod(zacetek+dt/2*k2,lam)
        k4=odvod(zacetek+dt*k3,lam)
        zacetek=zacetek+dt/6*(k1 +2* k2 +2* k3 + k4)
        #todo preveri ali dela tempreratura
        if i%10==0 and i!=0:
            a1=np.random.normal(scale=np.sqrt(2))
            a2=np.random.normal(scale=np.sqrt(1))
            # print(a1,a2)
            zacetek[-1]=a1
            zacetek[n]=a2
        data.append(zacetek)

    return data



def trajectorija(meritve):
    tocke=len(meritve)
    x=[]
    print(tocke)
    for i in range(tocke):
        x.append(meritve[i][2]**2)
    return x

def temp(data):
    st_delcev=int((len(data[0]))/2)
    print(st_delcev)
    temperatura=np.zeros(st_delcev)
    m=len(data)
    for stanje in data:
        for j in range(st_delcev):
            temperatura[j]+=stanje[st_delcev+j]**2
    for i in range(len(temperatura)):
        temperatura[i]=temperatura[i]/m

    return temperatura

# odvod(np.ones(20),0)
podatki=rk4(10**5,10**-2,0.5,20)
b=trajectorija(podatki)

a=temp(podatki)
print(a)
print(len(a))

plt.plot(a,'o-')
plt.grid()
# plt.ylim([0,10])
plt.show()


