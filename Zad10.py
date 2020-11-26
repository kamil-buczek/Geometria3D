import numpy as np


print('a')
x=60  #w stopniach

x=x*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

R=np.array([[np.cos(x),-np.sin(x),0],[np.sin(x),np.cos(x),0],[0,0,1]])  # definicja macierzy obrotu wokol osi Z
print('Macierz obrotu o kąt ',x,' (wyrazony w radianach), liczby zaokrąglone do 2 cyfr')
print(np.round(R,2))

Va=np.array([9,3,2])
VaPrim=np.matmul(R,Va)
VaPrim=np.round(VaPrim,3);


print(Va)
print(VaPrim)

x=45  #w stopniach

x=x*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

R=np.array([[np.cos(x),-np.sin(x),0],[np.sin(x),np.cos(x),0],[0,0,1]])  # definicja macierzy obrotu wokol osi Z
print('Macierz obrotu o kąt ',x,' (wyrazony w radianach), liczby zaokrąglone do 2 cyfr')
print(np.round(R,2))

Va=np.array([2,2,4])
VaPrim=np.matmul(R,Va)
VaPrim=np.round(VaPrim,3);

print('b')
print(Va)
print(VaPrim)

