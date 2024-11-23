import csv

# Abrir el archivo CSV
with open("respuestaschat.csv", "r") as archivo:
    lector = csv.reader(archivo)
    for fila in lector:
        print(fila)  # Imprime cada fila como una lista

# Leer un CSV con encabezados
with open("respuestaschat.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila)  # Imprime cada fila como un diccionario

with open("respuestaschat.csv", "r") as archivo:
    lector = csv.DictReader(archivo)
    for fila in lector:
        print(fila["preguntas"], fila["respuestas"])  # Accede a columnas específicas