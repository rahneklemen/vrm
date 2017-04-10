import matplotlib.pyplot as plt
import numpy as np



def odvod(x):
    return -1*x



def rk():
    x=[]
    x0=1
    x.append(x0)
    h=10**-2
    print(h)
    for i in range(100):
        k1=odvod(x0)
        k2=odvod(x0+h/2*k1)
        k3=odvod(x0+h/2*k2)
        k4=odvod(x0+h/2*k3)
        x0+=h/6*(k1+2*k2+2*k3+k4)
        x.append(x0)
    return x

a=rk()
plt.plot(a)
plt.show()
