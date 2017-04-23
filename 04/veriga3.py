import numpy as np
import matplotlib.pyplot as plt


def vektor(kot1,kot2):
    return np.cos(kot1)*np.sin(kot2), np.sin(kot1)*np.sin(kot2),np.cos(kot2)

def stanje(n):
    T=1
    N=10**5
    fi=np.random.rand(n)*2*np.pi
    theta=np.arccos(2*np.random.rand(n)-1)
    rand_st=np.random.rand(N)
    for i in range(N):
        j=np.random.randint(0,n-1)

        x1,y1,z1=vektor(fi[j],theta[j])
        x2,y2,z2=vektor(fi[j+1],theta[j+1])

        x_sum=x1+x2
        y_sum=y1+y2
        z_sum=z1+z2

        #presecisce-krona med sfero (r=1 s=0) in sfero (r=1 in s=rs)
        rs_kvadrat=x_sum**2+y_sum**2+z_sum**2
        rs=np.sqrt(rs_kvadrat)

        #kota krone
        alfa=np.arcos(rs_kvadrat/2)
        beta=np.random.rand()*2*np.pi

        #delta vektor
        x_delta=np.cos(beta)*np.sin(alfa)
        y_delta=np.sin(alfa)*np.sin(alfa)
        z_delta=np.cos(alfa)

        #trasformacija za kota fi_sum, theta_sum
        fi_sum=np.arctan(y_sum/x_sum)
        theta_sum=np.arccos(z_sum/rs)

        x1_nov = x_delta*np.cos(theta_sum)+y_delta*np.sin(theta_sum)*np.cos(fi_sum)+z_delta*np.sin(theta_sum)*np.sin(fi_sum)
        y1_nov = x_delta*-1*np.sin(theta_sum)+y_delta*np.cos(theta_sum)*np.cos(fi_sum)+z_delta*np.cos(theta_sum)*np.cos(fi_sum)
        z1_nov = -1*np.sin(theta_sum)+z_delta*np.cos(theta_sum)

        #drugi vektor:
        x2_nov=x_sum-x1_nov
        y2_nov=y_sum-y1_nov
        z2_nov=z_sum-z1_nov

        #todo spremema energije
    return fi, theta

def korelacija_single(phi,theta):
    phi0=phi[0]
    theta0=theta[0]
    kor=np.zeros(len(phi))
    for i in range(len(phi)):
        kor[i]=np.sin(theta0)*np.sin(theta[i])*np.cos(phi0-phi[i])+np.cos(theta0)*np.cos(theta[i])
    return kor


def korelacija():
    M=30
    korel_dolzina=np.zeros(M)
    for iteracija in range(10**2):
        a,b=stanje(M)
        korel_dolzina+=korelacija_single(a,b)
        print(iteracija)

    return korel_dolzina

plt.plot(korelacija())
plt.grid()
plt.show()



