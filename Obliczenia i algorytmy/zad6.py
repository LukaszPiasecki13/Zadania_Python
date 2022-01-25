# Lukasz Piasecki
# Programowanie w języku Python
#
# 27.11.2021

import random
import numpy as np

def det(A):
    n=len(A)
    sum =0
    if (n>2):
        for i in range(n):
            A11 = []
            A11 = np.delete(A, (i), axis=0)  # usuwanie wiersza
            A11 = np.delete(A11, (0), axis=1)  # usuwanie kolumny
            a11 = A[i][0] * (-1) ** ((i + 1)+1)
            sum += a11 * det(A11)
        return sum
    else:
        return (A[0][0]*A[1][1]-A[0][1]*A[1][0])



#main

wielkość_macierzy =4
a=[]
A = []
#testowe dane
#a1 = [-1,2,3]
#b1 =[-9,8,7]
#c1 = [4,5,6]
#tworzenie macierzy B-macierz testowa
#B = np.vstack((a1, b1))
#B = np.vstack((B, c1))


#losowe tworzenie macierzy
for i in range(wielkość_macierzy):
    A.append(random.randint(0, 99))

for i in range(wielkość_macierzy-1):
    for i in range(wielkość_macierzy):
        a.append(random.randint(0, 99))
    A = np.vstack((A, a))
    a.clear()

print(A)
print("")
print(det(A))


