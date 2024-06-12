'''
miVariable = 3
print(miVariable)
miVariable = "Hello a todos los estudiantes de la tecnicatura"
print(miVariable)
miVariable = 3.5 
print(miVariable)
x = 10
y = 2
z = x + y
print(id(x))

# Las literales se escriben x056
print(id(z))
print(id(y))

# Tipos de datos

x = 10
print(x)
print(type(x))
x = 14.5
print(x)
print(type(x))
x = "Hola alumnos"
print(x)
print(type(x))
x = True
print(x)
print(type(x))
x = False
print(x)
print(type(x))

# Manejo de cadenas

miGrupoFavorito = "Red hot chili peppers"
caracteristicas = "The best band"
print("Mi grupo favorito es: "+miGrupoFavorito+""+caracteristicas)

numero1 = 7
numero2 = 8
print(int(numero1) + int(numero2))

# Tipos booleanos (bool)

miBooleano = 3 > 4
print(miBooleano)

if miBooleano:
    print("El resultado es verdadero")
else:
    print("El resultado es falso")

# Procesar entrada del usuario
# Función input
resultado = input("Ingrese un valor")
print("El resultado es: ",resultado)

# Conversión del dato de entrada
numero1 = int(input("Escribe el primer número"))
numero2 = int(input("Escribe el segundo número"))
resultado = numero1 + numero2

print("El resultado de la suma es: ",resultado)
'''
'''
#Operadores (clase 4)

operandoA = 8
operandoB = 5
suma = operandoA + operandoB
#print("El resultado de la suma es:",suma)
print(f"El resultado de la suma es: {suma}")

resta = operandoA - operandoB
print(f"El resultado de la resta es: {resta}")

multiplicacion = operandoA * operandoB
print(f"El resultado de la multiplicación es: {multiplicacion}")

division = operandoA / operandoB
print(f"El resultado de la división es: {division}")
division = operandoA // operandoB
print(f"El resultado de la división (int) es: {division}")
modulo = operandoA % operandoB
print(f"El resultado de la división o modulo (residuo) es: {modulo}")
exponente = operandoA ** operandoB
print(f"El resultado del exponente es: {exponente}")
'''
#Calcular área y perímetro de un triángulo
'''
print("Calcula el área y perímetro de un triángulo")
alto = int(input("Ingrese la atura del triángulo"))
ancho = int(input("Ingrese su ancho"))

area = (ancho * alto) / 2
perimetro = (alto + ancho) * 2

print("Área:", area)
print("Perímetro:",perimetro)
'''
"""
#operadores de reasignación
miVariable3 = 10
print(miVariable3)
miVariable3 = miVariable3 + 1
print(miVariable3)

miVariable3 += 1
print(miVariable3)

miVariable3 -= 2
print(miVariable3)
miVariable3 *= 3
print(miVariable3)
miVariable3 /= 2
print(miVariable3)

#Operadores de comparación
d = 4
b = 2
resultado = d==b #comparar si son iguales
print(resultado)

#operador diferente
resultado = d != b
print(resultado)
#operador mayor que
resultado = d > b
print(resultado)
#operador menor que
resultado = d < b
print(resultado)
#operador menor o igual que
resultado = d <= b
print(resultado)
#operador mayor o igual que
resultado = d >= b
print(resultado)
"""
"""
# Operadores lógicos

#and
a = False
b = True
resultado = a and b
print(resultado)

#or
resultado = a or b
print(resultado)

#not
resultado = not a
print(resultado)
"""

"""
#Ejercicio: valor dentro de un rango

valor = int(input("Digite un número:"))
valorMinimo = 0
valorMaximo = 5
dentroRango = (valor >= valorMinimo and valor <= valorMaximo)
if dentroRango:
    print(f"El valor {valor} se encuentra dentro del rango")
else:
    print(f"El valor {valor} se encuentra fuera del rango")
"""
"""
#Ejercicio operador or (saber si un padre puede asistir al juego del hijo), operador not

vacaciones = True
diaDescanso = False
if not (vacaciones or diaDescanso):
    print("Puede asistir al juego")
else:
    print("No puede asistir, tiene trabajo que hacer")"""
"""
#Ejercicio rango de edad 20-30

edadUsuario = int(input("Ingrese su edad"))
edadMinima = 20
edadMaxima = 30
rangoEdad = (edadUsuario >= edadMinima and edadUsuario <= edadMaxima)
if rangoEdad:
    print(f"Su edad {edadUsuario} se encuentra dentro del rango 20-30")
else:
    print(f"Su edad {edadUsuario} está fuera del rango 20-30")
"""
#El mayor de dos números

numero1 = int(input("Digite un número: "))
numero2 = int(input("Digite otro número: "))

if numero1 > numero2:
    print(f"El numero {numero1} es mayor")
else:
    print(f"El número {numero2} es mayor")
