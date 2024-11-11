'''
Created on 11 nov 2024

@author: carlo
'''
from entrega2.tipos.Lista_ordenada import Lista_ordenada

if __name__ == '__main__':
    print("TEST DE LISTA ORDENADA:")
    # Creación de una lista con criterio de orden
    lista = Lista_ordenada(lambda x: x)
    print("Creación de una lista con criterio de orden lambda x: x")

    # Se añade en este orden: 3, 1, 2
    lista.add(3)
    lista.add(1)
    lista.add(2)
    print(f"Se añade en este orden: 3, 1, 2")
    print(f"Resultado de la lista: {lista}")

    # El elemento eliminado al utilizar remove()
    removed_element = lista.remove()
    print(f"El elemento eliminado al utilizar remove(): {removed_element}")

    # Elementos eliminados utilizando remove_all
    removed_elements = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {removed_elements}")
    
    # Comprobando si se añaden los números en la posición correcta
    lista.add(3)  # Reagregar elementos para la prueba
    lista.add(1)
    lista.add(2)

    lista.add(0)
    print(f"Lista después de añadirle el 0: {lista}")

    lista.add(10)
    print(f"Lista después de añadirle el 10: {lista}")

    lista.add(7)
    print(f"Lista después de añadirle el 7: {lista}")
    