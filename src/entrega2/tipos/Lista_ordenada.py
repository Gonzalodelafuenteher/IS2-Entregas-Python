'''
Created on 10 nov 2024

@author: gonza
'''
from typing import  TypeVar, Generic, Callable
from entrega2.tipos.Agregado_lineal import Agregado_lineal

# Tipos genéricos
E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')


class Lista_ordenada(Agregado_lineal[E], Generic[E, R]):
    def __init__(self, order: Callable[[E], R]):
        # Inicializa la colección con una función de ordenación
        super().__init__()
        self._order = order

    @classmethod
    def of(cls, order: Callable[[E], R]) -> 'Lista_ordenada[E, R]':
        """
        Crea una instancia de la clase lista ordenada.
        :param order: Función de ordenación
        :return: Instancia de Lista_ordenada
        """
    
        return cls(order)

    def __index_order(self, e: E) -> int:
        assert len(self._elements) > 0, "La lista está vacía."
        if e < self._elements[0]: 
            return 0
    
        if e > self._elements[len(self._elements) - 1]: 
            return len(self._elements)
    
        for i in range(len(self._elements)):  
            if e < self._elements[i]: 
                return i
    
        return len(self._elements) 
         
    # Aqui lo que hacemo es unicamente el proceso de ordenar el numero 


        
    def add(self, e: E) -> None:
        if len(self._elements) == 0:  # Si la lista está vacía, simplemente agrega el elemento
            self._elements.append(e)
        else:
            posicion = self.__index_order(e)  # Llama a __index_order solo si la lista no está vacía
            self._elements.insert(posicion, e)
        
        
    # Lo que hace esta funcion es coger la funcion de ordenar y la utiliza con ese numero,
    # entonces ya sabe donde poner el numero y con la funcion insert metemos el numero en su sitio
    
    def __str__(self)->str:
       
        return "ListaOrdenada(" + ", ".join(str(e) for e in self._elements) + ")"

