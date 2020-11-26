import matplotlib
import numpy as np

print('a')
N=np.array([[1,4,0,-4],[2,-1,0,-2],[3,9,0,-1]]);  #macierz A
S=np.array([[2,0,0],[0,3,0],[0,0,4]])  #macierz skalowania
PT=np.array([-4,-2,-1]);  #punkt

print('skalujemy punkty')
print(N)
print('macierzą skalowania')
print(S)
print('względem punktu')
print(PT)
print('UWAGA ostatni z punktow w tablicy to punkt wzgledem ktorego sie skaluje - on nie powinien sie zmienic')


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

print('\n\n\n Teraz uzyjemy wspolrzednych jednorodnych')

N=np.array([[1,4,0,-4],[2,-1,0,-2],[3,9,0,-1],[1,1,1,1]]);  #macierz A
SJ=np.array([[2,0,0,-4*(1-2)],[0,3,0,-2*(1-3)],[0,0,4,-1*(1-4)],[0,0,0,1]])  #macierz skalowania we wspolrzednych jednorodnych
W1=np.matmul(SJ,N)
print('Macierz N we wspolrzednych jednorodnych')
print(N)
print('Macierz skalowania wzgledem punktu we wspolrzednych jednorodnych')
print(SJ)
print('Wynik\n\n')
print(W1)



