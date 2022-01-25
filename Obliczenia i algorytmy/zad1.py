# Lukasz Piasecki
# Programowanie w języku Python
# 27.11.2021

import cmath

while(True):
    try:
        a = float(input('Write a ='))
        break
    except ValueError:
        print("variable isn't number")

while(True):
    try:
        b = float(input('Write b ='))
        break
    except ValueError:
        print("variable isn't number")

while(True):
    try:
        c = float(input('Write c ='))
        break
    except ValueError:
        print("variable isn't number")


delta = b**2 - 4*a*c

if (delta==0 ) :
    x0 = -b/(2*a)
    print(x0)
else :
    x1 = -b - cmath.sqrt(delta) / (2*a)
    x2 = -b - cmath.sqrt(delta) / (2*a)
    print(x1)
    print(x2)













