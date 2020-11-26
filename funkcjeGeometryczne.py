import numpy as np
import math


def macierz_odwrotna(X):
    dim=X.shape[0]
    ONES=np.zeros((dim,dim),dtype=float)
    for i in range(0,dim):
        ONES[i,i]=1
    Z1=np.append(X,ONES,axis=1)
    for i in range(0,dim):
        Z1[i,:]=Z1[i,:]/Z1[i,i]
        for j in range(0,dim):
            if j !=i:
                Z1[j,:]=Z1[j,:]-Z1[i,:]*Z1[j,i]
    Z2=Z1[:,dim:2*dim]
    return Z2




def projection(u,na_v):
    v=na_v
    u_norm=np.sqrt(np.dot(u,u))
    v_norm=np.sqrt(np.dot(v,v))
    proj_u_na_v=(np.dot(u,v)/(v_norm*v_norm))*v;
    return proj_u_na_v;

def norma(u):
    return np.sqrt(np.dot(u,u));

def normalizuj(u):
    return u/norma(u);


def kosinus(u,v):
    u_norm=np.sqrt(np.dot(u,u))
    v_norm=np.sqrt(np.dot(v,v))
    ilocz=np.dot(u,v);
    kos=ilocz/(u_norm*v_norm);
    return kos;

def kat(u,v):
    kos=kosinus(u,v)
    katRad=math.acos(kos)
    return math.degrees(katRad);

def ortigonalizacja(u,v,z):
    u1=u;
    v1=v-projection(v,u1);
    z1=z-projection(z,u1)-projection(z,v1)
    return {'u1':u1,'v1':v1,'z1':z1};