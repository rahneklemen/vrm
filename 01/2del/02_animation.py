"""
A simple example of an animated plot
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

L=10
h=0.1
x=np.arange(-L,L,h)

psi=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2))

fig, ax = plt.subplots()


line, = ax.plot(x, np.absolute(psi)**2)


def animate(i):
    line.set_ydata(np.absolute(np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2))*np.exp(-1j*i/2)*i))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,interval=5, blit=True)
plt.show()
