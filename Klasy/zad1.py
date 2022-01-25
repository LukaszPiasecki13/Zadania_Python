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


a = Complex(1,-2)
b = Complex(1,0)
c = a * b

c.print()







