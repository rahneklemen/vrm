import pyqentangle
import numpy as np

tensor = np.array([[0., np.sqrt(0.5)], [np.sqrt(0.5), 0.]])

pyqentangle.schmidt_decomposition(tensor)

fcn = lambda x1, x2: np.exp(-((0.5*(x1+x2))**2))*np.exp(-(x1-x2)**2)*np.sqrt(2./np.pi)

decompositions = pyqentangle.continuous_schmidt_decomposition(fcn, -10., 10., -10., 10., keep=10)

map(lambda dec: dec[0], decompositions)

x1array = np.linspace(-10., 10., 100)
x2array = np.linspace(-10., 10., 100)
import matplotlib.pyplot as plt
print(decompositions[0][1](x1array))
# plt.plot(x2array, decompositions[0][1](x2array))
plt.show()