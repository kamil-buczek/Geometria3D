import numpy as np
import funkcjeGeometryczne

print('b')
A=np.array([0,2,0])
B=np.array([10,2,0])
C=np.array([5,12,0])

print('wyznaczmy dwa boki')
AB=B-A
AC=C-A
print(AB)
print(AC)

X=np.cross(AB,AC)
print('przed normalizacja')
print(X)
X=funkcjeGeometryczne.normalizuj(X)
print('po normalizacji')
print(X)

print('dla testu wezmy inne boki')
AB=B-A
BC=C-B
print(AB)
print(BC)

Y=np.cross(AB,BC)
print('przed normalizacja')
print(Y)
Y=funkcjeGeometryczne.normalizuj(Y);
print('po normalizacji')
print(Y)

