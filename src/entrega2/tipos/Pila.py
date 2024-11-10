'''
Created on 10 nov 2024

@author: gonza
'''

from typing import  TypeVar
from entrega2.tipos.Agregado_lineal import Agregado_lineal

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')



class Pila(Agregado_lineal[E]):
    """
    Una Pila es una estructura de datos que sigue el principio LIFO (Last In, First Out).
    Los elementos se apilan y solo se puede acceder al elemento en la parte superior.
    
    IMPORTANTE. Como la estructura subyacente es una lista, la parte superior de la pila es el primer 
    elemento de la lista.
    """
    
    def add(self, element: E) -> None:
        """Añade un nuevo elemento a la parte superior de la pila (al principio)."""
        self.elements.insert(0, element)  # Inserta el elemento al principio de la lista


    @classmethod
    def of(cls) -> 'Pila[E]':
        """Método de fábrica que crea e inicializa una nueva instancia de la clase."""
        return cls()