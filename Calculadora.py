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

# Función para salir del programa
def salir():
    print("Saliendo del programa...")
    exit()




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
        
        if opcion == "1":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(suma(num1, num2))
        elif opcion == "2":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(resta(num1, num2))
        elif opcion == "3":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            print(multiplicacion(num1, num2))
        elif opcion == "4":
            num1 = float(input("Introduce el primer número: "))
            num2 = float(input("Introduce el segundo número: "))
            if num2 == 0:
                print("Error: División por cero")
            else:
                print(division(num1, num2))
        elif opcion == "5":
            salir()

if __name__ == "__main__":
    calculadora()
    