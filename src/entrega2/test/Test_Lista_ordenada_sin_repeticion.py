'''
Created on 11 nov 2024

@author: carlo
'''
from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion

if __name__ == '__main__':
    
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN::")
    
    print("Creación de una lista con criterio de orden lambda x: -x")
    lista:Lista_ordenada_sin_repeticion = Lista_ordenada_sin_repeticion(lambda x: -x)
    elementos_a_agregar:list[int] = [23, 47, 47, 1, 2, 2, -3, 4, 5]
    
    lista.add_all(elementos_a_agregar)
        
    
    print(f"Resultado de la lista ordenada sin repetición: {lista}")
    
    eliminado:list[int] = lista.remove(47)
    print(f"El elemento eliminado al utilizar remove(): {eliminado}")
    
    elementos_eliminados:list[int]= lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")
    
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(0)  # Añadir 0
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(7)  # Añadir 7
    print(f"Lista después de añadirle el 7: {lista}")
   
    