import numpy as np

print('b')
S=np.array([[4,0,0,0],[0,2,0,0],[0,0,2,0],[0,0,0,1]])
T1=np.array([[1,0,0,1],[0,1,0,-2],[0,0,1,3],[0,0,0,1]])
T2=np.array([[1,0,0,2],[0,1,0,1],[0,0,1,0],[0,0,0,1]])

alfa=45;
alfa=alfa*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

RX=np.array([[1,0,0,0],[0,np.cos(alfa),-np.sin(alfa),0],[0,np.sin(alfa),np.cos(alfa),0],[0,0,0,1]])
#print(RX)

beta=120;
beta=beta*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

RY=np.array([[np.cos(beta),0,np.sin(beta),0],[0,1,0,0],[-np.sin(beta),0, np.cos(beta),0],[0,0,0,1]])
#print(RY)

P=np.array([[0,3,3],[2,2,-2],[4,1,5],[1,1,1]])

M=np.matmul(RX,S);
M=np.matmul(T1,M);
M=np.matmul(RY,M);
M=np.matmul(T2,M);
W=np.matmul(M,P)
print('macierz M')
print(np.round(M,3));
print('P\'')
print(np.round(W,3))


print('c')
S=np.array([[0.5,0,0,0],[0,2,0,0],[0,0,3,0],[0,0,0,1]])
T1=np.array([[1,0,0,5],[0,1,0,-1],[0,0,1,2],[0,0,0,1]])
T2=np.array([[1,0,0,2],[0,1,0,0],[0,0,1,4],[0,0,0,1]])

alfa=150;
alfa=alfa*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

RX=np.array([[1,0,0,0],[0,np.cos(alfa),-np.sin(alfa),0],[0,np.sin(alfa),np.cos(alfa),0],[0,0,0,1]])
#print(RX)

beta=270;
beta=beta*np.pi/180# przeliczenie kąta na radiany (do sinusa i kosinusa)

RY=np.array([[np.cos(beta),0,np.sin(beta),0],[0,1,0,0],[-np.sin(beta),0, np.cos(beta),0],[0,0,0,1]])
#print(RY)

P=np.array([[4,1,-1],[2,2,2],[0,3,-4],[1,1,1]])

M=np.matmul(RX,S);
M=np.matmul(T1,M);
M=np.matmul(RY,M);
M=np.matmul(T2,M);
W=np.matmul(M,P)
print('macierz M')
print(np.round(M,3));
print('P\'')
print(np.round(W,3))

