import numpy as np
import Ex1



def ortogonalizacja_gramma_shmidta(*vectors):
    # Argumenty - n wektrów, dla których chcemy wykonać ortogonalizację
    # Zwraca listę, która zawiera wszystkie zortogonalizowane wektory

    result_vectors = []
    n = len(vectors)

    for vec in vectors:
        if vec is vectors[0]:
            first_vec = vectors[0]
            result_vectors.append(first_vec)
        else:
            suma = vec
            for i in result_vectors:
                proj = Ex1.projekcja_wektora(vec,i)
                suma = np.subtract(suma,proj)
            result_vectors.append(suma)
    return result_vectors


def wyznacznik(matrix):
    return np.linalg.det(matrix)


def rozwiaz_uklad_rownan(A, B):
    # solve Ax=b
    return np.linalg.solve(A,B)


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


def wartosci_wektory_wlasne(matrix):
    values, vectors = np.linalg.eig(matrix)
    return values, vectors


def main():
    vec1 = np.array([4, -4, 2])
    vec2 = np.array([6, -2, 2])
    vec3 = np.array([0, 0, 2])

    A = np.array([[3, 0, 0], [-1, 0, 4], [2, 1, 0]])
    B = np.array([[5, 3], [-6, -4]])

    val, vec = wartosci_wektory_wlasne(A)
    print(f'Wartosci wlasne: {val}')
    print(f'Wektory wlasne: {vec}')

   # C = np.array([[1, 8, 9], [0, 4, 3], [5, 0, 5]])
   # D = np.array([[1, 6, 4, 0], [2, 7, 3, 0], [0, 0, 0, 0], [8, 9, 0, 5]])
   # E = np.array([[1, 8, 9, 2], [0, 2, 4, 3], [5, 0, 2, 5], [5, 1, 4, 2]])


    #print(f'Rozwiazanie: {macierz_odwrotna(A)}')


if __name__ == "__main__":
    main()