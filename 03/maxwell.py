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

    tabela_odvod[n]=-1*(2*tabela[0]-tabela[1]+lamda*tabela[0]**3)
    tabela_odvod[-1]=-1*(2*tabela[n-1]-tabela[n-2]+lamda*tabela[n-1]**3)
    # test[n] += 2
    for i in range(1,n-1):
        tabela_odvod[n+i]=-1*(3*tabela[i]-tabela[i-1]-tabela[i+1]+lamda * tabela[i]**3)

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
        y0[n+i]=1
        # y0[n+i]=1


    h=10**-2
    profil=[]
    dolzina=10**6
    print(dolzina,dolzina*0.95, dolzina-0.95*dolzina)
    for i in range(dolzina):
        if (i%1000==0 and i!=0):
            print(i/dolzina*100)
        # if(i%dolzina*0.1==0):
        #     print(dolzina*0.1)
        # print(i)

        k1=odvod(y0)
        k2=odvod(y0+h*k1/2)
        k3=odvod(y0+h*k2/2)
        k4=odvod(y0+h*k3)
        y0=y0+h*(k1 + k2 + k2 + k3 + k3 + k4) / 6

        # if i> dolzina*0.95:
        #     profil.append(y0)

        if (i%100==0 and i!=0):
            # print(i)
            y0[n]=np.random.normal(loc=y0[n],scale=np.sqrt(T_l))
            y0[2*n-1]=np.random.normal(loc=y0[2*n-1],scale=np.sqrt(T_r))
        #
        # y0[n]=np.random.normal(loc=y0[n],scale=T_l)
        # y0[2*n-1]=np.random.normal(loc=y0[2*n-1],scale=T_r)
        profil.append(y0)
    return profil
    # return y0




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
# plt.ylim([-5,5])
plt.grid()
plt.show()

# plt.plot(a[-1])
# plt.grid()
# plt.show()






