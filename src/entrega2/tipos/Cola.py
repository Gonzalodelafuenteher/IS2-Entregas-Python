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


class Cola(Agregado_lineal[E]):
    @classmethod
    def of(cls) -> 'Cola[E]':
        return cls()

    def add(self, e: E) -> None:
        self._elements.append(e) 
        """
        Agrega un elemento a la cola.
        :param e: Elemento a agregar
        :raise NotImplementedError: Método abstracto
        """
    def __str__(self)->str:
       
        return "Cola(" + ", ".join(str(e) for e in self._elements) + ")"  