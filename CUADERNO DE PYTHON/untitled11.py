# -*- coding: utf-8 -*-
"""
Created on Fri Aug  4 19:37:38 2023

@author: Neymar
"""

class RedSocial:
    def _int_(self,logo,funciones,colores,nombre,audiencia):
        self.logo=logo
        self.funciones=funciones
        self.colores=colores
        self.nombre=nombre
        self.audiencia=audiencia
        
    def enviar (self):
        print("La red social esta enviando mensaje")
    def ver(self):
        print("La red social esta visualizando videos y fotos ")
    def seguir (self):
        print("La red social esta siguiendo personajes publicos")
    def informar(self):
        print("La red social esta informando ")
    def subir (self):
        print("La red social esta subiendo videos y fotos")