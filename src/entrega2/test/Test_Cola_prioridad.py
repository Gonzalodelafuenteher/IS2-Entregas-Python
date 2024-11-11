'''
Created on 11 nov 2024

@author: carlo
'''
from entrega2.tipos.Cola_prioridad import Cola_prioridad

if __name__ == '__main__':
    print("TEST DE COLA PRIORIDAD:")
    cola:Cola_prioridad[str, int] = Cola_prioridad[str, int]()
    cola.add('Paciente A', 3) 
    cola.add('Paciente B', 2) 
    cola.add('Paciente C', 1)
    print(cola)
    assert cola.elements() == ['Paciente C','Paciente B','Paciente A'],"El orden de la cola es incorrecto."
    atencion:list[str] = []
    while not cola.is_empty():
        atencion.append(cola.remove())
    assert atencion == ['Paciente C','Paciente B','Paciente A'],"El orden de atención no es correcto."
    print("Pruebas superadas exitosamentee.")
    