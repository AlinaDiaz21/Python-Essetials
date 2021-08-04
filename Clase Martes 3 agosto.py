# -*- coding: utf-8 -*-
"""
Created on Tue Aug  3 18:24:27 2021

@author: Usuario
"""

a=5
b=2
multiply=a*b


def dos(a,b):
    return(a*b)
print(dos(5,2))
multiply=(dos(5,2))
suma=multiply+5
print(suma)

#4 operaciones

def  uno(a,b):
    print("Ingresar la operación que desea realizar(*,/,+,-:")
    signo=input()
    if signo== "*":
        return a*b
    if signo=="/":
        return a/b
    if signo== "+":
        return a+b
    if signo=="-":
        return a-b
resultado=uno(5,2)
print(resultado)
