import numpy as np

print('a')
print('macierz')
X=np.array([[1,0.5],[0,2]])
print(X)

z=np.linalg.eigvals(X)
z1=np.linalg.eig(X)
print('\nwartosci wlasne')
print(z)
print('\nwartosci wlasne i wektory wlasne do poszczegolnych wartosci  - wektory własne to kolumny macierzy!!!')
print(z1)

print('b')
X=np.array([[5,3],[-6,-4]])
print(X)


z=np.linalg.eigvals(X)
z1=np.linalg.eig(X)
print('wartosci wlasne')
print(z)
print('wartosci wlasne i wektory wlasne do poszczegolnych wartosci')
print(z1)


print('c')
X=np.array([[3,0,0],[-1,0,4],[2,1,0]])
print(X)


z=np.linalg.eigvals(X)
z1=np.linalg.eig(X)
print('wartosci wlasne')
print(z)
print('wartosci wlasne i wektory wlasne do poszczegolnych wartosci')
print(z1)