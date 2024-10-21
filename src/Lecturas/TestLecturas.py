'''
Created on 21 oct 2024

@author: carlo
'''
from Lecturas.lecturas import funcion1_6, funcion2_7, funcion3_8, longitud_promedio_lineas


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