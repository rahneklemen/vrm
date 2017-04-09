import numpy as np
import matplotlib.pyplot as plt

N=1000
dt=0.1
lamda=0.5


##stanje [q,p]
def kin(stanje,koef):
    return np.array([stanje[0]+stanje[1]*dt*koef , stanje[1] , stanje[2]+stanje[3]*dt*koef , stanje[3]])

def pot(stanje,koef):
    return np.array([ stanje[0] , stanje[1]-stanje[0]*(1+lamda*2*stanje[2]**2)*dt*koef , stanje[2] , stanje[3]-stanje[2]*(1+lamda*2*stanje[0]**2)*dt*koef])

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



def energija(stanje):
    return 0.5*(stanje[0]**2+stanje[2]**2+stanje[1]**2 + stanje[3]**2) +lamda*stanje[0]**2*stanje[2]**2

def ekviparticija(stanje):
    return sum(np.absolute(stanje)**2)/len(stanje)


l = [0, 0.1, 1, 10]
dt = 0.01
N = 10000

p1=[]
p2=[]


for i in l:
    lamda = i
    vektor = np.array([0,1/2,1,0])

    p_temp1=[]
    p_temp2=[]
    p_temp1.append(ekviparticija(vektor[:2]))
    p_temp2.append(ekviparticija(vektor[-2:]))

    for j in range(N):
        vektor=s4(vektor)
        p_temp1.append(ekviparticija(vektor[:2]))
        p_temp2.append(ekviparticija(vektor[-2:]))
    p1.append(p_temp1)
    p2.append(p_temp2)

for i in p1:
    plt.plot(i)
plt.legend(l,title=r'$\lambda$')
plt.grid()
plt.xlabel('čas')
plt.ylabel(r'$<p_1>$')
plt.savefig('ekviparticija1.png')
plt.show()

for i in p2:
    plt.plot(i)
plt.legend(l,title=r'$\lambda$')
plt.xlabel('čas')
plt.ylabel(r'$<p_1>$')
plt.grid()
plt.savefig('ekviparticija2.png')
plt.show()

# x=[]
# v=[]
#
# x1=[]
# v1=[]
#
# ##energija:
# e=[]
# e1=[]
#
#
#
# vektor=np.array([0,1/2,1,0])
# vektor1=vektor
# vektor2=vektor
#
# # vektor1=np.array([0,1/2,1,0])
#
# e.append(energija(vektor))
# e1.append(energija(vektor1))
#
# ##ekviparticija:
# ek=[]
# ek1=[]
#
# x.append(vektor[0])
# v.append(vektor[1])
#
# x1.append(vektor[2])
# v1.append(vektor[3])
#
# for i in range(N):
#     vektor = s4(vektor)
#     # vektor2 = s4(vektor2)
#     x.append(vektor[0])
#     v.append(vektor[1])
#     x1.append(vektor[2])
#     v1.append(vektor[3])
#
#     e.append(energija(vektor))
#     e1.append(energija(vektor2))
#
#     ek.append(ekviparticija(v))
#     ek1.append(ekviparticija(v1))



    # vektor1 = s4(vektor2)
    # x1.append(vektor2[0])
    # v1.append(vektor2[1])




# naslov=r'trajektorije $\lambda=$'+str(lamda)
#
# plt.title(naslov)
# plt.plot(x,v,'-',label='x')
# plt.plot(x1,v1,'-',label='y')
# plt.xlabel('položaj')
# plt.ylabel('hitrost')
# plt.legend()
# plt.grid()
# plt.savefig('trajektorije_1.png')
# plt.show()

# naslov='energija_0.png'
# plt.plot(e,label='S2')
# plt.plot(e1,label='S4')
# plt.grid()
# plt.title(r'$\lambda$='+str(lamda)+'\t'+'dt='+str(dt))
# plt.legend(title='metoda')
# # plt.ylim([0.6,0.65])
# plt.ylabel('energija sistema')
# plt.xlabel('čas')
#
# plt.savefig(naslov)
# plt.show()

#
#
# plt.plot(ek)
# plt.plot(ek1)
# plt.ylabel(r'$<p>$')
# plt.grid()
# plt.show()





