"""
String
"""
my_string = "Mi string"
my_other_string = "Mi otro string"

print(len(my_string))
print(len(my_other_string))
print(my_string + my_other_string)
print(my_string + " " + my_other_string)
print("Hola \nmi nombre es aaron") # El "\n" se coloca junto a la nueva linea
print("\t Hola") # Es con un espacio o tabulación

# Formateo
name = "Aaron"
lastname = "Tumba"
print(f"Mi nombre es {name} y mi lastname es {lastname}")
print("Mi nombre es %s y mi lastname es %s" %(name, lastname))
print("Mi nombre es {} y mi lastname es {}".format(name, lastname))

# Desempaquetado de caracteres
lenguaje = "Aaron"
a, b, c, d, e = lenguaje # La cantidad de variables es la cantidad de caracteres del string guardado en la variable
print(a)
print(b)
print(c)
print(d)
print(e)


# División
division = lenguaje[1:4] # Acá solo hay 3 caracteres (Considera el valor 1 pero no el valor 4, es como n-1; 4 - 1 = 3)
slice = lenguaje[-2]
print(division)
print(slice)

# Reverse
reverse = lenguaje[::-1]
print(reverse)

# Funciones
print(lenguaje.capitalize())
print(lenguaje.upper())
print(lenguaje.count("A"))
print(lenguaje.isnumeric())
print("1".isnumeric())
print(lenguaje.lower())
print(lenguaje.upper().isupper())
print(lenguaje.lower().islower())
print(lenguaje.lower().isupper())