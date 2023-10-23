# Función para realizar una suma
def suma(num1, num2):
    return num1 + num2
# Función para realizar una resta
def resta(num1, num2):
    return num1 - num2

# Función para realizar una multiplicación
def multiplicacion(num1, num2):
    return num1 * num2

# Función para realizar una división
def division(num1, num2):
    if num2 == 0:
        return "Error: División por cero"
    return num1 / num2