
respuestas = {
    "hola":"hola como estas",
    "tiene zapatos":"si somos una tienda de zapatos",
    "donde estan ubicados":"estamos ubicados en sotomayor",
    "en que ciudad":"Bucarmanga y otras",
    "direccion":"crr 29 # 50-20"
}

def generar_respuesta(pregunta):
    if pregunta in respuestas:
        return respuestas[pregunta]
    else:
        return "lo siento no puedo ayudarte"


print("hola soy un chatbot de serivicio al cliente")

while True:
    pregunta = input("Hola en que puedo ayudarte: ")
    if pregunta == "salir":
        print("hasta luego")
        break
    respuesta = generar_respuesta(pregunta)
    print(respuesta)