"""
Variables
"""
name = "Aaron Tumba"
print(f"Hola, mi nombre es: {name}")

# Área de un rectángulo

ancho = 20
largo = 50
area = ancho * largo
print(f"El área del rectágunlo es {area} m2")

# Cálculo de número de taladros

ancho_s = 3
largo_s = 3.5
area_s = ancho_s * largo_s * 11/12
perimetro = 4 * area_s ** (1/2)
nt = (perimetro / 0.6) + (1.5 * area_s)
print(f"El número de taladros para una seccion de 3*3.5 es: {nt} taladros.")
print(f"El número de taladros para una seccion de 3*3.5 es: {nt:.2f} taladros.")
print(f"El número de taladros para una seccion de 3*3.5 es: {nt:.0f} taladros.")

# Ingresando datos

a = float(input("Ingrese el ancho de la labor:"))
b = float(input("Ingrese el largo de la labor:"))
c = a * b * 11/12
p = 4 * c ** (0.5)
nt_a = (p / 0.6) + (1.5 * c)
print(f"El número de taladros para una seccion de {a} * {b} es: {nt_a} taladros.")
print(f"El número de taladros para una seccion de {a} * {b} es: {nt_a:.2f} taladros.")
print(f"El número de taladros para una seccion de {a} * {b} es: {nt_a:.0f} taladros.")

print("Son:", nt_a, "taladros.")
