import numpy as np


#przyklad a
print('a')
S=np.array([[2,0,0,0],[0,1,0,0],[0,0,2,0],[0,0,0,1]])
T=np.array([[1,0,0,1],[0,1,0,1],[0,0,1,2],[0,0,0,1]])
N=np.array([[0,1,2],[0,1,5],[0,1,1],[1,1,1]])

print('\nPunkty')
print(N)
print('\nMacierz skalowania')
print(S)
print('\nMacierz translacji')
print(T)


F=np.matmul(T,S)
print('\n\nMacierz T*S')
print(F)
W=np.matmul(F,N)
print('\nWynik a')
print(W)

#przyklad b
print('b')
S=np.array([[4,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,1]])
T=np.array([[1,0,0,1],[0,1,0,-2],[0,0,1,3],[0,0,0,1]])
N=np.array([[0,3,3,0],[2,2,-2,0],[4,1,5,0],[1,1,1,1]])

print('\nPunkty')
print(N)
print('\nMacierz skalowania')
print(S)
print('\nMacierz translacji')
print(T)


F=np.matmul(T,S)
print('\n\nMacierz T*S')
print(F)
W=np.matmul(F,N)
print('\nWynik b')
print(W)

print('c')
#przyklad c
S=np.array([[0.5,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,1]])
T=np.array([[1,0,0,5],[0,1,0,-1],[0,0,1,2],[0,0,0,1]])
N=np.array([[4,1,-1],[2,2,2],[0,3,-4],[1,1,1]])

print('\nPunkty')
print(N)
print('\nMacierz skalowania')
print(S)
print('\nMacierz translacji')
print(T)


F=np.matmul(T,S)
print('\n\nMacierz T*S')
print(F)
W=np.matmul(F,N)
print('\nWynik c')
print(W)


