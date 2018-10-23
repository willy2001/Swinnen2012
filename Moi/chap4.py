# -*- coding: utf-8 -*-
"""
Spyder Editor
"""
#exercice 4,1
a, b, c, d = 3, 4, 5, 7
a, c = c, a

print(a, b, c, d)

#exercice 4,2
e = 0
while e < 20:
    e = e +1
    print(e*7)
    
    #exercice 4,3
f = 1
while f<= 16384:
    print(f, f*1.65)
    f = f*2
    
    #exercice 4,5
l, h, p = 5, 6, 7
print(l*h*p)

    #exercice 4.6
sec= 86400 * 366 + 3661

annés, jours = sec // (365*86400), sec % (365*86400)
jours, heures = jours // 86400, jours % 86400
heures, minutes = heures // 3600, minutes % 3600
minutes, seconde = minutes // 60, minutes % 60
print(annés, 'an', jours, 'jo', heures, 'heu', minutes, 'min', seconde, 'sec')

    # exercice 4.7
k = 1
while k<21:
    o = k*7
    print(k,end=' ')
    if k % 3 == 0:
        print("*", end=' ')
    k = k + 1
    
    # exercice 4.8
q = 1
while q<51:
    r = q*13
    print(r,end=' ')
    if r % 7 == 0:
        print("*", end=' ')
    q = q + 1
    
#exercice 4.9

for x in range(1, 8):
    for y in range(1, x+1):
        print('*', end=' ')
    print()
    
    
    
    
    
    
    
    
    