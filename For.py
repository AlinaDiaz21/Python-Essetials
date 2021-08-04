# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:57:23 2021

@author: Usuario
"""
print("Inicio")
lista=["R1", "R2","R3","R4"]
"""print(lista[0])
print(lista[1])
print(lista[2])
print(lista[3])"""
for item in lista:
    print(item)
    print("IN for")
    
print("Fin")
lista1=[]
lista=["R1","R2","R3","R4"
       ,"S1","S2"]
for item in lista:
    if "S" in item:
        lista1.append(item)
print(lista1)


print