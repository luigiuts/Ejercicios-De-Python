# /*
#  * Crea una única función (importante que sólo sea una) que sea capaz
#  * de calcular y retornar el área de un polígono.
#  * - La función recibirá por parámetro sólo UN polígono a la vez.
#  * - Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
#  * - Imprime el cálculo del área de un polígono de cada tipo.
#  */

def calcularAreaPoligono(base,altura):
    return print(f"El area del cuadrado con base {base} y altura {altura} es: {base*altura} \n El area del triangulo con base {base} y altura {altura} es: {(base*altura)/2} \n El area del rectangulo con base {base} y altura {altura} es: {base*altura}")

Base = int(input("Ingrese la base del poligono: "))
Altura = int(input("Ingrese la altura del poligono: "))

calcularAreaPoligono(Base,Altura)