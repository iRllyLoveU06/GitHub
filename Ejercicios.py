

import numpy as np 
import matplotlib.pyplot as plt
import pandas as pd




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

ejer6 = np.random.randint(0,1000,(5,5))
print(ejer6)

minimo = np.min(ejer6)
maximo = np.max(ejer6)

print("\nMinimo: ", minimo)
print("\nMaximo: ", maximo)


#EJERCICIO 7: Normalizar la matriz anterior

ejer7 = (ejer6 - minimo) / (maximo - minimo)
print("\n", ejer7)


#EJERCICIOS DE LA CLASE 10

#1.Cree un vector de size = 720, con valores aleatorios
ejer8 = np.random.rand(720)
print(ejer8)

#2.Haga reshape de (120, 6)
ejer9 = ejer8.reshape((120,6))

#3.Haga la transpuesta de la matriz y cree dos copias, una usando order F y la otra usando order C

ejer10_1 = ejer9.transpose()

ejer10_C = np.array(ejer10_1, order='C',copy=True)
ejer10_F = np.array(ejer10_1, order='F', copy=True)

#4.Genere un subplot con 6 paneles, usando la versión “a mano”, y con proporciones diferentes
x = ejer10_C
y = ejer10_F

plt.figure(figsize=(10, 8)) 

# Panel 1
plt.axes([0.05, 0.7, 0.4, 0.25])
plt.title("Panel 1")

# Panel 2 (más pequeño)
plt.axes([0.55, 0.7, 0.35, 0.25])
plt.title("Panel 2")

# Panel 3 (proporciones distintas)
plt.axes([0.1, 0.4, 0.3, 0.2])
plt.title("Panel 3")

# Panel 4
plt.axes([0.5, 0.4, 0.45, 0.2])
plt.title("Panel 4")

# Panel 5 (ancho completo)
plt.axes([0.1, 0.1, 0.35, 0.2])
plt.title("Panel 5")

# Panel 6
plt.axes([0.55, 0.1, 0.4, 0.2])
plt.title("Panel 6")


#5.En cada panel hacer un grafico diferente (plot, scatter, bar, histograma, pie, etc) , sus datos serán cada fila de la matriz anterior.

plt.figure(figsize=(12, 10))
x = np.arange(ejer10_1.shape[1])

plt.axes([0.05, 0.7, 0.4, 0.25])
plt.plot(x, ejer10_1[0], color='blue')
plt.title("Plot lineal")

plt.axes([0.55, 0.7, 0.4, 0.25])
plt.scatter(x, ejer10_1[1], color='red')
plt.title("Gráfico de dispersión")

plt.axes([0.05, 0.4, 0.4, 0.25])
plt.bar(x[:10], ejer10_1[2, :10], color='green')
plt.title("Gráfico de barras")

plt.axes([0.55, 0.4, 0.4, 0.25])
plt.hist(ejer10_1[3], bins=10, color='purple', edgecolor='black')
plt.title("Histograma")

plt.axes([0.05, 0.1, 0.4, 0.25])
plt.fill_between(x, ejer10_1[4], color='orange', alpha=0.6)
plt.title("Área (fill)")

plt.axes([0.55, 0.1, 0.4, 0.25])
valores = ejer10_1[5, :6]
plt.pie(valores, labels=[f"Cat {i}" for i in range(6)], autopct="%1.1f%%")
plt.title("Gráfico circular (pie)")


#6.Poner títulos, labels,legends, cuadrículas.

import numpy as np
import matplotlib.pyplot as plt

vector = np.random.randint(0, 100, 720)
matriz = vector.reshape(120, 6)
ejer10_1 = matriz.T

plt.figure(figsize=(12, 10))
x = np.arange(ejer10_1.shape[1])

plt.axes([0.05, 0.7, 0.4, 0.25])
plt.plot(x, ejer10_1[0], color='blue', label='Serie 1')
plt.title("Gráfico de línea")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)

plt.axes([0.55, 0.7, 0.4, 0.25])
plt.scatter(x, ejer10_1[1], color='red', label='Serie 2')
plt.title("Gráfico de dispersión")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)

plt.axes([0.05, 0.4, 0.4, 0.25])
plt.bar(x[:10], ejer10_1[2, :10], color='green', label='Serie 3')
plt.title("Gráfico de barras")
plt.xlabel("Categorías")
plt.ylabel("Valor")
plt.legend()
plt.grid(True, axis='y')

plt.axes([0.55, 0.4, 0.4, 0.25])
plt.hist(ejer10_1[3], bins=10, color='purple', edgecolor='black', label='Serie 4')
plt.title("Histograma")
plt.xlabel("Valor")
plt.ylabel("Frecuencia")
plt.legend()
plt.grid(True)

plt.axes([0.05, 0.1, 0.4, 0.25])
plt.fill_between(x, ejer10_1[4], color='orange', alpha=0.6, label='Serie 5')
plt.title("Gráfico de área")
plt.xlabel("Índice")
plt.ylabel("Valor")
plt.legend()
plt.grid(True)

plt.axes([0.55, 0.1, 0.4, 0.25])
valores = ejer10_1[5, :6]
plt.pie(valores, labels=[f"Cat {i}" for i in range(6)], autopct="%1.1f%%")
plt.title("Gráfico circular")

plt.show()


#EJERCICIOS CLASE 12(pandas)

#primer ejercicio: Crear un sistema que almacene equipos biomédicos , cada
#equipo tiene información de nombre, marca, ubicación, fecha
#de calibración ,fecha de mmto ,nombre del proveedor.
#Para ello implementarlo a partir de un dataframe con la
#información anterior


equipos = {
    "Nombre": ["Electrocardiógrafo", "Bomba de Infusión", "Desfibrilador", "Incubadora", "Monitor de Signos"],
    "Marca": ["GE", "Mindray", "Philips", "Dräger", "Nihon Kohden"],
    "Ubicación": ["UCI", "Pediatría", "Urgencias", "Neonatos", "Hospitalización"],
    "Fecha_Calibración": [
        "2025-01-10", "2025-02-18", "2024-12-05", "2025-03-20", "2025-01-30"
    ],
    "Fecha_Mantenimiento": [
        "2025-07-10", "2025-08-18", "2025-06-05", "2025-09-20", "2025-07-30"
    ],
    "Proveedor": ["TecnoSalud", "BioMedics", "ElectroCare", "NeoTec", "VitalMed"]
}


df_equipos = pd.DataFrame(equipos)


df_equipos["Fecha_Calibración"] = pd.to_datetime(df_equipos["Fecha_Calibración"])
df_equipos["Fecha_Mantenimiento"] = pd.to_datetime(df_equipos["Fecha_Mantenimiento"])


print("📋 Inventario de Equipos Biomédicos:\n")
print(df_equipos)


filtro = df_equipos[df_equipos["Fecha_Mantenimiento"] > "2025-06-30"]
print("\n🧰 Equipos con mantenimiento en el segundo semestre del 2025:\n")
print(filtro)


df_equipos.to_csv("equipos_biomedicos.csv", index=False)
print("\n💾 Archivo 'equipos_biomedicos.csv' guardado exitosamente.")


