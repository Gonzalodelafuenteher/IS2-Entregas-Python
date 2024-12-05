from __future__ import annotations
from typing import Optional, Dict, Set, List, Tuple, Type, Callable
from dataclasses import dataclass
from datetime import datetime, date
from collections import Counter
from dateutil.relativedelta import relativedelta
from collections import Counter
# --------------------------
# Clase Persona
# --------------------------
@dataclass(frozen=True, order=True)
class Persona:
    nombre: str
    apellidos: str
    dni: str
    fecha_nacimiento: datetime
    direccion: str
    telefono: str

    @staticmethod
    def parse(linea: str) -> Persona:
        campos = linea.split(",")
        fecha_nacimiento = datetime.strptime(campos[3], "%Y-%m-%d %H:%M:%S")
        return Persona(
            nombre=campos[0],
            apellidos=campos[1],
            dni=campos[2],
            fecha_nacimiento=fecha_nacimiento,
            direccion=campos[4],
            telefono=campos[5],
        )

# --------------------------
# Clase Cuenta
# --------------------------
@dataclass(frozen=True, order=True)
class Cuenta:
    iban: str
    dni: str
    fecha_creacion: datetime
    saldo: float

    @staticmethod
    def parse(linea: str) -> Cuenta:
        campos = linea.split(",")
        fecha_creacion = datetime.strptime(campos[2], "%Y-%m-%d %H:%M:%S")
        return Cuenta(
            iban=campos[0],
            dni=campos[1],
            fecha_creacion=fecha_creacion,
            saldo=float(campos[3])
        )

# --------------------------
# Clase Empleado
# --------------------------
@dataclass(frozen=True, order=True)
class Empleado:
    dni: str
    fecha_contrato: datetime
    salario_mensual: float

    @staticmethod
    def parse(linea: str) -> Empleado:
        campos = linea.split(",")
        fecha_contrato = datetime.strptime(campos[1], "%Y-%m-%d %H:%M:%S")
        return Empleado(
            dni=campos[0],
            fecha_contrato=fecha_contrato,
            salario_mensual=float(campos[2])
        )

    def meses_contratado(self) -> int:
        return relativedelta(datetime.now(), self.fecha_contrato).months

# --------------------------
# Clase Prestamo
# --------------------------
@dataclass(frozen=True, order=True)
class Prestamo:
    nid: int
    dni_cliente: str
    cantidad: float
    fecha_inicio: datetime
    duracion: int
    interes: float
    dni_empleado: str

    @staticmethod
    def parse(linea: str) -> Prestamo:
        campos = linea.split(",")
        fecha_inicio = datetime.strptime(campos[3], "%Y-%m-%d %H:%M:%S")
        return Prestamo(
            nid=int(campos[0]),
            dni_cliente=campos[1],
            cantidad=float(campos[5]),
            fecha_inicio=fecha_inicio,
            duracion=int(campos[4]),
            interes=float(campos[6]),
            dni_empleado=campos[2]
        )

    def fecha_vencimiento(self) -> date:
        return self.fecha_inicio + relativedelta(months=self.duracion)

# --------------------------
# Clase Poblacion
# --------------------------
class Poblacion:
    def __init__(self, tipo_elemento: Type, clave_func: Callable[[Type], str]):
        """
        Crea una colección de elementos de un tipo específico. Para ello se usa un diccionario
        que agrupa los elementos por una clave que se obtiene aplicando una función clave_func a
        cada elemento.
        Por ejemplo, si consideramos una colección de personas y la clave
        es el DNI, la función clave_func sería lambda p: p.dni. 
        Esto es útil para relacionar elementos de diferentes poblaciones. Por ejemplo, si tenemos
        una población de cuentas y otra de personas, podemos relacionarlas a través del DNI de la
        persona.
        
        """
        self._elementos: Dict[str, List[Type]] = {}
        self._tipo_elemento: Type = tipo_elemento
        self._clave_func: Callable[[Type], str] = clave_func

    def agregar(self, elemento: Type) -> None:
        if not isinstance(elemento, self._tipo_elemento):
            raise ValueError(f"Elemento debe ser de tipo {self._tipo_elemento.__name__}")
        clave = self._clave_func(elemento)
        if clave not in self._elementos:
            self._elementos[clave] = []
        self._elementos[clave].append(elemento)

    def obtener(self, clave: str) -> Optional[List[Type]]:
        return self._elementos.get(clave)

    def todos(self) -> List[Type]:
        return [elemento for elementos in self._elementos.values() for elemento in elementos]

