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