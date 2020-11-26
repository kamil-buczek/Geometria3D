import numpy as np

x=60  #w stopniach

x=x*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

R=np.array([[np.cos(x),-np.sin(x),0],[np.sin(x),np.cos(x),0],[0,0,1]])  # definicja macierzy obrotu wokol osi Z
print('Macierz obrotu o kąt ',x,' (wyrazony w radianach), liczby zaokrąglone do 2 cyfr')
print(np.round(R,2))


V1=np.array([1,2,0])
V1Prim=np.matmul(R,V1)
V1Prim=np.round(V1Prim,3);

V2=np.array([2,1,0])
V2Prim=np.matmul(R,V2)
V2Prim=np.round(V2Prim,3);

print('wektory przed obrotem')
print(V1)
print(V2)
print('wektory po obrocie')
print(V1Prim)
print(V2Prim)

#rysujemy punkty (Z=0 zatem są one na płaszczyznie)

import matplotlib.pyplot as plt
plt.xlim(-3, 3) #zakres rysunku wzdluz osi X
plt.ylim(-3, 3) #zakres rysunku wzdluz osi Y

plt.plot([V1[0],V2[0]],[V1[1],V2[1]],'-o', c='r')  #wyrusujmy sobie punkty V1 i V2 połączone linią
plt.plot([V1Prim[0],V2Prim[0]],[V1Prim[1],V2Prim[1]],'-o', c='g') #to samo co wyżej dla punktow po obrocie

plt.axhline(y=0, color='b')  #dodajemy do rysunku os X
plt.axvline(x=0, color='b')  #dodajemy do rysunku os Y

plt.show()


