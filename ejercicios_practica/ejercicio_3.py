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
    print("Scatter Plot")

    # NOTA: aproveche los ejemplos "scatter_plot" de clase

    # Se desea graficar la función tanh para el siguiente
    # intervalor de valores de "X"
    x = np.arange(-np.pi, np.pi, 0.1)

    # Función y = tanh(x) --> tangente hiperbólica
    y = np.tanh(x)

    # Alumno: Graficar la función utilizando "scatter"
    # utilizando "x" e "y" ya disponible

    # Colocar la leyenda y el label con el nombre de la función

    # Elegir un marker a elección

    # Crear acá su gráfico

    fig = plt.figure()
    fig.suptitle('Tangente Hiperbólica', fontsize=16)    # colocamos el titulo
    ax1 = fig.add_subplot()

    ax1.scatter(x, y, marker='.', label= 'y = tanh(x)', c='darkcyan') # grafica de puntos difernecias con "plot"
    ax1.set_facecolor('whitesmoke')
    ax1.grid('solid')
    ax1.legend()                    # mostramos la leyenda
    plt.show()                      # mostramos el grafico

    print("terminamos")
