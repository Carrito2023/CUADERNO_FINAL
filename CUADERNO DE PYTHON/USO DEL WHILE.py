# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:17:31 2023

@author: Neymar
"""

contar=input("Ingrese el numero al que debo contar")
contar=int(contar)
contador=1
while True:
    print(contador)
    contador+=1
    if contador > contar:
        break
    
    