# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:46:09 2023

@author: Neymar
"""
acl=int(input("Ingrese el # de ACL: "))
if acl>=1 and acl <=99:
    print("Es una ACL estandar")
elif  acl>=100 and acl <=99:
    print("Es unACL extendida")
else:
    print("El numero ingresado no es un ACL")        