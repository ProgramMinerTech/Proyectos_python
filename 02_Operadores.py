"""
Operadores
"""
# Calculamos el VPN de un año

c = 2000
r = 0.1
t = 1
vp = c / (1 + 0.1) ** t
print(vp)
print(f"El valor del VP es {vp:.2f} U$S")

# Suma
a = 22
b = 32
suma = a + b
print(f"La suma de a + b es {suma}.")

# Resta
resta = a - b
print(f"La resta de a - b es {resta}.")

# Multiplicación
multiplicacion = a * b
print(f"La multiplicación de a * b es {multiplicacion}.")

# División
division = a / b
print(f"La división entre a / b es {division}.")
print(f"La división de a / b es {division:.2f}.")

# Potenciación
potencia_1 = a ** b
potencia_2 = b ** a
print(f"La potencia de a^b es {potencia_1:.2e}.")
print(f"La potencia de b^a es {potencia_2:.2e}.")

# Raiz
raiz_1 = a ** (1/b)
raiz_2 = b ** (1/a)
print(f"La potencia de a^(1/b) es {raiz_1}.")
print(f"La potencia de b^(1/a) es {raiz_2}.")

# Modulo
modulo_1 = a % b
modulo_2 = b % a
print(f"El modulo de a % b es {modulo_1}.")
print(f"El modulo de b % a es {modulo_2}.") # Es el residuo de una división entera

# Flor división (división entera)
division_entera_1 = a // b
division_entera_2 = b // a
print(f"La división entera entre a // b es {division_entera_1}.")
print(f"La división entera entre b // a es {division_entera_2}.")

# Operacion con string (str)
print("Hola," + " Aaron " + "¿Que Tal?")
print("Hola " + str(5))
print(5 * "Hola ")
print(2 ** 3 * "Hola ")
print(int(2.5 * 2) * "Hola ")

# Operadores comparativos
print(5 < 4) # Menor que
print(5 > 4) # Mayor que
print(5 <= 4) # Menor igual que 
print(5 >= 4) # Mayor igual que
print(5 == 4) # Igual a 
print(5 != 4) # No es igual a 
print(4 > 3 == 3)
print(4 > 3 != 3)


print("Aaron" < "hola")
print("Aaron" > "hola")
print("aaaa" > "AAAA") # Ordena de manera alfabetica por ASCII
print("Aaron" <= "hola")
print("Aaron" >= "hola")
print("Aaron" == "hola")
print("Aaron" != "hola")

# Operadores Lógicos
print(4 < 5 and 6 < 7)
print(4 < 5 or 6 > 7)
print(4 < 5 and 6 > 7)
print(4 < 5 or 6 < 7)
print(not(4 < 5 and 6 < 7))
print(not(4 < 5 and 6 > 7)) # Para el NOT se debe de hacer de esta manera