#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''Tarea: Crea un algoritmo que compare las edades de dos usuarios  
e imprima cual usuario es mas grande en edad. Nota: El resultado 
debe contener el nombre de la persona de mayor edad).'''

# Jonathan Zárate Cartas

persona1 = input("Introduzca el nombre del usuario 1: ")
edad1 = int(input("Introduzca la edad del usuario 1: "))

persona2 = input("Introduzca el nombre del usuario 2: ")
edad2 = int(input("Introduzca la edad del usuario 2: "))

if (edad1 != edad2):
    if(edad1 > edad2):
        print("El usuario", persona1, "es mayor que", persona2)
    else:
        print("El usuario", persona2, "es mayor que", persona1)
else:
    print("Ambos usuarios tienen la misma edad.")