# Lukasz Piasecki
# Programowanie w języku Python
# 27.11.2021

import random
import numpy as np

wielkość_macierzy =8
a=[]
b=[]
A = []
B = []
C = []


for i in range(wielkość_macierzy):
    A.append(random.randint(0, 99))
    B.append(random.randint(0, 99))

for i in range(wielkość_macierzy-1):
    for i in range(wielkość_macierzy):
        a.append(random.randint(0, 99))
        b.append(random.randint(0, 99))
    A = np.vstack((A, a))
    a.clear()
    B = np.vstack((B, b))
    b.clear()

C= A*B

print(A)
print("")
print(B)
print("")
print(C)


