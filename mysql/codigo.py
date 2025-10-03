# Este código solicita tu nombre y luego te saluda.

def saludar_usuario():
    """
    Función que pide el nombre al usuario y muestra un saludo personalizado.
    """
    try:
        # Pide al usuario que ingrese su nombre
        nombre = input("Por favor, ingresa tu nombre: ")

        # Verifica si el nombre no está vacío
        if nombre:
            # Imprime el saludo usando una f-string
            print(f"¡Hola, {nombre}! ¡Bienvenido a Python!")
            print("Este es un código de Python muy básico.")
        else:
            print("No ingresaste ningún nombre. ¡Hasta pronto!")

    except Exception as e:
        # Manejo de errores básico
        print(f"Ocurrió un error: {e}")

# Llamar a la función para ejecutar el código
if __name__ == "__main__":
    saludar_usuario()
