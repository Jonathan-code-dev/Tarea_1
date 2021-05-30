#!/usr/bin/env python
# -*- coding: utf-8 -*-
    
'''Tarea: Identificar si una cadena de caracteres de entrada es palíndroma'''

# Jonathan Zárate Cartas

cadena = input("Introduzca una cadena: ") # Lectura de la cadena
string = cadena.lower() # Convierte toda la cadena a minúsculas

cad1 = "".join(string.split()) # Eliminar espacios en blanco

if cad1 == cad1[::-1]: # Se comparan las cadenas
    print("La cadena", cadena, "es palindroma")
else:
    print("La cadena", cadena, "no es palindroma")

