# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:15:24 2023

@author: Neymar
"""

class Coche:
    def _init_(self,color,marca,año,estado,modelo):
        self.color=color
        self.marca=marca
        self.año=año
        self.estado=estado
        self.modelo=modelo
        
    def enciende (self):
        print("El carro se esta encendiendo")
    def conducir(self):
        print("El carro esta conduciendo")
    def detener (self):
        print("El carro se detuvo")
    def parquear(self):
        print("El carro se ha parqueado")
    def apagar(self):
        prin("El carro se esta apagando")
        
        