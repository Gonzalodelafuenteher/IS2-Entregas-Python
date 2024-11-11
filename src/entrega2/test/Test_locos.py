'''
Created on 10 nov 2024

@author: gonza
'''
from entrega2.tipos.Lista_ordenada_sin_repeticion import Lista_ordenada_sin_repeticion
from entrega2.tipos.Lista_ordenada import Lista_ordenada
from entrega2.tipos.Cola import Cola
from entrega2.tipos.Cola_prioridad import Cola_prioridad

def main():
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
    
    print("#############################################################################################################")
    
    print("TEST DE LISTA ORDENADA SIN REPETICIÓN::")
    
    print("Creación de una lista con criterio de orden lambda x: -x")
    lista = Lista_ordenada_sin_repeticion(lambda x: -x)
    elementos_a_agregar = [23, 47, 47, 1, 2, 2, -3, 4, 5]
    
    lista.add_all(elementos_a_agregar)
        
    
    print(f"Resultado de la lista ordenada sin repetición: {lista}")
    '''
    eliminado = lista.remove(47)
    print(f"El elemento eliminado al utilizar remove(): {eliminado}")
    
    elementos_eliminados = lista.remove_all()
    print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")
    '''
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(0)  # Añadir 0
    print(f"Lista después de añadirle el 0: {lista}")
    lista.add(7)  # Añadir 7
    print(f"Lista después de añadirle el 7: {lista}")
   
    
    print("##############################################################################################################")
    
    print("TEST DE COLA:")
    print("Creación de una cola vacía a la que luego se le añaden con un solo método los números: 23, 47, 1, 2, -3, 4, 5")
    
    cola = Cola()  # Crea una nueva cola
    elementos_a_agregar = [23, 47, 1, 2, -3, 4, 5]
    for e in elementos_a_agregar:
        cola.add(e)  # Añade cada elemento a la cola
    
    print(f"Resultado de la cola: {cola}")  # Muestra el estado de la cola

    elementos_eliminados = cola.remove_all()  # Elimina todos los elementos de la cola
    print(f"Elementos eliminados utilizando remove_all: {elementos_eliminados}")  # Muestra los elementos eliminados
    
    print("##############################################################################################################")
    print("TEST DE COLA PRIORIDAD:")
    cola = Cola_prioridad[str, int]()
    cola.add('Paciente A', 3) 
    cola.add('Paciente B', 2) 
    cola.add('Paciente C', 1)
    assert cola.elements() == ['Paciente C','Paciente B','Paciente A'],"El orden de la cola es incorrecto."
    atencion = []
    while not cola.is_empty():
        atencion.append(cola.remove())
    assert atencion == ['Paciente C','Paciente B','Paciente A'],"El orden de atención no es correcto."
    print("Pruebas superadas exitosamentee.")

if __name__ == '__main__':
    main()