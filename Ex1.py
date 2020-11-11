import numpy as np
import math




def suma_wektorow(vec1, vec2):
    return np.add(vec1, vec2)


def iloczyn_skalarny(vec1, vec2):
    return np.dot(vec1, vec2)


def iloczyn_wektorowy(vec1, vec2):
    return np.cross(vec1, vec2)


def cos_alfa(vec1, vec2):
    licznik = iloczyn_skalarny(vec1, vec2)
    mianownik = iloczyn_skalarny(norma_wektora(vec1), norma_wektora(vec2))
    wynik = licznik/mianownik
    return wynik


def norma_wektora(vec):
    return np.sqrt(np.dot(vec, vec))


def kat_pomiedzy_wektorami(vec1, vec2):
    cos = cos_alfa(vec1, vec2)
    katrad = math.acos(cos)
    return math.degrees(katrad)


def projekcja_wektora(vec1, vec2):
    # Projekcja wektora vec1 na wektor vec2
    # projvec2VEC1
    licznik = iloczyn_skalarny(vec1, vec2)
    mianownik = iloczyn_skalarny(vec2,vec2)
    wynik = np.multiply((licznik/mianownik), vec2)
    return wynik


def normalizacja_wektora(vec):
    return vec/norma_wektora(vec)


def main():
    vec1 = np.array([8, 8, 0])
    vec2 = np.array([6, 2, 0])
    print(f'Projekcja wektora wynosi: {projekcja_wektora(vec1, vec2)}')


if __name__ == "__main__":
    main()
