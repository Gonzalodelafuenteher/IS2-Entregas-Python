### **Cuándo usar `dataclass` en el diseño de tipos en Python**

La anotación `@dataclass` en Python se utiliza cuando queremos definir clases simples que representan datos. Es especialmente útil para simplificar el código y hacer que sea más legible, ya que Python genera automáticamente métodos básicos como `__init__`, `__str__` y `__eq__` (entre otros). A continuación, se detalla cuándo y por qué utilizar `dataclass`.

----------

#### **Cuándo usar `dataclass`:**

1.  **Clases inmutables o centradas en datos:**
    
    -   Si la clase es principalmente un contenedor de datos sin lógica compleja.
    -   Ejemplo: representar un punto en el espacio, una coordenada o una entidad con atributos fijos.
2.  **Cuando los métodos por defecto son suficientes:**
    
    -   Si solo necesitas los métodos básicos (como inicialización, comparación o representación en texto) que Python genera automáticamente con `dataclass`.
3.  **Cuando necesitas ordenar instancias:**
    
    -   Si los objetos de la clase necesitan ser comparados u ordenados, puedes activar la generación automática de métodos como `__lt__`, `__le__`, etc., usando el parámetro `order=True`.
4.  **Para mejorar la claridad del código:**
    
    -   Si deseas un código más limpio y conciso, evitando la escritura repetitiva de métodos como `__init__`.
5.  **Cuando el modelo es inmutable:**
    
    -   Si necesitas objetos inmutables, puedes usar el parámetro `frozen=True`. Esto evita que los atributos sean modificados después de la creación.

----------

#### **Ejemplo simple con `dataclass`:**

```python
from dataclasses import dataclass

@dataclass(frozen=True)
class Punto:
    x: float
    y: float

```

Aquí, `Punto` es una clase inmutable que representa coordenadas. No es necesario escribir el constructor, y los métodos básicos ya están disponibles.

----------

#### **Cuándo usar `class` en lugar de `dataclass`:**

1.  **Si la clase tiene lógica compleja:**
    
    -   Si contiene métodos con mucha funcionalidad o procesos internos que van más allá de un simple almacenamiento de datos.
2.  **Si necesitas herencia compleja:**
    
    -   Aunque `dataclass` soporta herencia, no es ideal para modelos complicados donde las relaciones entre clases son intrincadas.
3.  **Cuando controlas todos los métodos manualmente:**
    
    -   Si necesitas personalizar completamente métodos como `__init__`, `__str__` o `__eq__`.
4.  **Cuando el comportamiento interno de los atributos es dinámico:**
    
    -   Si los valores cambian según métodos complejos o hay dependencia entre atributos.

----------

#### **Ejemplo con `class`:**

```python
class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14159 * self.radio ** 2

    def perimetro(self):
        return 2 * 3.14159 * self.radio

```

Aquí, `Circulo` no es una simple estructura de datos, ya que tiene lógica asociada a sus métodos, por lo que una clase regular es más adecuada.

----------

### **Resumen:**

-   Usa `@dataclass` para clases simples centradas en datos, especialmente si deseas inmutabilidad y métodos generados automáticamente.
-   Usa `class` para diseños más complejos, con lógica interna y personalización detallada.
