# /*
#  * Escribe un programa que se encargue de comprobar si un número es o no primo.
#  * Hecho esto, imprime los números primos entre 1 y 100.
#  */

NumeroPrimo = int(input("Introduce un numero primo:"))
if NumeroPrimo < 2:
    print(f"El numero {NumeroPrimo} no es primo")
else:
    es_primo = True
    for i in range(2, NumeroPrimo):
        if NumeroPrimo % i == 0:
            es_primo = False
            break
        
    if es_primo:
        print(f"El numero {NumeroPrimo} es primo")
    else:
        print(f"El numero {NumeroPrimo} no es primo")
    