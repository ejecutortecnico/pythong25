import csv
respuestas = {}

with open("respuestaschat.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        respuestas[fila["preguntas"]] = fila["respuestas"]

def generar_respuesta(pregunta):
    if pregunta in respuestas:
        return respuestas[pregunta]
    else:
        return "lo siento no puedo ayudarte"

def entrenar():
    with open("respuestaschat.csv", "a", newline="") as archivo:
        escritor = csv.writer(archivo)
        pregunta = input("ingresa la pregunta: ")
        respuesta = input("ingresa la respuesta: ")
        escritor.writerow([pregunta, respuesta])

print("hola soy un chatbot de servicio al cliente")

while True:
    pregunta = input("Hola en que puedo ayudarte: ")
    if pregunta == "salir":
        print("hasta luego")
        break
    if pregunta == "entrenar":
        entrenar()
    respuesta = generar_respuesta(pregunta)
    print(respuesta)