import numpy as np
import matplotlib.pyplot as plt


n=4

matrika = np.array([np.ones(n),np.ones(n)])/np.sqrt(8)
# matrika[0][0]=np.sqrt(2)
# matrika[1][-1]=np.sqrt(2)


# print(matrika)

print(np.linalg.svd(matrika))


# print(a)




