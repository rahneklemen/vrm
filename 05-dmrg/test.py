#empty file
# import schmidt
#

import matplotlib.pyplot as plt
import pyqentangle
import numpy as np

# tensor = np.array([[0., np.sqrt(0.5)], [np.sqrt(0.5), 0.]])

n=8

tensor=np.ones(n)/np.sqrt(n)
a=pyqentangle.schmidt_decomposition(tensor)
print(a)
print(len(a))

