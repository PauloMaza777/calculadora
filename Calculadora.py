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


# Función principal para la calculadora
def calculadora():
    print("Calculadora básica")
    while True:
        print("Opciones:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        opcion = input("Elige una opción (1/2/3/4/5): ")
    