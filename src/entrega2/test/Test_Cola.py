'''
Created on 11 nov 2024

@author: carlo
'''
from entrega2.tipos.Cola import Cola

if __name__ == '__main__':
    print("TEST DE COLA:")
    print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
    
    cola = Cola()  # Crea una nueva cola
    elementos_a_agregar = [23, 47, 1, 2, -3, 4, 5]
    for e in elementos_a_agregar:
        cola.add(e)  # Añade cada elemento a la cola
    
    print(f"Resultado de la cola: {cola}")  # Muestra el estado de la cola

    elementos_eliminados = cola.remove_all()  # Elimina todos los elementos de la cola
    print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")  # Muestra los elementos eliminados
    