import numpy as np
import math
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


def dfsd():



    print('b')
    A=np.array([[1,2,3],[2,3,1],[3,1,2]])
    B=np.array([1,3,2])
    x=np.linalg.solve(A,B)
    print(x)


    print('b')
    A=np.array([[1,2,3],[2,3,1],[3,1,2]])
    B=np.array([1,3,2])
    x=np.linalg.solve(A,B);
    print(x)


def main():
    vec1 = np.array([4, -4, 2])
    vec2 = np.array([6, -2, 2])
    vec3 = np.array([0, 0, 2])

    A = np.array([[1, 1, -2], [0, 2, 3], [-1, 1, -5]])
    B = np.array([5,6,-3])
   # C = np.array([[1, 8, 9], [0, 4, 3], [5, 0, 5]])
   # D = np.array([[1, 6, 4, 0], [2, 7, 3, 0], [0, 0, 0, 0], [8, 9, 0, 5]])
   # E = np.array([[1, 8, 9, 2], [0, 2, 4, 3], [5, 0, 2, 5], [5, 1, 4, 2]])


    print(f'Rozwiazanie: {rozwiaz_uklad_rownan(A,B)}')


if __name__ == "__main__":
    main()