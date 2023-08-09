# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 15:51:26 2023

@author: Neymar
"""

edad=int(input("Ingrese su edad"))
if edad >=1 and edad <=10:
    print("Es un infante")
elif edad >10 and edad <=17:
    print("Es un adoleceste")
    
elif edad >18 and edad <=25:
    print("Es un adulto joven")
elif edad >25 and edad <60:
    print("Es un adulto")
else:
    print("Usted es un adulto mayor ")