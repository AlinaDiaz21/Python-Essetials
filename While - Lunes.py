# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 18:28:06 2021

@author: Usuario
"""

contar=input("Ingrese el # de veces a contar:")
contar=int(contar)
contador=1
while True:
    print(contador)
    contador+=1
    #contador=contador+1
    if contador >contar:
        break
    
#Ejercicio WHILE

while True:
    x=input("Enter a number to count to:")
    if x=="q" or x== "quit":
        break
    x=int(x)
    y=1
    while True:
        print(y)
        y=y+1
        if y>x:
            break
