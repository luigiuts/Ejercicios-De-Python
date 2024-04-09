mensaje = "Hola mundo"
MensajeInvertido = ""

for i in range(len(mensaje)):
    MensajeInvertido += mensaje[len(mensaje) - 1 - i]

print(MensajeInvertido)