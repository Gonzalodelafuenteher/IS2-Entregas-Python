'''
Created on 10 nov 2024

@author: gonza
'''

from typing import List, TypeVar, Generic, Tuple



E = TypeVar('E')
R = TypeVar('R')
P = TypeVar('P')



class Cola_prioridad(Generic[E, P]):
    def __init__(self):
        # Inicializa dos listas vacías, una para los elementos y otra para sus prioridades
        self._elements: List[E] = []  
        self._prioridad: List[P] = []

    def size(self) -> int:
        """
        Devuelve el número de elementos en la colección.
        :return: Int
        """
        return len(self._elements)

    def is_empty(self) -> bool:
        if len(self._elements) == 0:
            return True
        else:
            return False

    def elements(self) -> List[E]:
        """
        Devuelve una copia de la lista de elementos de mayor a menor prioridad
        :return: List
        """
        return self._elements.copy()


    def add(self, e: E, priority: P) -> None:
        index = self.index_order(priority)
        self._elements.insert(index, e)
        self._prioridad.insert(index, priority)
        
    def index_order(self, priority: P) -> int:
        """
        Este método calcula el índice en el que se debe insertar
        el nuevo elemento, de acuerdo con su prioridad.
        :param priority: Prioridad del nuevo elemento.
        :return: Índice donde se debe insertar el nuevo elemento.
        """
        if len(self._prioridad) == 0:
            return 0  # Si la cola está vacía, insertamos al principio
        
        # Si la nueva prioridad es mayor que la más alta, se inserta al final
        if priority >= self._prioridad[-1]: 
            return len(self._elements)
        
        # Si la nueva prioridad es menor que la más baja, se inserta al principio
        if priority < self._prioridad[0]: 
            return 0
    
        # Buscamos el índice donde la nueva prioridad debe ser insertada
        for i in range(len(self._prioridad)):
            if priority < self._prioridad[i]: 
                return i
            
        return len(self._elements)  # Si no se encontró un índice, se inserta al final
     

    def remove(self) -> E:
        """
        Elimina el primer elemento de la cola. El primer elemento es el de mayor prioridad.
        :return: Elemento eliminado
        :raise IndexError: Si la cola está vacía
        """
        assert not self.is_empty(), 'El agregado está vacío'
        self._prioridad.pop(0)  
        return self._elements.pop(0)
   
    def remove_all(self) -> List[E]:
        removed_elements = []
        while not self.is_empty():
            removed_elements.append(self.remove())
        return removed_elements
    
    def add_all(self, ls: List[Tuple[E, P]]) -> None:
        """
        Agrega todos los elementos y sus prioridades a la cola.
        :param ls: Lista de tuplas (elemento, prioridad, )
        """
        for e, prioridad in ls:
            self.add(e, prioridad)
    

    def decrease_priority(self, e: E, new_priority: P) -> None:
        """
        Reduce la prioridad del elemento en la cola. El elemento debe estar en la cola, y la nueva prioridad debe ser menor
        :param e: Elemento a reducir prioridad.
        :param new_priority: Prioridad nueva para el elemento
        """
        if e in self._elements:
            index = self._elements.index(e)
            current_priority = self._prioridad[index]
            if new_priority < current_priority: 
                self.remove()  
                self.add(e, new_priority)  
      

    def __repr__(self) -> str:
        return "ColaDePrioridad[" + ", ".join(f"({e}, {p})" for e, p in zip(self._elements, self._prioridad)) + "]"