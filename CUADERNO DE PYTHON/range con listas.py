# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 16:02:31 2023

@author: Neymar
"""
listar_r=[]
listar_a=[]
listar_v=[]
listar_s=[]
lista=["R1","R2","R3",
       "S1","S2","S3",
       "AP1","AP2","AP3",
       "FW2","PC1","PC2"]
for elemento in lista:
    if "R" in elemento:
       listar_r.append(elemento)
       print(listar_r)
       
       
    elif "S" in elemento:
       listar_s.append(elemento)
       print(listar_s)
       
       
    elif "AP" in elemento:
        listar_a.append(elemento)
        print(listar_a)
    else:
        listar_v.append(elemento)
        print(listar_v)
       
       
       


   
    