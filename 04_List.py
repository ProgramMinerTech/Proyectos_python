"""
List
"""
lista = [5, 7, 9, 11]
my_list = [6, 8, 10, 12]

# Imprimir datos
print(lista)
print(my_list)

# Longitud de listas
print(len(lista))
print(len(my_list))

data = [35, 1.70, "Hola", "Aaron"]

# Verificamos el tipo de variable, en este caso lo considerará como lista
print(type(data))

# Impresion de cada valor de la lista "data", en base al valor de la ubicación de los datos
print(data[0])
print(data[1])
print(data[2])
print(data[3])

# Impresion al inverso
print(data[-1])
print(data[-2])
print(data[-3])
print(data[-4])

# Imprime si es Falso o Verdadero la presencia de la informacion dentro de la lista mediante 0 y 1
print(data.count("Aaron"))

# Imprime la union de ambas listas (solo aplicable con el operador suma)
print(lista + my_list)

# Agregamos un valor mas a la lista
lista.append("Oscar")
print(lista)

# Agrega nuevo dato a la lista, en base a la ubicación que lo ubiques o a su posición
lista.insert(2, "Pepe")
lista.insert(0, 100)
print(lista)

# Elimina el valor que ingresas perteneciente a la lista, sino se encuentra saldrá error
lista.remove(5)
print(lista)

# Permite agregar varios elementos a la lista
lista.extend([12, 23, 52, 55])
print(lista)

# Elimina el ultimo dato, y si colocas el print, te muestra lo que se eliminó
print(lista.pop())
print(lista.pop(2))