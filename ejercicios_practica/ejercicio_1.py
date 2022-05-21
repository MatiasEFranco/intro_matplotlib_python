# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot")

    # NOTA: aproveche los ejemplos de "line_plot" de clase

    # Se desea graficar los valores de "x" e "y" en un gráfico de línea
    # A continuación los datos ya disponibles de "x" e "y" para que utilice:
    x = list(range(-10, 11, 1))

    # Bucle que completa y calcula todos los valores de "y"
    y = []
    for i in x:
        y.append(i**2)

    # Alumno: Crear una "figura" y crear un "ax" con add_subplot
    # Graficar el "line plot" de "y" en función de "x"
   
    # Alumno: Colocar la leyenda y el label con el nombre de la función
    # Darle color a la línea a su elección

    # Crear acá su gráfico
    
    fig = plt.figure()                  # Definir tamaño figura
    ax = fig.add_subplot()              # Definir cuantos gráficos tendrá

    ax.plot(x, y, color='k', marker='.', label= 'y=x**2')   # Graficar con plot en mi gráfico "ax"
    ax.set_facecolor('whitesmoke')      # color de fondo
    ax.set_title("Cuadratica")          # titulo
    ax.set_ylabel("Eje Y")              # nombre a la etiqueta Y
    ax.set_xlabel("Eje X")              # nombre a la etiqueta X
    ax.legend()                         # mostramos la leyenda
    plt.show()                          # mostramos el grafico

    
    print("terminamos")
