'''
Created on 10 nov 2024

@author: gonza
'''
from typing import  TypeVar, Generic
from entrega2.tipos.Lista_ordenada import Lista_ordenada

E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')


class Lista_ordenada_sin_repeticion(Lista_ordenada[E, R], Generic[E, R]):
        
    def add(self, e: E) -> None:
        cont = 0
        if len(self._elements) == 0:  # Si la lista está vacía, simplemente agrega el elemento
            self._elements.append(e)
        else:
            cont = 0 
            for i in range(len(self._elements)):  
                if e == self._elements[i]:  
                    cont += 1  
            if cont < 1:
                    posicion = self.__index_order(e)
                    self._elements.insert(posicion, e)

         
    # Aqui lo que hacemo es unicamente el proceso de ordenar el numero 
    
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

    def __str__(self)->str:
       
        return "Lista_ordenada_sin_repeticion(" + ", ".join(str(e) for e in self._elements) + ")"
        

