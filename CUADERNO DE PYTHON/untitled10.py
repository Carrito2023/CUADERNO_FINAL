# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:31:16 2023

@author: Neymar
"""

class Robot:
    def _int_(self,nombre,marca,tecnologia,tamaño,color):
        self.nombre=nombre
        self.marca=marca
        self.tecnologia=tecnologia
        self.tamaño=tamaño
        self.color=color
        
    def cocinar (self):
        print("El robot esta cocinando")
    def ayudar(self):
        print("El robot esta ayudando")
    def caminar (self):
        print("El robot esta caminando")
    def barrer(self):
        print("El robot esta barriendo ")
    def lavando(self):
        print("El robot esta lavando")