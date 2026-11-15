#Tablero alfanumerico para mostrar al jugador
# Crear un tablero vacío de 10x10 (letras A-J, números 1-10)
#Le preguntamos a la IA - GEMINI

# 1. Definir letras y números
letras = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
numeros = range(1, 11)

# 2. Crear el diccionario (¡en líneas separadas!)
tablero = {}
for letra in letras:
    for numero in numeros:
        tablero[(letra, numero)] = "~"  # '~' representa agua

# 3. ¡Pintar el tablero en pantalla!
# Primero, imprimimos la cabecera con las letras
print("      " + "   ".join(letras))
print("    " + "----" * len(letras) + "-")

# Luego, recorremos número por número para pintar cada fila
for numero in numeros:
    # Creamos el texto de la fila empezando por el número
    fila_str = f"{numero:2d} |"
    for letra in letras:
        # Añadimos lo que hay en el diccionario para esa coordenada
        fila_str += f"  {tablero[(letra, numero)]} "
    print(fila_str)