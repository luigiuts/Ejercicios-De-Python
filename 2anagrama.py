# /*
#  * Escribe una función que reciba dos palabras (String) y retorne
#  * verdadero o falso (Bool) según sean o no anagramas.
#  * - Un Anagrama consiste en formar una palabra reordenando TODAS
#  *   las letras de otra palabra inicial.
#  * - NO hace falta comprobar que ambas palabras existan.
#  * - Dos palabras exactamente iguales no son anagrama.
#  */
def Anagrama (Palabra1, Palabra2):
    if Palabra1 == Palabra2:
        return False
    else:
        palabra1list = list(Palabra1)
        palabra2list = list(Palabra2)
        palabra1list.sort()
        palabra2list.sort()
        if palabra1list == palabra2list:
            return True
    
if Anagrama("mora","roma"):
    print("Es un anagrama")
else:
    print("Las palabras no son anagramas")