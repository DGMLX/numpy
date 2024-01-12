#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np
import matplotlib.pyplot as plt


# In[6]:


lista = [1,2,3,4,5]
arr = np.array(lista)
arr


# In[23]:


#Arreglo de una dimension
arr.ndim


# In[17]:


lista2d = [[1,2,3,4,5],
            [6,7,8,9,10]]
arr2d = np.array(lista2d)
arr2d



# In[18]:


# Saber estructura del arreglo
arr2d.shape


# In[19]:


#Saber dimension del arreglo
arr2d.ndim


# In[21]:


#Tipo de dato que contiene al arreglo
arr2d.dtype


# In[22]:


#Numero de valores que contiene el arreglo
arr2d.size


# In[27]:


#Creacion de arreglos 0 y 1 con estructura 3x2
np.zeros((3,2))
np.ones((3,2))


# In[29]:


#Creacion de arreglo de una dimension con los primeros 10 valores
arreglo = np.arange(10)
arreglo


# In[31]:


#Creacion de arreglo de dos dimensiones con los primeros 10 valores con forma 2x5
arreglo2d = np.arange(10).reshape(2,5)
arreglo2d


# In[32]:


#Creacion de array con valores del 10 al 20 con un paso de 2 en 2
np.arange(10,20,2)


# In[33]:


#Crear un array del 10 al 20 con 50 valores, usando linspace los valores se dividen equitativamente, incluye el 10 y el 20 
np.linspace(10,20,50)


# In[35]:


from numpy import pi
#Crear un array con 100 numeros entre 0 y 2pi
np.linspace(0,2*pi,100)


# In[38]:


#seno y coseno del arreglo anterior
from numpy import pi
arr = np.linspace(0,2*pi,100)
seno = np.sin(arr)
coseno = np.cos(arr)
#graficar seno y coseno 
plt.plot(seno,coseno)
plt.show()


# In[41]:


#suma de arreglos de una dimension
a = np.linspace(10,20,6)
b = np.linspace(5,25,6)
suma = a + b
suma


# In[52]:


#Union de ambos arreglos en variable c
c = np.concatenate((a,b))
c


# In[56]:


#Ordenar de menor a mayor los datos
ordenados = np.sort(c)
ordenados


# In[64]:


#Generar un arreglo de 1000 numeros aleatorios entre 0 y 1
rg = np.random.default_rng(2)
aleatorios = rg.random(1000)
aleatorios


# In[68]:


#Generar 2000 numeros enteros aleatorios entre 0 y 19

aleatoriosInt = rg.integers(20,size=2000)
aleatoriosInt


# In[69]:


#Grafico de estos 2000 numeros
plt.hist(aleatoriosInt)
plt.show()


# In[73]:


#Generar 10 numeros aleatorios sin repetir entre 0 y 25
arrNoRepite = rg.choice(26,size=10,replace=False)
arrNoRepite


# In[74]:


#Funciones estadisticas con numpu
#Generar 8 enteros aleatorios de 0 a 19
rg = np.random.default_rng(2)
arr = rg.integers(20,size=8)
arr


# In[81]:


#Obtener valor minimo , maximo , promedio , desviacion estandar , suma total de los numeros del arreglo
arr.min()
arr.max()
arr.mean()
arr.std()
arr.sum()


# In[85]:


#Extraccion de datos a partir de un arreglo de dos dimensiones
arr2d = rg.integers(20,size=(5,4))
arr2d


# In[86]:


#Obtener el valor minimo de cada columna
arr2d.min(axis=0)


# In[88]:


#Obtener el valor maximo de cada fila
arr2d.max(axis=1)


# In[90]:


#Filtrar valores, obtener todos los valores menores a 12 en un array 
arr2d[arr2d<12]


# In[93]:


#Apilamiento de arreglos
n1 = rg.integers(20,size = (3,3))
n2 = rg.integers(20, size = (3,3))

print(n1)
print("---------")
print(n2)


# In[96]:


#Apilamiento vertical
np.vstack((n1,n2))


# In[97]:


#Apilamiento horizontal
np.hstack((n1,n2))


# In[98]:


#Seleccion de valores en arreglos
#Generamos un arreglo con 10 enteros aleatorios
arr = rg.integers(20,size = 10)
arr


# In[99]:


#Obtener los 6 primeros valores
arr[:6]


# In[100]:


#Obtener los valores en la posicion 0,2,4
arr[0:6:2]


# In[101]:


#Seleccionar todos los valores en indice de 2 en 2
arr[::2]


# In[102]:


#Generamos un arreglo de dos dimensiones 8,5 
arr2d = rg.integers(20,size=(8,5))
arr2d


# In[103]:


#obtener el cuarto valor del segundo arreglo
arr2d[1,3]


# In[104]:


#obtener el segundo valor de los arreglos con indice 3,4,5
arr2d[3:6,1]


# In[105]:


##obtener el los 2 primeros valores de los arreglos con indice 4,5,6
arr2d[4:7,0:2]

