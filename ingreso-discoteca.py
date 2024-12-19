# Paso 1: Solicitar al usuario que ingrese la edad de su cliente.

# - Convertir de str a int:
edad = int(input("Por favor, ingrese su edad: "))

# Paso 2: Verificar si la edad ingresada cumple con el requisito de acceso a la discoteca.

# Usando un ternario:
permitido = True if edad >= 18 else False

# Paso 3: Mostrar al usuario si el cliente puede o no ingresar a la discoteca.
if permitido:
    print("¡Bienvenido! Que la pases espectacular.")
else:
    print("Lo sentimos, no tienes edad suficiente para entrar.")