import numpy as np

print('a')
S=np.array([[2,0,0,0],[0,1,0,0],[0,0,2,0],[0,0,0,1]])
T1=np.array([[1,0,0,1],[0,1,0,1],[0,0,1,2],[0,0,0,1]])
T2=np.array([[1,0,0,0],[0,1,0,1],[0,0,1,2],[0,0,0,1]])

alfa=45;
alfa=alfa*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

RX=np.array([[1,0,0,0],[0,np.cos(alfa),-np.sin(alfa),0],[0,np.sin(alfa),np.cos(alfa),0],[0,0,0,1]])
#print(RX)

beta=90;
beta=beta*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

RY=np.array([[np.cos(beta),0,np.sin(beta),0],[0,1,0,0],[-np.sin(beta),0, np.cos(beta),0],[0,0,0,1]])
#print(RY)

P=np.array([[0,1,2],[0,1,5],[0,1,1],[1,1,1]])

M=np.matmul(RX,S);
print(np.round(M,3));
M=np.matmul(T1,M);
print(np.round(M,3));
M=np.matmul(RY,M);
print(np.round(M,3));
M=np.matmul(T2,M);
print(np.round(M,3));
W=np.matmul(M,P)
print('macierz M')
print(np.round(M,3));
print('P\'')
print(np.round(W,3))

