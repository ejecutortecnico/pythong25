def sumar(a, b):
    return float(a) + float(b)

def resta(a, b):
    return float(a) - float(b)

operacion = input("ingrese la operacion que desea realizar")
a = input("ingrese el numero 1")
b = input("ingrese el numero 2")

if operacion == "suma":
    resultado = sumar(a,b)
elif operacion == "resta":
    resultado = resta(a,b)
else:
    print("esa opcion es incorrecta")

print(resultado)  # Imprime 8
            