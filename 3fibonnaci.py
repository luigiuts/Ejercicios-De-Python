# /*
#  * Escribe un programa que imprima los 50 primeros números de la sucesión
#  * de Fibonacci empezando en 0.
#  * - La serie Fibonacci se compone por una sucesión de números en
#  *   la que el siguiente siempre es la suma de los dos anteriores.
#  *   0, 1, 1, 2, 3, 5, 8, 13...
#  */
A = 0
B = 1
C = 0

for i in range (1,51):
    if A == 0 and B == 1:
        print(A)
        print(B)
    C=A+B
    print(C)
    A = B
    B = C