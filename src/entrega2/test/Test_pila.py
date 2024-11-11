'''
Created on 11 nov 2024

@author: carlo
'''
from entrega2.tipos.Pila import Pila

if __name__ == '__main__':
    pila:Pila = Pila()
    pila.add(3)
    pila.add(4)
    pila.add(5)
    print(pila)
    pila.remove()
    print(pila)
    pila_elementos:list[int] = pila.remove_all()
    print(f"los elementos borrados son {pila_elementos}")