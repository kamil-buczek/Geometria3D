import numpy as np

print('Tutaj mamy prostszą wersję poprzedniego składamy skalowanie wokol zera i jedna translacje - uwaga wazna kolejnosc :)')

#S=np.array([[2,0,0,0],[0,1,0,0],[0,0,2,0],[0,0,0,1]])
#T=np.array([[1,0,0,1],[0,1,0,1],[0,0,1,2],[0,0,0,1]])
#N=np.array([[0,1,2],[0,1,5],[0,1,1],[1,1,1]])

S=np.array([[1/2,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,1]])
T=np.array([[1,0,0,5],[0,1,0,-1],[0,0,1,2],[0,0,0,1]])
N=np.array([[4,1,-1],[2,2,2],[0,3,-4],[1,1,1]])

print('\nPunkty')
print(N)
print('\nMacierz skalowania')
print(S)
print('\nMacierz translacji')
print(T)
F=np.matmul(S,T)
print('\nMacierz S*T - nie ta kolejnosc!!!')
print(F)
W=np.matmul(F,N)
print('\nWynik')
print(W)

F=np.matmul(T,S)
print('\n\nMacierz T*S')
print(F)
W=np.matmul(F,N)
print('\nWynik')
print(W)

