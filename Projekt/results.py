wynik_Y =[]
wynik_Z =[]
wynik_R =[]
tab_y =[]
tab_z =[]
tab_r =[]
y = open('wynik_Y.txt', 'r').readlines()
z = open('wynik_Z.txt', 'r').readlines()
r = open('wynik_R.txt', 'r').readlines()

for i in y:
    tab_y.append(i)
    
for i in tab_y:
    wynik_Y.append(int(i))

for i in z:
    tab_z.append(i)
    
for i in tab_z:
    wynik_Z.append(int(i))

for i in r:
    tab_r.append(i)
    
for i in tab_r:
    wynik_R.append(int(i))
        
print ('Y: ', sum(wynik_Y))
print ('Z: ', sum(wynik_Z))
print ('R: ', sum(wynik_R))

print ('\nWynik osiągnięto dla ', len(tab_y), 'procesorów')
