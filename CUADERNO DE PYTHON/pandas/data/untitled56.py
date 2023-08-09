# -*- coding: utf-8 -*-
"""
Created on Tue Aug  8 21:25:58 2023

@author: Neymar
"""



class Elevador:
    def __init__(self, floor_numbers, floor_types):
        self.floor_numbers = floor_numbers
        self.floor_types = floor_types

    def go_to_floor(self, floor_number):
        if floor_number in self.floor_numbers:
            floor_type = self.floor_types[floor_number]
            print("¡Vaya al piso del {}!".format(floor_type))
        else:
            print("En este edificio está el piso número {}.".format(floor_number))

    def ask_which_floor(self, floor_type):
        if floor_type in self.floor_types:
            floor_number = self.floor_types.index(floor_type)
            print("El piso de {} es el número: {}.".format(floor_type, floor_number))
        else:
            print("No hay ningún piso con {} en este edificio.".format(floor_type))

# Datos de ejemplo
floor_types = ['Estacionamiento', 'Negocios', 'Área de restaurantes', 'Oficinas']
floor_numbers = list(range(-1, 4))

# Crear instancia de la clase Ascensor
el = Elevador(floor_numbers, floor_types)

# Ejemplos de uso
el.go_to_floor(1)
el.go_to_floor(-2)
el.ask_which_floor('Oficinas')
el.ask_which_floor('Piscina')
