import numpy as np
import matplotlib.pyplot as plt
#todo: ne deluje???!!!!!!
lamda=0

T_l=1
T_r=2
n=20




def odvod(tabela):
    tabela_odvod=np.zeros(2*n)

    for i in range(n):
        tabela_odvod[i]=tabela[n+i]

    ##odvod impulza
    ##i=0,...n-1
    ##n,..2*n-1

    tabela_odvod[n]=-1*(2*tabela[0]-tabela[1]+lamda*tabela[0]**3)
    # test[n] += 2
    for i in range(1,n-1):
        tabela_odvod[n+i]=-1*(3*tabela[i]-tabela[i-1]-tabela[i+1]+lamda * tabela[i]**3)
        # test[n+i] +=2

    tabela_odvod[2*n-1]=-1*(2*tabela[n-1]-tabela[n-2]+lamda*tabela[n-1]**3)
    # test[2*n-1] += 1


    return tabela_odvod

def temp(data):
    n=int((len(data[0]))/2)
    temperatura=np.zeros(n)
    m=len(data)
    for stanje in data:
        for j in range(n):
            temperatura[j]+=stanje[n+j]**2
    for i in range(len(temperatura)):
        temperatura[i]=temperatura[i]/m
    # print(len(temperatura))
    return temperatura


def rk4():

    y0 = np.zeros(2 * n )
    for i in range(n):
        y0[n+i]=np.random.uniform()
        y0[n]=np.random.uniform()
        # y0[n+i]=1


    h=10**-2
    profil=[]
    dolzina=10**5
    print(dolzina,dolzina*0.95, dolzina-0.95*dolzina)
    for i in range(dolzina):
        if (i%1000==0 and i!=0):
            print(i/dolzina*100)
        # if(i%dolzina*0.1==0):
        #     print(dolzina*0.1)
        # print(i)
        s=y0
        k1=odvod(s)
        k2=odvod(s+h*k1/2)
        k3=odvod(s+h*k2/2)
        k4=odvod(s+h*k3)
        y0=s+h*(k1 + k2 + k2 + k3 + k3 + k4) / 6

        # if i> dolzina*0.95:
        #     profil.append(y0)

        if (i%100==0 and i!=0):
            print(i)
            y0[n]=np.random.normal(loc=y0[n],scale=np.sqrt(T_l))
            y0[2*n-1]=np.random.normal(loc=y0[2*n-1],scale=np.sqrt(T_r))
        profil.append(y0)


    return profil
    # return y0




def j(podatki):
    n=int((len(podatki)-2)/2)

    tok=np.zeros(n)
    for i in range(1,n-1):
        tok[i]=-.05*podatki[n+i]*(podatki[i+1]-podatki[i-1])
    return tok



dt=10**-2
##stanje [q,p]
def kin(stanje,x):
    n=len(stanje)
    m=int(n/2)
    stanje[:m]+=stanje[m:]*x*dt
    return stanje

def pot(tabela,x):
    m=len(tabela)
    n=int(m/2)
    tabela_odvod=tabela
    tabela_odvod[n]=-1*(2*tabela[0]-tabela[1]+lamda*tabela[0]**3)*x*dt
    # test[n] += 2
    for i in range(1,n-1):
        tabela_odvod[n+i]=-1*(3*tabela[i]-tabela[i-1]-tabela[i+1]+lamda * tabela[i]**3)*x*dt
        # test[n+i] +=2

    tabela_odvod[2*n-1]=-1*(2*tabela[n-1]-tabela[n-2]+lamda*tabela[n-1]**3)*x*dt
    # test[2*n-1] += 1


    return tabela_odvod



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

def integracija(iteracija):
    y0 = np.zeros(2 * n )
    podatki=[]
    podatki.append(y0)
    for i in range(n):
        y0[n+i]=np.random.uniform()
        y0[n]=np.random.uniform()

    for i in range(iteracija):
        if i%100==0 and i!=0:
            # print(i)
            y0[n]=np.random.normal(loc=y0[n],scale=np.sqrt(T_l))
            y0[2*n-1]=np.random.normal(loc=y0[2*n-1],scale=np.sqrt(T_r))
        y0=s4(y0)
        podatki.append(y0)
    return podatki

# a=[]
# for i in range(100):
#     a.append(rk4())
# b=temp(a)

# a=rk4()
a=integracija(10**5)
b=temp(a)
# c=j(a[-1])

plt.plot(b)
# plt.ylim([-5,5])
plt.grid()
plt.show()

# plt.plot(c)
# plt.grid()
# plt.show()






