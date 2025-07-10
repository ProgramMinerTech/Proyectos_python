"""
        TUPLES
"""

my_tuple = tuple()
my_other_tuple = ("Hola", 6, "Jose", "Vemtura")

my_tuple = (35, 1.77, "Aaron", "Tumba")
print(my_tuple)
print(type(my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
#print(my_tuple[4]) IndexError
#print(my_tuple[-6]) IndexError
print(my_tuple.count("Aaron"))
print(my_tuple.index("Tumba"))

#my_tuple[1] = 1.80 No se puede ejecutar debido a que una tupla es inmutable
print(my_tuple + my_other_tuple)

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple[3] = "tumba" #Saldrá error si es que no se pone el valor numero 3 uvicado en la tupla
my_tuple.insert(1, "Jose")
my_tuple = tuple(my_tuple)

del my_tuple
#print(my_tuple) elimina la variable


