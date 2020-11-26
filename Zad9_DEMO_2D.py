import numpy as np
import matplotlib.pyplot as plt

print('a')
N=np.array([[1,3,2],[1,1,4]])
print('skalujemy czerwone punktu - wierzchołki trojkata')
print(N)


S=np.array([[2,0],[0,3]])
print('\nmacierza S')
print(S)
W=np.dot(S,N);
print('\nwynik -punkty zielone')
print(W)

plt.xlim(0, 15)
plt.ylim(0, 15)

plt.scatter(N[0],N[1],  c='r')
plt.scatter(W[0],W[1],  c='g')

plt.show()











