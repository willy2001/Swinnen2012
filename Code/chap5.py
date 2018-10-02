# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 15:53:14 2018

@author: Cyril GENISSON
"""
from math import pi

# Exercice 5.1
# Convertir un angle degré minute seconde en radian
degre = 60
minute = 0
seconde = 0

angle = degre + minute / 60. + seconde / 3600.
rad = angle * pi / 180
print(rad)

# Exercice 5.2
# Convertir un angle radian en degré minute seconde

angle = rad * 180 / pi
degre = int(angle)
minute = int(60 * (angle - degre))
seconde = int(3600 * (angle - degre - minute / 60))

print(degre, "°", minute, "'", seconde, '"')

# Exercice 5.3
# Convertir des °C en °F
degre = 30
fahr = degre * 1.8 + 32

print(fahr)

# Exercice 5.4
annuite = 20
taux = 4.3
capital= 100
interet = 0

for k in range(1, 21):
    interet += taux * capital / 100
    capital *= (1 + taux / 100)

print(interet)

# Exercice 5.5
# Calcul le nombre de grains de riz sur chaque case de l'échiquier
case = 1
print("case", k, ":", 1, "\t", case)
for k in range(2, 65):
    case *= 2
    print("case", k, ":", 2 ** (k-1), "\t", case)

# Exercice 5.6-5.7
# Détecte si une chaîne contient un "e" et les comptes
char = "PZAOEIUZIAEZA"
cpt = False
for k in range(len(char)):
    if str.lower(char[k]) == "e":
        cpt += 1

if cpt:
    print("La chaîne contient au moins un 'e': ", cpt)
else:
    print("La chaîne ne contient pas de 'e'")

# Exercice 5.8
# Recopie une chaîne en insérant des * entre chaque caractère
ch1 = "DNADA8192_uç&ud&éjppzjd"
ch2 = ""

for k in range(len(ch1) - 1):
    ch2 += ch1[k] + "*"

ch2 += ch1[len(ch1) - 1]

print(ch2)

# Exercice 5.9
# Inverse l'ordre des caractères d'une chaîne
ch1 = "jnzadjnazjndzalk"
reverse = ""

for k in range(len(ch1)):
    reverse += ch1[len(ch1)-k-1]
print(reverse)

# Exercice 5.10
# Détecte les palindrômes
ch1 = "Lol"
reverse = ""

for k in range(len(ch1)):
    reverse += ch1[len(ch1)-k-1]

if str.lower(reverse) == str.lower(ch1):
    print(ch1, "est un palindrôme.")
else:
    print(ch1, "n'est pas un palindrôme")


# Exercice 5.11
# Fusion de listes
t1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
t2 = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet', 'Août',
      'Septembre', 'Octobre', 'Novembre', 'Décembre']
t3 = []

for k in range(len(t1)):
    t3.append(t2[k])
    t3.append(t1[k])

print(t3)

# Exercice 5.12
# Affiche proprement les éléments d'une liste
for k in range(len(t2)):
    print(t2[k], end=" ")
print()

# Exercice 5.13
# Recherche du mamximum d'une liste
liste = [12, 11, 15, 13, 20, 35, 1, 4]
max = liste[0]

for k in range(1, len(liste)):
    if liste[k] > max:
        max = liste[k]
print("le maximum de la liste a la valeur: ", max)

# Exercice 5.14
# Scinde une liste d'entiers en deux listes de nombres pairs et impairs.
pairs = []
impairs = []
for k in range(len(liste)):
    if liste[k] % 2:
        impairs.append(liste[k])
    else:
        pairs.append(liste[k])
print(pairs, impairs)

# Exercice 5.15
# Scinde une liste de chaînes en deux listes: une pour moins de 6 caractères
name = ['Cyril', 'Alexandre', 'Bob', 'Mireille', 'Tony', 'Christine']
moins = []
plus = []
for k in range(len(name)):
    if len(name[k])>6:
        plus.append(name[k])
    else:
        moins.append(name[k])
print(moins, plus)