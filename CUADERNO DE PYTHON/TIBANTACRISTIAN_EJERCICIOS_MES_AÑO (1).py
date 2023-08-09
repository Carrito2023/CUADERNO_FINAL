# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 16:27:33 2023

@author: Neymar
"""

def numerodias(año, mes):
    if mes < 1 or mes > 12:
        return None
    
    dias_por_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    return dias_por_mes[mes - 1] + (mes == 2 and ((año % 4 == 0 and año % 100 != 0) or (año % 400 == 0)))

# Pruebas
año = int(input("Ingresa un año: "))
mes = int(input("Ingresa un mes en el rango (1-12): "))

numerodias = numerodias(año, mes)

if numerodias is None:
    print("El mes debe estar en el rango de 1 a 12.")
else:
    print(f"El mes {mes} del año {año} tiene {numerodias} días.")