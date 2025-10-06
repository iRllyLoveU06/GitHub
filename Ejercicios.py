import numpy as np 

#clase numero 9, ejercicios:


#EJERCICIO 1: Crear una matriz de ceros de tipo entero 3x4
ejer1 = np.zeros((3,4))
print(ejer1)

#EJERCICIO 2:Crear una matriz de ceros de tipo entero 3x4 excepto la primera fila que será uno

ejer2 = np.zeros((3,4),int)
ejer2[0,:] = 1
print(ejer2)

#EJERCICIO 3: Crear una matriz de ceros de tipo entero 3x4 excepto la última fila que será el rango entre 5 y 8.

ejer3 = np.zeros((3,4), int)

ejer3[2,:] = np.linspace(5,8,4,True,False,int)
print(ejer3)

#EJERCICIO 4: Crea un vector de 10 elementos, siendo los índices impares unos y los índices pares dos.

ejer4 = np.zeros(10,int)
ejer4[::2] = 2
ejer4[1::2] = 1
print(ejer4)

#EJERCICIO 5: Crea un «tablero de ajedrez», con unos en las casillas negras y ceros en las blancas.

ejer5 = np.zeros((8,8), int)
ejer5[1::2,::2] = 1
ejer5[::2,1::2] = 1 
print(ejer5)
 
#EJERCICIO 6: Crea una matriz aleatoria 5x5 y halla los valores mínimo y máximo.


#EJERCICIO 7: Normalizar la matriz anterior