# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 14:46:11 2018

@author: Cyril GENISSON
"""
from math import pi

# Exercice 7.2
def ligneCar(n , ca):
    l = ""
    for k in range(n):
        l += ca
    return l

# Exercice 7.3
def surfCercle(R):
    return pi * R**2

# Exercice 7.4
def volBoite(x1, x2, x3):
    return x1 * x2 * x3

# Exercice 7.5
def maximum(n1, n2, n3):
    if n1 >= n2:
        if n1 >= n3:
            return n1
        else:
            return n3
    elif n2 >= n3:
        return n2
    else:
        return n3

# Exercice 7.9
def compteCar(ca, ch):
    n = 0
    for k in range(len(ch)):
        if ch[k] == ca:
            n += 1
    return n

# Exercice 7.10
def indexMax(liste):
    max = liste[0]
    for k in range(len(liste)):
        if max < liste[k]:
            max = liste[k]
    return max

# Exercice 7.11
def nomMois(n):
    t = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai', 'Juin', 'Juillet',
         'Août', 'Septembre', 'Octobre', 'Novembre', 'Décembre']
    return t[n-1]

# Exercice 7.12
def inverse(ch):
    reverse = ""
    for k in range(len(ch)):
        reverse += ch[len(ch)-1-k]
    return reverse

# Exercice 7.13
#
def compteMots(ph):
    if ph[0] != " ":
        n = 0
    else:
        n = 1

    return n

# Exercice 7.14
