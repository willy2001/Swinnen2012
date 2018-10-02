# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 16:52:31 2018

@author: Cyril GENISSON
"""

# Exercice 4.2
# Affiche les 20 premiers multiples de 7
for k in range(1, 21):
    print(7*k, end=' ')
print()

# Exercice 4.3
# Affiche la conversion euro-dollar pour les 15 premières puissances de 2
euro = 1.65

for k in range(0, 15):
    print(2**k, 'euro(s) = ', euro * 2**k, 'dollar(s)')

# Exercice 4.4
# Affiche les 12 premiers termes d'une suite géométrique de raison 3
nb = 10
for k in range(13):
    print(nb * 3**k)

# Exercice 4.5
# Affiche l'aire d'un parallélépipède rectangle
L, l, p = 10, 20 , 30
print(L*l*p)

# Exercice 4.6
# Converti un nombre de seconde en années jours heures minutes secondes
nb_sec = 86400 * 366 + 3661

years, days = nb_sec // (365*86400), nb_sec % (365*86400)
days, hours = days // 86400, days % 86400
hours, minutes = hours // 3600, hours % 3600
minutes, secondes = minutes // 60, minutes % 60
print(years, 'année(s)', days, 'jour(s)', hours, 'h', minutes, 'm', secondes, 's')

# Exercice 4.7
# Donne les multiples de 7 en marquant les divisible par 3
for k in range(1, 21):
    n = 7*k
    if n%3:
        print(n, end=' ')
    else:
        print(n, end='* ')
print()

# Exercice 4.8
# Affiche les multiples de 13 divisibles par 7
for k in range(1, 21):
    n = 13*k
    if not(n % 7):
        print(n, end=' ')
print()

# Exercice 4.9
# Affiche un demi sapin de Noël
for i in range(1, 8):
    for j in range(1, i+1):
        print('*', end=' ')
    print()