import numpy as np
import matplotlib.pyplot as plt

lamda=0
tau=1
T_l=1
T_r=2
n=50



def odvod(tabela):
    tabela_odvod=np.zeros(2*n+2)
    # test=np.zeros(2*n+2)
    #
    # print(type(tabela))
    ## odvod koordinate
    ##i=0,...,n-1
    for i in range(n):
        tabela_odvod[i]=tabela[n+i]

    ##odvod impulza
    ##i=0,...n-1
    ##n,..2*n-1

    tabela_odvod[n]=-1*(2*tabela[0]-tabela[1]+lamda*tabela[0]**3)-tabela[n]*tabela[2*n]
    # test[n] += 2
    for i in range(1,n-1):
        tabela_odvod[n+i]=-1*(3*tabela[i]-tabela[i-1]-tabela[i+1]+lamda * tabela[i]**3)
        # test[n+i] +=2

    tabela_odvod[2*n-1]=-1*(2*tabela[n-1]-tabela[n-2]+lamda*tabela[n-1]**3)-tabela[2*n-1]*tabela[2*n+1]
    # test[2*n-1] += 1


    ##odvod "šuma"
    ##i= 2*n, 2*n+1
    tabela_odvod[2*n]=1/tau*(tabela[n]**2-T_l)
    tabela_odvod[2*n+1]=1/tau*(tabela[2*n-1]**2-T_r)

    # print(test)
    return tabela_odvod



def rk4():

    y0 = np.zeros(2 * n + 2)
    for i in range(n):
        y0[n+i]=np.random.uniform()
        # y0[n+i]=1


    h=10**-2
    profil=[]
    dolzina=10**5
    print(dolzina,dolzina*0.95, dolzina-0.95*dolzina)
    for i in range(dolzina):
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
        profil.append(y0)

    return profil
    # return y0


def temp(data):
    n=int((len(data[0])-2)/2)
    print(n)
    temperatura=np.zeros(n)
    m=len(data)
    for stanje in data:
        for j in range(n):
            temperatura[j]+=stanje[n+j]**2
    for i in range(len(temperatura)):
        temperatura[i]=temperatura[i]/m

    return temperatura

def j(podatki):
    n=int((len(podatki)-2)/2)

    tok=np.zeros(n)
    for i in range(1,n-1):
        tok[i]=-.05*podatki[n+i]*(podatki[i+1]-podatki[i-1])
    return tok



# a=[]
# for i in range(100):
#     a.append(rk4())
# b=temp(a)

a=rk4()
b=temp(a)
# c=j(a[-1])

plt.plot(b)
plt.ylim([0.8,2.2])
plt.grid()
plt.show()

# plt.plot(c)
# plt.grid()
# plt.show()






