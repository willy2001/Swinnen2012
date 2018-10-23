"""
Created on Wed Oct 17 18:02:24 2018

@author: willy
"""

#exercice 6.1

print("nombres de mph", end =' ')
nbr = input()
mph = float(nbr)
mps = mph * 1609 / 3600
kmph = mph * 1.609

print(mph, "mph =", kmph, "km/h ", mps, "m/s")

#exercice 6.2

from math import sqrt

print("a= ")
a = float(input())
print("b= ")
b = float(input())
print("c= ")
c = float(input())
d = (a + b + c)/2 
S = sqrt(d*(d-a)*(d-b)*(d-c)) 
print("côtés =", a, b, c)
print("Périmètre =", d*2, "Aire =", S)

#exercice 6.3

from math import sqrt
from math import pi

print("l= ")
l = float(input())
print("g= ")
g = float(input())
t = 2 * pi * sqrt(l / g)

print("la période de la pendule est : ", t)

#exercice 6.4

liste = []
valeur = "valeur"
while valeur != "":
    print("entrer un valeur")
    valeur = input()
    if valeur != "":
        liste.append(float(valeur))
print(liste)

#exercice 6.5
#si la valeur entrée est 1 ou 15, le programme affiche "gagné"
#si la valeur entrée est 2, le programme affiche "perdu"
#si la valeur entrée est 3, le programme affiche "un instant s.v.p"


#exercice 6.6
#a) le programme affiche "& et and"
#b) le programme affiche "presque gagné"
#c) le programme affiche "perdu"

#exercice 6.7
#si a est une valeur réelle alors le programme affiche perdu 
#si a est une valeur non réelle alors le programme affiche gagné
