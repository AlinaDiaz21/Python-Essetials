# -*- coding: utf-8 -*-
"""
Created on Mon Aug  2 19:46:08 2021

@author: Usuario
"""

def uno():
    print("Ingrese el valor:")
    
uno()

def hola(nombre):
    print("Hola", nombre)
    
hola("Alina")

#Saludos 2 parametros
def saludos(nombre1,nombre2):
    print("Hola",nombre1)
    print("Hola",nombre2,"\n")

saludos("Juan","Ana")  
saludos("Carlos","Diana")  

#Direcciones

def direccion(provincia,ciudad,barrio):
    print("Su dirección es:")
    print("Su provincia es:",provincia)
    print("La ciudad de domicilio es:",ciudad)
    print("La dirección de referencia es:",barrio)
    
pr=input("Ingrese la provincia:")
br=input("Ingrese el barrio:")
ci=input("Ingrese la ciudad:")

direccion(pr,ci,br)
direccion(provincia=pr,ciudad=ci,barrio=br)
direccion(provincia=pr,barrio=br,ciudad=ci)

#resta
def resta(a,b):
    print("La resta entre:",a,"-",b,"es:",a-b,"\n")
resta(5,2)
resta(2,5)
resta(a=2,b=5)
resta(b=5,a=2)
resta(5,b=2)
    













