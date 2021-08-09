"""
@author: Usuario
"""
#Convertir 1/100km en mpg 
'''Funciones:
    |100mtompg
    mpgto|100km
    
    Verificar: 
       mil= 1 milla a mericana = 1609.344 metros;
       gal=1 galón americano =3.785411784 litros.'''
mil=float(1609.344)
gal=float(3.785411784)
def l100kmtompg(liters):
    a = ((1 / (liters / 100)) * 1000 / mil *gal)
    a = float(a)
    return a

def mpgtol100km(miles):
    l100km = (1 / (((miles * mil) / gal) / 1000) * 100)
    return l100km

print(l100kmtompg(3.9))
print(l100kmtompg(7.5))
print(l100kmtompg(10))
print(mpgtol100km(60.3))
print(mpgtol100km(31.4))
print(mpgtol100km(23.5))

