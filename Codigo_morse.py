"""
CÓDIGO MORSE

Crea un programa que sea capaz de transformar texto natural a código
morse y viceversa.
Debe detectar automáticamente de qué tipo se trata y realizar
la conversión.
En morse se soporta raya "—", punto ".", un espacio " " entre letras
o símbolos y dos espacios entre palabras "  ".
El alfabeto morse soportado será el mostrado en
https://es.wikipedia.org/wiki/Código_morse.

"""

# Definimos un diccionario que contiene los caracteres y su correspondiente código morse
MORSE_CODE_DICT = { 'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

# Función que convierte texto natural a código morse
def texto_a_morse(texto):
    morse = ""
    for char in texto:
        if char != " ":
            morse += MORSE_CODE_DICT[char.upper()] + " "
        else:
            morse += " "
    return morse

# Función que convierte código morse a texto natural
def morse_a_texto(morse):
    texto = ""
    morse += " "
    inv_dict = {v: k for k, v in MORSE_CODE_DICT.items()}
    morse_char = ""
    for char in morse:
        if char != " ":
            i = 0
            morse_char += char
        else:
            i += 1
            if i == 2:
                texto += " "
            else:
                texto += inv_dict[morse_char]
                morse_char = ""
    return texto

# Solicitamos al usuario el texto que desea convertir
texto = input("Introduzca el texto a convertir: ")

# Detectamos automáticamente si el texto es código morse o texto natural y realizamos la conversión correspondiente
if "-" in texto or "." in texto:
    resultado = morse_a_texto(texto)
    print("El texto en código morse es:", resultado)
else:
    resultado = texto_a_morse(texto)
    print("El código morse del texto es:", resultado)
