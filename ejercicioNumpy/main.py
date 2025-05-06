"""
Que es Numpy?
Numpy es una libreria de Python 
que permite trabajar con arreglos multidimensionales y matrices,
ademas de contar con una gran cantidad de funciones matematicas para operar sobre estos arreglos.
"""

"""
ndim: numero de ejes (dimensionales del array).
shape: una tupla de enteros indicando el tamaño del array en cada dimension. 
size: el número total de elementos del array.
dtype: es un objeto que describe el tipo de elementos de una array.
itemsize: el tamaño en bytes de cada elemento del array.
data: el buffer de datos subyacente que contiene los elementos del array.
"""
import numpy as np

a = np.array([1,2,3,4,5])

print("array: ", a)
print("número de dimensiones",a.ndim)
print("forma del array",a.shape)
print("tamaño del array",a.size)
print("tipo de datos",a.dtype)
print("tamaño de cada elemento en bytes",a.itemsize)