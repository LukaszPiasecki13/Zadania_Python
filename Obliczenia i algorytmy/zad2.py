# Lukasz Piasecki
# Programowanie w języku Python
# 27.11.2021

import random
X = []
X_sorted = []
X_check = []
for i in range(50) :
    X.append(random.randint(0,99))
X_check = X.copy()
X_check.sort(reverse = True)
print(X)



for i in range(len(X)) :
    max_num = max(X)
    X_sorted.append(max_num)
    X.remove(max_num)

print(X_sorted)

#Sprawdzanie

if X_check == X_sorted :

    print("Program działa prawidłowo")

