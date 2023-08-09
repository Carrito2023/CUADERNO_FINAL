# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 11:26:57 2023

@author: Neymar
"""

class Robot:
    def _init_(self,color,marca,tecnologia,estado,modelo):
        self.color=color
        self.marca=marca
        self.tecnologia=tecnologia
        self.estado=estado
        self.modelo=modelo
        
    def lava (self):
        print("El robot esta lavando")
    def cocina(self):
        print("El robot esta cocinando")
    def ayuda (self):
        print("El robot esta ayudando")
    def barre(self):
        print("El robot esta barriendo")
    def apaga(self):
        print("El robot se esta apagando")