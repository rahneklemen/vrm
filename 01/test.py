"""
A simple example of an animated plot
"""
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up formatting for the movie files
Writer = animation.writers['ffmpeg']
writer = Writer(fps=15, metadata=dict(artist='Me'), bitrate=1800)



tau=0.001
h=0.1
lamda=0.0
L=10
premik=2

x=np.arange(-L,L,h)
pot=1/2*x**2+lamda*x**4


psi=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-x**2/2))

psi2=np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-(x+premik)**2/2),dtype=complex)
A=np.array([np.zeros(len(psi),dtype=complex) for i in range(len(psi))],dtype=complex)
H=np.identity(len(A),dtype=complex)

for i in range(len(H)):
    if i==0:
        H[0][0]=1-1j*tau*(1/h**2+pot[i])
        H[0][1]=1j*tau/h**2
    if i+1==len(H):
        H[i][i]=1-1j*tau*(1/h**2+pot[i])
        H[i][i-1] = 1j * tau / h ** 2
    else:
        H[i][i]=1-1j*tau*(1/h**2+pot[i])
        H[i][i-1] = 1j * tau / h ** 2
        H[i][i+1] = 1j * tau / h ** 2

C=np.dot(np.linalg.inv(np.conjugate(H)),H)


fig, ax = plt.subplots()
line, = ax.plot(x, np.absolute(psi2))

def animate(i):

    psi2=np.dot(C,np.array(np.polynomial.hermite.hermval(x,[1])*1/(np.pi)**0.25*np.exp(-(x+premik)**2/2),dtype=complex))
    line.set_ydata(np.absolute(psi2))  # update the data
    return line,


# Init only required for blitting to give a clean slate.
def init():
    line.set_ydata(np.ma.array(x, mask=True))
    return line,

ani = animation.FuncAnimation(fig, animate, np.arange(1, 200), init_func=init,interval=25, blit=True)
ani.save('im.mp4',writer=writer)
plt.show()


