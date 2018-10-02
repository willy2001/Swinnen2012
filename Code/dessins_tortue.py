# -*- coding: utf-8 -*-
"""
Created on Mon Oct  1 20:16:49 2018

@author: Cyril GENISSON
"""
from turtle import *

# Exercice 7.*
# Création de différentes fonctions de dessins
couleur = ['blue', 'brown', 'black', 'red', 'yellow', 'green', 'purple']

def equilateral(c, s):
    ''' Méthode pour dessiner un triangle équilatéral:
        c: couleur
        s: taille en pixels
    '''
    color(c)
    down()
    for k in range(3):
        forward(s)
        left(120)
    up()
    forward(s+20)

def carre(c, s):
    ''' Méthode pour dessiner un carré:
        c: couleur
        s: taille en pixels
    '''
    color(c)
    down()
    for k in range(4):
        forward(s)
        left(90)
    up()
    forward(s+20)

reset()
carre(couleur[3], 60)
equilateral(couleur[0],50)