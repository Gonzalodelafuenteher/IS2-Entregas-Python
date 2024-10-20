'''
Created on 12 oct 2024

@author: gonza
'''
def funcion1_6(file:str,separador:str,palabra:str) -> int:
    with open(file,encoding='UTF-8') as f:
        r:list[str] = []
        contador:int = 0
        for linea in f:
            for p in linea.split(separador):
                p = p.strip()
                if len(p) > 0:
                    r.append(p.lower())
    for i in r:
        if i  == palabra:
            contador = contador + 1
      
    return contador

def funcion2_7 (file:str, palabra:str)-> list[str]:
    with open (file, encoding = 'UTF-8') as f:
        suma_lineas:list[str] = []
        palabra = palabra.lower()
        for linea in f:
            for p in linea.split(' '):
                p = p.strip().lower()
                if p == palabra:
                    suma_lineas.append(linea.strip())
                    
    return suma_lineas    

def funcion3_8 (file:str)-> set[str]:
    with open (file, encoding = 'UTF-8') as f:
        r = set()
        for linea in f:
            for p in linea.split(" "):
                p = p.strip()
                if len(p) > 0:
                    r.add(p)
    return r  


def longitud_promedio_lineas(file_path: str) -> float:
    with open (file_path, encoding = 'UTF-8') as f:
        longitud_lineas = 0
        longitud_total = 0
        for linea in f:
            longitud_lineas = longitud_lineas +len(linea.split(","))
            longitud_total = longitud_total + 1
        if longitud_total == 0:
            return print("none")
    return longitud_lineas/longitud_total  
    
    
      
      
        
if __name__ == '__main__': 
    print ('################################################')
    print("TEST DE LA FUNCION 6: ")
    palabra = "quijote"
    file1 =  '../../'  + "Resources/lin_quijote.txt"
    separador = " "
    resultado = funcion1_6(file1 , separador , palabra)
    print(f'El número de veces que aparece la palabra {palabra} en el fichero {file1} es: {resultado} \n')
    
    
    print ('################################################')
    print("TEST DE LA FUNCION 7: ")
    palabra2 = "quijote"
    file2 = '../../'  + "Resources/lin_quijote.txt"
    resultado2 = funcion2_7(file2 , palabra2)
    print (f' Las líneas en las que aparece la palabra {palabra2} son: {resultado2} \n')
    
    
    print ('################################################')
    print("TEST DE LA FUNCION 8: ")

    file3 = '../../'  + "Resources/archivo_palabras.txt"
    resultado3 = funcion3_8(file3)
    print (f'Las palabras únicas en el fichero {file3} son: {resultado3} \n')

    print ('################################################')
    print("TEST DE LA FUNCION 9: ")
    file4 = '../../'  + "Resources/palabras_random.csv"
    file5 = '../../'  + "Resources/vacio.csv"
    resultado4 = longitud_promedio_lineas(file4)
    resultado5 = longitud_promedio_lineas(file5)
    print(f'La longitud promedio de las líneas del fichero {file4} es: {resultado4} \n')
    
    print("TEST DE LA FUNCION 9: ")
    print(f'La longitud promedio de las líneas del fichero {file5} es: {resultado5}')

