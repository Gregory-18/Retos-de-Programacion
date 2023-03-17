"""
Crea una función que reciba dos cadenas como parámetro (str1, str2)
e imprima otras dos cadenas como salida (out1, out2).
out1 contendrá todos los caracteres presentes en la str1 pero NO
estén presentes en str2.
out2 contendrá todos los caracteres presentes en la str2 pero NO
estén presentes en str1.
"""

def diferencia_caracteres(str1, str2):
    # Obtiene los caracteres únicos en str1 que no están en str2
    out1 = ''.join(sorted(set(str1) - set(str2)))
    # Obtiene los caracteres únicos en str2 que no están en str1
    out2 = ''.join(sorted(set(str2) - set(str1)))
    print("out1:", out1)
    print("out2:", out2)

diferencia_caracteres("hola", "adios")