'''
Created on 12 oct 2024

@author: gonza
'''
def Funcion1_6(file:str,separador:str,palabra:str) -> int:
    with open(file,encoding='UTF-8') as f:
        r:list[str] = []
        contador:int = 0
        for linea in f:
            for p in linea.split(separador):
                p = p.strip()
                if len(p) > 0:
                    r.append(p.lower())
    print (r)
    for i in r:
        if i  == palabra:
            contador = contador + 1
      
    return contador


if __name__ == '__main__':
    
    palabra = "quijote"
    separador = " "
    resultado = Funcion1_6("lin_quijote.txt" , separador , palabra)
    print(f'La palabra {palabra} se repite {resultado}')