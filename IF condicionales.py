# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 19:28:24 2021

@author: Usuario
"""

print("Inicio")
datos=1
nativa=100
print("Antes de IF")
if datos==nativa:
    print("entro del IF para el valor de verdad")
    print("Las variables son iguales")
else:
    print("dentro del else para el valor de falso")
    print("Las variables son diferentes")

print("Despues del IF")
print("Fin")

#ACL

acl=int(input("Ingrese el valor de ACL:"))
if acl>=1 and acl<=99:
    print("La ACL es estandar")
elif acl>=100 and acl<=199:
    print("La ACL es extendida")

else:
    print("el #ingresado no es de un ACL")
    

