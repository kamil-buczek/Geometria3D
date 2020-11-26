import matplotlib
import numpy as np

print('a')
N=np.array([[1,3],[2,1],[-1,2]]);
M=np.array([[1,0,0],[0,2,0],[0,0,3]])
#print(M)

W=np.dot(M,N)
print('rezultat\n' ,W)


print('b')
N=np.array([[1,-2,5],[-2,2,3],[3,2,4]]);
M=np.array([[2,0,0],[0,2,0],[0,0,3]])
print(N)

W=np.dot(M,N)
print('rezultat\n' ,W)

print('c')
N=np.array([[0,1,2,-4],[0,1,-1,7],[0,1,3,5]]);
M=np.array([[3,0,0],[0,4,0],[0,0,1]])
print(N)

W=np.dot(M,N)
print('rezultat\n' ,W)
