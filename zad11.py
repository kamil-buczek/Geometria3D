import numpy as np

print('b')
#N=np.array([[1,4,0,-4],[2,-1,0,-2],[3,9,0,-1]]);  #macierz A
#S=np.array([[2,0,0],[0,3,0],[0,0,4]])  #macierz skalowania
#PT=np.array([-4,-2,-1]);  #punkt

N=np.array([[0,5,3,-4],[0,-5,4,-2],[0,5,5,-1]]);  #macierz A
S=np.array([[1,0,0],[0,2,0],[0,0,4]])  #macierz skalowania
PT=np.array([3,4,1]);  #punkt

print('skalujemy punkty')
print(N)
print('macierzą skalowania')
print(S)
print('względem punktu')
print(PT)

#Problem z "kształtem" wektora kolumnowego
#print(PT.shape)  #python za bardzo nie wie, jaki jest poprawny wymiar wektora PT
PT=PT.reshape(3,1) #trzeba go przerobic
#print(PT.shape)  #teraz jest OK

print('\n Najpierw musimy dokonac Translacji o wektor -PT')

N_After_Trans_1=N-PT  # numpy jest dosc mądre, stosuje tzw. 'broadcasting' ktore pozwala dodawac wektor do macierzy,
#ale trzeba uwazac, bo mozna latwo zrobic blad, warto sprawdzic czy o to nam chodzilo
print('\n punkty po translacji ')
print(N_After_Trans_1)
print('\nTeraz mozemy zrobic skalowanie')
N_AfterScale=np.matmul(S,N_After_Trans_1);
print('\n punkty po skalowaniu')
print(N_AfterScale)
print('\n Teraz ponowna translacja (tym razem o wektor PT)')
N_FINAL=N_AfterScale+PT
print('\n Wynik ostateczny (po translacji o PT)')
print(N_FINAL)

print('uwaga to można też zrobic we wspolrzednych jednorodnych!!!')
