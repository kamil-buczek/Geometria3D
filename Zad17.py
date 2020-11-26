import numpy as np
import funkcjeGeometryczne as FG;

print('a')
N=np.array([2,2,2])
n=FG.normalizuj(N)

V=np.array([9,3,2])

alfa=60
alfa=alfa*np.pi/180  #na radiany

Vprim=np.cos(alfa)*V+np.dot(n,V)*(1-np.cos(alfa))*n+np.sin(alfa)*np.cross(n,V)

print(Vprim)


print('b')
N=np.array([3,0,3])
n=FG.normalizuj(N)

V=np.array([2,2,4])

alfa=45
alfa=alfa*np.pi/180  #na radiany

Vprim=np.cos(alfa)*V+np.dot(n,V)*(1-np.cos(alfa))*n+np.sin(alfa)*np.cross(n,V)

print(Vprim)
