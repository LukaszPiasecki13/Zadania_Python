# Lukasz Piasecki
# Programowanie w języku Python
# 20.12.2021

import math

class Complex:
    def __init__(self,real,imag):
        self.re = real
        self.im = imag
    def conjugate(self):
        self.im = -self.im
    def module(self):
        self.module = math.sqrt(self.re * self.re + self.im * self.im)
    def print(self):
        if(self.im >0):
            print(f"{self.re} + {self.im}i")
        else:print(f"{self.re} {self.im}i")
    def __mul__(self, other):
        if isinstance(other, Complex):
            return Complex(self.re * other.re - self.im * other.im, self.re * other.im +self.im * other.re)
        else:
            return Complex(self.re * other, self.im * other)
    def __add__(self, other):
        if isinstance(other,Complex):
            return Complex(self.re + other.re, self.im + other.im)
        else: return Complex(self.re + other, self.im)
    def __sub__(self, other):
        return Complex(self.re - other.re, self.im - other.im)



def Initiation():
    while(True):
        print("Podaj liczbę zespoloną. Format(a + bi)): ")
        try:
            a = int(input("a = "))
            break
        except ValueError:
            print("variable isn't number")
    while (True):
        try:
            b = int(input("b = "))
            break
        except ValueError:
            print("variable isn't number")
    z = Complex(a, b)
    return z

def Is_Space_Symbol(symbol):
    if symbol == " ":
        return True
    else : return False
def Is_Plus_Symbol(symbol):
    if symbol == "+":
        return True
    else : return False
def Is_Minus_Symbol(symbol):
    if symbol == "-":
        return True
    else : return False
def Is_Mul_Symbol(symbol):
    if symbol == "*":
        return True
    else : return False
def Is_Equal_Symbol(symbol):
    if symbol == "=":
        return True
    else : return False
def Is_Div_Symbol(symbol):
    if symbol == "/":
        return True
    else : return False

def Count(flag_sign,z1,z2):
    if flag_sign == "+":
        return (z1+z2)
    elif flag_sign == "-":
        return (z1-z2)
    elif flag_sign == "*":
        return (z1+z2)
    elif flag_sign == " ":
        return z1


print("Można wpisywać równanie nie zważając na spacje np. 1+2 *3i+ 1-2i. Błędne litery są pomijane.")
print("Pamiętaj aby nie doblować znaków np. ++, **, -----")
print("")
rownanie = input("Podaj równanie:")
#rownanie = "1sd+10i+1i  = "
wynik = Complex(0,0)
cyfra =""
flag_sign= "+"
flag_work = False
liczba = Complex(0,0)

for i in range (len(rownanie)):
    if str.isnumeric(rownanie[i]):
        warunek = True
        while(warunek):
            try:
                if str.isnumeric(rownanie[i]) :
                    cyfra = cyfra + rownanie[i]
                    try:
                        liczba = Complex(int(cyfra), 0)
                        flag_work = False
                        warunek = False
                    except ValueError:
                        print("Coś poszło nie tak")
                else: warunek = False
            except IndexError:
                warunek = False

    elif rownanie[i] == "i":
        liczba = Complex(0, int(cyfra))
        warunek = False
    else :
        if Is_Space_Symbol(rownanie[i]):
            cyfra = ""
            flag_work = False
        if Is_Plus_Symbol(rownanie[i]):
            flag_work = True
            if flag_work:
                if flag_sign == "*":
                    liczba = liczba * liczba_w_pamieci
                wynik = Count(flag_sign, wynik, liczba)
                flag_work = False
            cyfra = ""
            flag_sign = "+"
            flag_work = True
        if Is_Minus_Symbol(rownanie[i]):
            flag_work = True
            if flag_work:
                if flag_sign == "*":
                    liczba = liczba * liczba_w_pamieci
                wynik = Count(flag_sign, wynik, liczba)
                flag_work = False
            cyfra = ""
            flag_sign = "-"
            flag_work = True
        if Is_Mul_Symbol(rownanie[i]):
            cyfra = ""
            flag_sign = "*"
            liczba_w_pamieci =liczba
        if Is_Equal_Symbol(rownanie[i]):
            cyfra = ""
            flag_work = True
            if flag_work:
                if flag_sign == "*":
                    liczba = liczba * liczba_w_pamieci
                wynik = Count(flag_sign, wynik, liczba)
                flag_work = False
            break
       # if Is_Div_Symbol(rownanie[i]): #Zrobić w przyszłości


flag_work = True
if flag_work:
    if flag_sign == "*":
        liczba = liczba * liczba_w_pamieci
    wynik = Count(flag_sign, wynik, liczba)
    flag_work = False
print("wynik =")
wynik.print()