# --------------------------
# Clase FactoriaDatos
# --------------------------
class FactoriaDatos:
    @staticmethod
    def cargar_datos(file_path: str, tipo_elemento: Type, clave_func: Callable[[Type], str]) -> Poblacion:
        coleccion = Poblacion(tipo_elemento, clave_func)
        with open(file_path, encoding="utf-8") as f:
            for line in f:
                coleccion.agregar(tipo_elemento.parse(line.strip()))
        return coleccion

# --------------------------
# Clase Banco
# --------------------------
class Banco:
    def __init__(
        self,
        nombre: str,
        codigo_postal: int,
        email: str,
        personas: Poblacion,
        empleados: Poblacion,
        cuentas: Poblacion,
        prestamos: Poblacion
    ):
        self.nombre = nombre
        self.codigo_postal = codigo_postal
        self.email = email
        self.personas = personas
        self.empleados = empleados
        self.cuentas = cuentas
        self.prestamos = prestamos

    def prestamos_de_cliente(self, dni: str) -> List[Prestamo]:
	'''
	Devuelve una lista con todos los préstamos del cliente con el dni especificado
	'''
        pass

    def empleado_mas_longevo(self) -> Optional[Empleado]:
	'''
	Devuelve el empleado que lleva más meses contratado en el banco
	'''
        pass

    def intereses_prestamos(self) -> Tuple[float, float, float]:
	'''
	Devuelve una tupla con el mínimo interés, el máximo interés y la media del interés de todos los préstamos
	'''
        pass

    def media_cantidad_prestamos_cliente(self, dni: str) -> float:
	'''
	Devuelve el importe medio prestado al cliente con el dni indicado. Si el cliente no tiene ningún préstamo
	se devolverá 0	
	'''
        pass

    def clientes_con_multiples_prestamos(self) -> List[Persona]:
	'''
	Devuelve una lista de objetos Persona con aquellos clientes que tienen varios préstamos concedidos
	'''
        pass
        
           
      
# --------------------------
# Tests
# --------------------------
if __name__ == "__main__":
    raiz = "../../"

    personas = FactoriaDatos.cargar_datos(raiz+"data/personas.txt", Persona, lambda p: p.dni)
    empleados = FactoriaDatos.cargar_datos(raiz+"data/empleados.txt", Empleado, lambda e: e.dni)
    cuentas = FactoriaDatos.cargar_datos(raiz+"data/cuentas.txt", Cuenta, lambda c: c.iban)
    prestamos = FactoriaDatos.cargar_datos(raiz+"data/prestamos.txt", Prestamo, lambda p: p.dni_cliente)

    banco = Banco(
        nombre="Banco Ejemplo",
        codigo_postal=41012,
        email="info@bancoejemplo.com",
        personas=personas,
        empleados=empleados,
        cuentas=cuentas,
        prestamos=prestamos,
    )

    print("Préstamos de cliente:")
    for prestamo in banco.prestamos_de_cliente("92784222Z"):
        print(prestamo)
    print("\nEmpleado más longevo:", banco.empleado_mas_longevo())
    print("\nIntereses de préstamos:", banco.intereses_prestamos())

    f1 = datetime.strptime("2023-01-01", "%Y-%m-%d")
    f2 = datetime.strptime("2023-12-31", "%Y-%m-%d")
    print("\nMedia cantidad de préstamos:", banco.media_cantidad_prestamos_cliente("92784222Z"))
    
    print("\nClientes con múltiples préstamos:")
    for cliente in banco.clientes_con_multiples_prestamos():
        print(cliente)
