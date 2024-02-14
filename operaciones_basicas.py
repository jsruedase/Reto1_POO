def operaciones_basicas(num1, num2, operacion):
    """
    Explicación: Primero se crea el main y se pide al usuario que ingrese los dos numeros, que pueden ser decimales, y la operación. Si la operación que se ingresa no está
    dentro de las opciones, retorna un string donde dice que elija la opción correcta.
    """
    if operacion == "+":
        return num1 + num2
    elif operacion == "-":
        return num1-num2
    elif operacion == "*":
        return num1 * num2
    elif operacion == "/":
        return num1 / num2
    else:
        return "Elija una operación correcta"
    
if __name__ == "__main__":
    num1 = float(input("Ingrese un primer número: "))
    num2 = float(input("Ingrese un segundo número: "))
    operacion = input("Ingrese una operación (+, -, *, /): ")
    resultado = operaciones_basicas(num1, num2, operacion)
    print(resultado)