# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 07:44:00 2023

@author: Neymar
"""

def bisiesto(año):
    if (año % 4 == 0 and año % 100 != 0) or (año % 400 == 0):
        return True
    else:
        return False

# Pruebas
año = int(input("Ingresa un año: "))
if bisiesto(año):
    print(f"{año}es un año bisiesto.")
else:
    print(f"{año}no es un año bisiesto.")
    
    
    
    
    
    
    
    
    
    
    