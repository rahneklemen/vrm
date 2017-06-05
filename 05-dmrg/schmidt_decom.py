import numpy as np
import matplotlib.pyplot as plt

import mpnum
n=4

# matrika = np.array([np.zeros(n),np.zeros(n)])
# matrika[0][0]=1
#
matrika = np.array([np.ones(n),np.ones(n)])/np.sqrt(8)


# print(matrika)

print(np.linalg.svd(matrika))


# print(a)




