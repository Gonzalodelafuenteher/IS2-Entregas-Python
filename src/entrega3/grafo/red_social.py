from __future__ import annotations

from dataclasses import dataclass
from typing import Dict
from datetime import date, datetime
from entrega3.grafo.recorridos import *
from entrega3.grafo.grafon import *


@dataclass(frozen=True)
class Usuario:
    dni: str
    nombre: str
    apellidos: str
    fecha_nacimiento: date
    
    @staticmethod
    def of(dni: str, nombre: str, apellidos: str, fecha_nacimiento: date) -> 'Usuario':
        # Crear una nueva instancia de Usuario utilizando los parámetros proporcionados
        return Usuario(dni=dni, nombre=nombre, apellidos=apellidos, fecha_nacimiento=fecha_nacimiento)
    
    def __str__(self) -> str:
        # Devuelve una representación en formato de cadena del usuario
        return f"Usuario(dni={self.dni}, nombre={self.nombre}, apellidos={self.apellidos}, fecha_nacimiento={self.fecha_nacimiento})"

@dataclass(frozen=True)
class Relacion:
    id: int
    interacciones: int
    dias_activa: int
    __n: int = 0 # Contador de relaciones. Servirá para asignar identificadores únicos a las relaciones.

    @staticmethod
    def of(interacciones: int, dias_activa: int) -> 'Relacion':
        # Incrementar el contador global y asignar un nuevo ID
        Relacion.__n += 1
        return Relacion(Relacion.__n, interacciones, dias_activa)

    def __str__(self) -> str:
        # Representación en formato de texto de una relación
        return f"Relacion(id={self.id}, interacciones={self.interacciones}, dias_activa={self.dias_activa})"
        

class Red_social(Grafo[Usuario, Relacion]):
    """
    Representa una red social basada en el grafo genérico.
    """
    def __init__(self, es_dirigido: bool = False) -> None:
        super().__init__(es_dirigido)
        '''
        usuarios_dni: Diccionario que asocia un DNI de usuario con un objeto Usuario.
        Va a ser útil en la lectura del fichero de relaciones para poder acceder a los usuarios
        '''
        self.usuarios_dni: Dict[str, Usuario] = {}

    @staticmethod
    def of(es_dirigido: bool = False) -> Red_social:
        """
        Método de factoría para crear una nueva Red Social.
        
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        return Red_social(es_dirigido)

    @staticmethod
    def parse(f1: str, f2: str, es_dirigido: bool = False) -> Red_social:
        """
        Método de factoría para crear una Red Social desde archivos de usuarios y relaciones.
        
        :param f1: Archivo de usuarios.
        :param f2: Archivo de relaciones.
        :param es_dirigido: Indica si la red social es dirigida (True) o no dirigida (False).
        :return: Nueva red social.
        """
        red_social = Red_social.of(es_dirigido=es_dirigido)

    # Procesar usuarios
        with open(f1, 'r') as archivo_usuarios:
            for linea in archivo_usuarios:
                datos = linea.strip().split(',')
                dni, nombre, apellido, fecha_str = datos
                fecha = datetime.strptime(fecha_str, '%Y-%m-%d')
                usuario = Usuario.of(dni, nombre, apellido, fecha)
                red_social.usuarios_dni[dni] = usuario
                red_social.add_vertex(usuario)
        with open(f2, 'r') as archivo_relaciones:
            for linea in archivo_relaciones:
                datos = linea.strip().split(',')
                dni1, dni2, tipo_relacion, fecha_relacion = datos
                relacion = Relacion.of(tipo_relacion, fecha_relacion)
                red_social.add_edge(red_social.usuarios_dni[dni1],red_social.usuarios_dni[dni2],relacion)
    
        return red_social
    
if __name__ == '__main__':
    raiz = ''
    rrss = Red_social.parse(raiz+'usuarios.txt', raiz+'relaciones.txt', es_dirigido=False)
    camino = bfs(rrss, rrss.usuarios_dni['25143909I'], rrss.usuarios_dni['87345530M'])
    g_camino = rrss.subgraph(camino)
    
    g_camino.draw("caminos", lambda_vertice=lambda v: f"{v.dni}", lambda_arista=lambda e: e.id)

    print("El camino más corto desde 25143909I hasta 87345530M es:")
    
