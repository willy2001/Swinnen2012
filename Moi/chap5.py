#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 17 18:02:24 2018

@author: willy
"""
import math

#exercice 5.1

minutes = 0
secondes = 0
degré = 30
angle = degré + minutes /60. + secondes/3600.
radians = angle * math.pi /180
print(radians)

#exercice 5.3

degcel = 30
degfar = degcel * 1.8 + 32
print(degfar)

#exercie 5.4

somme = 100
interet1 = 100 * 4.3 / 100
interet20 = interet1 * 20
print(interet20)

#exercice 5.5

case = 1
grain = 1
while case < 65:
    print(case, grain)
    case, grain = case + 1, grain * 2
    
#exercice 5.6
    
     
chaine = "ndjnczjnzcaonbc"
caractere = "e"
lc = len(chaine)
a = 0
b = 0
while a < lc:
    if chaine[a] == caractere:
        b = 1
    a = a + 1
print("caractère :", caractere, end =' ')
if b == 1:
    print("il y a un E")
else:
    print("il y a pas de E", end =' ')

#exercice 5.8

mot = "bonjour"
mot2 = ""

for k in range(len(mot) - 1):
    mot2 += mot[k] + "*"

mot2 += mot[len(mot) - 1]

print(mot2)

#exercice 5.9

mot = "ruojnob"
retour = len(mot)
envers = retour - 1
nch = ""

while envers >= 0:
    nch = nch + mot[envers]
    envers = envers - 1

print(nch)

#exercice 5.10

mot = "kayak"
motinv = ""

for k in range(len(mot)):
    motinv += mot[len(mot)-k-1]

if str.lower(motinv) == str.lower(mot):
    print(mot, "est un palindrôme.")
else:
    print(mot, "n'est pas un palindrôme")
    
#exercice 5.11

t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin','Juillet', 'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']

t3 = []
liste = 0
while liste < len(t1):
    t3.append(t2[liste])
    t3.append(t1[liste])
    liste = liste + 1
print(t3)


#exercice 5.12

t2 = ['Janvier','Février','Mars','Avril','Mai','Juin', 'Juillet','Août','Septembre','Octobre','Novembre','Décembre']
liste = 0
while liste < len(t2):
    print(t2[liste], end =' ')
    liste = liste + 1
    
#exercice 5.13

liste = [32, 5, 12, 8, 3, 75, 2, 15]
maxi = liste[0]
a = 0
while a < len(liste):
    if liste[a] > maxi:
        maxi = liste[a]
    a = a + 1

print("le plus grand element de cette liste est", maxi)

#exercice 5.14

liste = [32, 36, 12, 8, 3, 75, 2, 15]
nbpairs = []
nbimpairs = []
a = 0
while a < len(liste):
    if liste[a] % 2 == 0:
        nbpairs.append(liste[a])
    else:
        nbimpairs.append(liste[a])
    a = a + 1

print("nombres pairs de la liste", nbpairs)
print("nombres impairs de la liste", nbimpairs)

#exercice 5.15

liste = ['Jean', 'Maximilien', 'Brigitte', 'Sonia', 'Jean-Pierre', 'Sandra']
nomplus = []
nommoins = []
a = 0
while a < len(liste):
    if len(liste[a])>6 :
        nomplus.append(liste[a])
    else:
        nommoins.append(liste[a])
    a = a + 1
    
print("nom avec plus de 6 lettres", nomplus)
print("nom avec moin de 6 lettres", nommoins)






