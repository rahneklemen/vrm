import numpy as np
import matplotlib.pyplot as plt

# def matrika(z):
#     np.array([],dtype=complex)
#     return np.array([np.array([np.exp(2*z),0,0,0],dtype=complex),np.array([0,np.cosh(2*z),np.sinh(2*z),0],dtype=complex),np.array([0,np.sinh(2*z),np.cosh(2*z),0],dtype=complex),np.array([0,0,0,np.exp(2*z)],dtype=complex)],dtype=complex)*np.exp(-1*z)
#
#
#
#
#
# def veriga(n):
#     qubiti=np.ones(n,dtype=complex)
#     return qubiti
#
# print(veriga(5))


def iteracija(stanje,n,z,K):
    stanje_temp=stanje
    for l in range(K):
        ##razdelitev na sode/lihe
        for j in range(n):
            if (j%2==0): # 0,2,4,6,..
                for i in range(len(stanje)):
                    a=np.binary_repr(i,n)
                    if a[j:j+2]=='00':
                        #print(type(stanje_temp[i]),type(stanje[i]),type(np.exp(z)))
                        stanje_temp[i] = stanje[i] * np.exp(z)
                    if a[j:j + 2] == '01':
                        b=a[:j]+'10'+a[j+2:]
                        stanje_temp[i] = np.exp(-1*z)*(np.cosh(z)*stanje[i]+np.sinh(z)*stanje[int(b,2)])
                    if a[j:j + 2] == '10':
                        b=a[:j]+'01'+a[j+2:]
                        stanje_temp[i] =  np.exp(-1*z)*(np.sinh(z)*stanje[i]+np.cosh(z)*stanje[int(b,2)])
                    if a[j:j + 2] == '11':
                        stanje_temp[i] = stanje[i] * np.exp(z)
                stanje=stanje_temp
        for j in range(n):
            if (j%2==1): # 1,3,5,7...; potrebno vkluciti robni pogoj
                if j==n-1:
                    for i in range(len(stanje)):
                        a=np.binary_repr(i,n)
                        if a[-1]+a[0]=='00':
                            stanje_temp[i] = stanje[i] * np.exp(z)
                        if a[-1]+a[0]=='01':
                            b = '1'+a[1:-1]+'0'
                            stanje_temp[i] = np.exp(-1 * z) * (np.cosh(z) * stanje[i] + np.sinh(z) * stanje[int(b, 2)])
                        if a[-1]+a[0]=='10':
                            b = '0' + a[1:-1] + '1'
                        if a[-1]+a[0]=='11':
                            stanje_temp[i] = stanje[i] * np.exp(z)

                for i in range(len(stanje)):
                    a=np.binary_repr(i,n)
                    if a[j:j+2]=='00':
                        stanje_temp[i] = stanje[i] * np.exp(z)
                    if a[j:j + 2] == '01':
                        b=a[:j]+'10'+a[j+2:]
                        stanje_temp[i] = np.exp(-1*z)*(np.cosh(z)*stanje[i]+np.sinh(z)*stanje[int(b,2)])
                    if a[j:j + 2] == '10':
                        b=a[:j]+'01'+a[j+2:]
                        stanje_temp[i] =  np.exp(-1*z)*(np.sinh(z)*stanje[i]+np.cosh(z)*stanje[int(b,2)])
                    if a[j:j + 2] == '11':
                        stanje_temp[i] = stanje[i] * np.exp(z)
                stanje = stanje_temp

    return stanje

def termodinamika(n):
    beta=np.arange(0.1,5,0.1)
    # beta=np.exp(temp)
    toplotna=[]
    stanje = np.ones(2 ** n, dtype=complex)
    for i in beta:
        a=iteracija(stanje,n,complex(-i/2,0),20)
        print(sum(np.absolute(a)**2/len(a)))
        toplotna.append(-1/i*np.log(sum(np.absolute(a)**2/len(a))))
        stanje=a
    plt.plot(beta,toplotna,'o')
    # plt.xscale('log')
    plt.show()

termodinamika(8)








