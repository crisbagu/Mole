def add(x, y):
    """Suma dos números."""
    return x + y

def subtract(x, y):
    """Resta el segundo número al primero."""
    return x - y

def multiply(x, y):
    """Multiplica dos números."""
    return x * y

def divide(x, y):
    """Divide el primer número por el segundo."""
    if y == 0:
        raise ValueError("No se puede dividir por cero.")
    return x / y

def main():
    print("Selecciona la operación.")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")

    while True:
        choice = input("Ingresa tu elección (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Ingresa el primer número: "))
                num2 = float(input("Ingresa el segundo número: "))
            except ValueError:
                print("Entrada inválida. Por favor, ingresa un número.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                try:
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
                except ValueError as e:
                    print(f"Error: {e}")

            next_calculation = input("¿Quieres hacer otra operación? (sí/no): ")
            if next_calculation.lower() not in ('sí', 'si', 's', 'yes', 'y'):
                break
        else:
            print("Entrada inválida")

if __name__ == "__main__":
    main()
