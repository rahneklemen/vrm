import numpy as np
import matplotlib.pyplot as plt


def vektor(kot1,kot2):
    return np.cos(kot1)*np.sin(kot2), np.sin(kot1)*np.sin(kot2),np.cos(kot2)


def inv_vektor(x5,y5,z5):
    # if z5/(x5**2+y5**2+z5**2) > 1 and z5/(x5**2+y5**2+z5**2) < -1 :
    #     print('vecje od 1',x5,y5,z5)
    # print('dolzina_na kvadrat',(x5**2+y5**2+z5**2))
    return np.arccos(z5),np.arctan(y5/x5)


def stanje(n,T):
    # T=1
    N=10**4
    fi=np.random.rand(n)*2*np.pi
    theta=np.arccos(2*np.random.rand(n)-1)
    rand_st=np.random.rand(N)
    # print('zacetek')
    for i in range(N):
        j=np.random.randint(0,n-1)

        x1,y1,z1=vektor(fi[j],theta[j])
        x2,y2,z2=vektor(fi[j+1],theta[j+1])

        x_sum=x1+x2
        y_sum=y1+y2
        z_sum=z1+z2

        # print('tocke', x1,y1,z1,'dolzina',x1**2+y1**2+z1**2,'tocka2',x2,y2,z2,'dolzina',x2**2+y2**2+z2**2,'j=',j)
        # print(x_sum**2+y_sum**2+z_sum**2)
        #presecisce-krona med sfero (r=1 s=0) in sfero (r=1 in s=rs)
        rs=np.sqrt(x_sum**2+y_sum**2+z_sum**2)
        # print('rs',rs)

        #kota krone
        beta=np.arccos(rs/2)
        alfa=np.random.rand()*2*np.pi

        #delta vektor
        x_delta=np.cos(alfa)*np.sin(beta)
        y_delta=np.sin(alfa)*np.sin(beta)
        z_delta=np.cos(beta)

        #trasformacija za kota fi_sum, theta_sum
        fi_sum=np.arctan(y_sum/x_sum)
        theta_sum=np.arccos(z_sum/rs)



        x1_nov = x_delta * np.cos(theta_sum) * np.cos(fi_sum) - y_delta * np.sin(fi_sum) + z_delta * np.sin(theta_sum) * np.cos(fi_sum)
        y1_nov = x_delta * np.cos(theta_sum) * np.sin(fi_sum) + y_delta * np.cos(fi_sum) + z_delta * np.sin(theta_sum) * np.sin(fi_sum)
        z1_nov = -1* x_delta * np.sin(theta_sum) + z_delta * np.cos(theta_sum)

        # print('mora biti 1:',x1_nov**2+y1_nov**2+z1_nov**2)
        # print('mora biti 1-delta:',x_delta**2+y_delta**2+z_delta**2)
        # print(j)

        #drugi vektor:
        x2_nov=x_sum-x1_nov
        y2_nov=y_sum-y1_nov
        z2_nov=z_sum-z1_nov

        #energije
        stara=-(x1*x2+y1*y2+z1*z2)
        nova=-(x1_nov*x2_nov+y1_nov*y2_nov+z1_nov*z2_nov)
        delta=nova-stara

        if rand_st[i]< np.exp(-delta/T):
            # print('-------------------------------^')
            theta[j],fi[j]=inv_vektor(x1_nov,y1_nov,z1_nov)

            theta[j + 1],fi[j+1]=inv_vektor(x2_nov,y2_nov,z2_nov)

    return fi, theta

def korelacija_single(phi,theta):
    phi0=phi[0]
    theta0=theta[0]
    kor=np.zeros(len(phi))
    for i in range(len(phi)):
        kor[i]=np.sin(theta0)*np.sin(theta[i])*np.cos(phi0-phi[i])+np.cos(theta0)*np.cos(theta[i])
    return kor


def korelacija(temperatura):
    M=20
    korel_dolzina=np.zeros(M)
    print('prvi zacetek')
    for iteracija in range(10**2):
        a,b=stanje(M,temperatura)
        korel_dolzina+=korelacija_single(a,b)
        print(iteracija)

    return korel_dolzina


T1=0.1
plt.plot(korelacija(T1))
plt.grid()
plt.show()



