#!/usr/bin/env python

import random
import time


Y = 0
Z = 0
Remis = 0
y2 = 0
y1 = 0
r_zliczenia = []
y_zliczenia = []
z_zliczenia = []
for i in range(6):
    r_zliczenia.append(0)
    y_zliczenia.append(0)
    z_zliczenia.append(0)


def gra_y():

    global y1
    global y2
    global punkty_y
    y = random.randint(1,10000)     
    if y <= y2:
        punkty_y += 2
    elif y > y2 and y <= y1+y2:
        punkty_y += 1
    else:
        pass                  

def gra_z():
    
    global punkty_z
    z = random.randint(1,100)
    if z <= 33:
        pass
    elif z > 33 and z <= 33+50:
        punkty_z += 1
    else:
        punkty_z += 2  

def licz_r(i):

    for j in range(6):
        if i == j+1:
            r_zliczenia[j] += 1

def licz_y(i):
    
    for j in range(6):
        if i == j+1:
            y_zliczenia[j] += 1       

def licz_z(i):

    for j in range(6):
        if i == j+1:
            z_zliczenia[j] += 1       
 
for i in range(0,10000): 
    punkty_y = 0
    punkty_z = 0
    
    for i in range(1,7):           
        y2 = int(12/216*10000)            
        y1 = int(4*(5-i)*(6-i)/216*10000)  
        x = random.randint(1,10)
        if x <= 4:                   
            #print ("remis")
            Remis += 1
            licz_r(i)
            break
        else:
            gra_y()
            gra_z()
        if punkty_y >= 2:
            Y += 1
            licz_y(i)
            break
        if punkty_z >= 3:
            Z += 1
            licz_z(i)
            break
        if i == 6:
            Remis += 1
            licz_r(i)
            break                           
        

print ("Y: ", Y)
print ("Z: ", Z)
print ("Remis: ", Remis)
print("\n")
for j in range(6):
    print ("Runda %d: %4d   Y: %4d   Z: %4d   Remis: %4d" % (j+1, r_zliczenia[j]+y_zliczenia[j]+z_zliczenia[j], y_zliczenia[j], z_zliczenia[j], r_zliczenia[j]))
print("\n")










