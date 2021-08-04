# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 19:24:40 2021

@author: Usuario
"""

def saludos(lista):
    for i in lista:
        print("Hola,",i)
    print("")

saludos(["Juan"])
saludos(["Juan","Ana"])
saludos(["Juan","Ana", "Dillan"])
saludos(["Juan","Ana", "Dillan","Ale"])

def crealista(n):
    lista=[]
    for i in range(n):
        lista.append(i)
    return lista
print(crealista(15))
resultado=crealista(20)
print(resultado)