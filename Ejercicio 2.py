# -*- coding: utf-8 -*-
"""
Created on Sat Nov  6 21:00:06 2021

Nombre: Gustavo Reyes Herrera
RUT: oculto

Mis respuestas en este trabajo son propias, y están realizadas
en conformidad con la formación ética de la universidad.

"""


# Esta función determinará las palabras mas largas que 'n'
def palabra_mas_grande(lista, largo):
    # Se inicializa una lista vacia para almacenar las palabras más largas que 'n'
    lista_nueva = []
    for palabra in lista:  # Para cada elemento dentro de la lista
        if len(palabra) > largo:  # Si el largo de la palabra es mayor que 'n'
            # Se agrega a una lista nueva la palabra más larga que 'n'
            lista_nueva.append(palabra)
    return lista_nueva  # Retornamos la lista nueva con las palabras mas largas que 'n'


frase = input("Ingrese una frase: ")
n = int(input("Ingrese el largo de la palabra máxima: "))

# Se separa cada string en su propio elemento y se guarda en la lista
lista_frase = frase.split()
# Se llama a la funcion para determinar las palabras más largas que 'n' y se le pasan los valores ingresador por el usuario anteriormente
resultado = palabra_mas_grande(lista_frase, n)

print(f"Las palabras más grandes que {n} son: {resultado}")  # Resultado final
