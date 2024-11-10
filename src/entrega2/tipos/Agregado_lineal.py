'''
Created on 10 nov 2024

@author: gonza
'''
from typing import List, TypeVar, Generic
from abc import ABC, abstractmethod

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')

class Agregado_lineal(ABC, Generic[E]):
    """
    Clase base para los objetos agregados lineales.
    """

    def __init__(self):
        # Inicializa una lista vacía para almacenar elementos
        self._elements: List[E] = []

    def size(self) -> int:
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        """
        Verifica si la colección está vacía.
        :return: Boolean
        """
        return self.size() == 0

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos.
        :return: List
        """
        return self._elements.copy()
    
    @abstractmethod
    def add(self, e: E) -> None:
        """
        Agrega un elemento a la colección.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
        raise NotImplementedError("Método abstracto: debe ser implementado en la subclase.")

    def add_all(self, ls: List[E]) -> None:
        """
        Agrega todos los elementos de una lista a la colección.
        :param ls: Lista a agregar
        :raise NotImplementedError: Método abstracto
        """
        for e in ls:
            self.add(e)

    def remove(self) -> E:
        
        if self.is_empty():
            raise IndexError("No se puede eliminar de un agregado vacío.")
        return self._elements.pop(0)
    # Aqui lo que hace es borrar el primer elemento, mira si la lista esta vacia 
    # y so no lo esta borra el primero 
    
    def remove_all(self) -> List[E]:
        """
        Elimina todos los elementos de la colección.
        :return: Lista eliminada
        """
        removed_elements = self._elements.copy()
        self._elements.clear()
        return removed_elements

