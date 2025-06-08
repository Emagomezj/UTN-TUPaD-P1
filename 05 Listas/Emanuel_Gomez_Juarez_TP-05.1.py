from os import system as sys
from utils.fx import exit_test, parse_input
from constants.terminal_colors import blue,green,red,res

# 1. Crear una lista con los números del 1 al 100 que sean múltiplos de 4. Utilizar la función range.

def ej_1():
    sys('cls')
    rang = list(range(4,101, 4))
    print(green+f'La lista resultante es: \n{rang}')
    res()
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 2. Crear una lista con cinco elementos (colocar los elementos que más te gusten) y mostrar el penúltimo. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

def ej_2():
    sys('cls')
    lst = [1,2,3,4,5]
    print(green+f'Penúltimo: \n==>{lst[-2]}')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 3. Crear una lista vacía, agregar tres palabras con append e imprimir la lista resultante por pantalla. Pista: para crear una lista vacía debes colocar los corchetes sin nada en su interior.

def ej_3():
    lst = []
    for i in range(3):
        sys('cls')
        print('Lista:')
        print(blue+f'{lst}')
        res()
        wrd= parse_input(str, 'Por favor ingrese un elemento para la lista: ')
        lst.append(wrd)
    
    sys('cls')
    print('Lista resultante: ')
    print(green+f'{lst}')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 4. Reemplazar el segundo y último valor de la lista “animales” con las palabras “loro” y “oso”, respectivamente. Imprimir la lista resultante por pantalla. ¡Puedes hacerlo como se muestra en los videos o bien investigar cómo funciona el indexing con números negativos!

def ej_4():
    sys('cls')
    animales = ["perro", "gato", "conejo", "pez"]
    animales[1] = 'loro'
    animales[-1] = 'oso'
    print(green+f'Lista resultante: \n  {animales}')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 5. Analizar el siguiente programa y explicar con tus palabras qué es lo que realiza.
def ej_5():
    sys('cls')
    print('Analiza el siguiente programa y explícalo con tus palabras: \nnumeros = [8,15,3,22,7]\nnumeros.remove(max(numeros))\nprint(numeros)\n\n')
    print(green+'El programa crea una lista con valores numéricos, luego elimina el mayor de la misma para finalmente imprimir por pantalla la lista modificada - sin el número que fue removido con remove() -.')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 6. Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros.

def ej_6():
    sys('cls')
    lst = list(range(10,31,5))
    print(green+f'\n{lst[0:2]}')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 7.  Reemplazar los dos valores centrales (índices 1 y 2) de la lista “autos” por dos nuevos valores cualesquiera.

def ej_7():
    autos = ["sedan", "polo", "suran", "gol"]
    for i in range(2):
        wrd= parse_input(str, 'Por favor ingrese un elemento para modificar en la lista: ')
        autos[i+1] = wrd
    sys('cls')
    print('Lista modificada: \n')
    print(green+f'{autos}')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 8. Crear una lista vacía llamada "dobles" y agregar el doble de 5, 10 y 15 usando append directamente. Imprimir la lista resultante por pantalla.


def ej_8():
    dobles = []
    i = 5
    while i < 16:
        dobles.append(i*2)
        i += 5
    sys('cls')
    print('\nDobles: \n')
    print(green+f'{dobles}')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 9.  Dada la lista “compras”, cuyos elementos representan los productos comprados por diferentes clientes:
def ej_9():
    sys('cls')
    compras = [["pan", "leche"], ["arroz", "fideos", "salsa"],["agua"]]
    # a) Agregar "jugo" a la lista del tercer cliente usando append.
    compras[2].append('jugo')
    # b) Reemplazar "fideos" por "tallarines" en la lista del segundo cliente.
    idx = compras[1].index('fideos')
    compras[1][idx] = 'tallarines'
    # c) Eliminar "pan" de la lista del primer cliente.
    compras[0].remove('pan')
    # d) Imprimir la lista resultante por pantalla
    print('\nLista resultante: \n')
    print(green+f'{compras}')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

# 10. Elaborar una lista anidada llamada “lista_anidada” que contenga los siguientes elementos:
# ● Posición lista_anidada[0]: 15
# ● Posición lista_anidada[1]: True
# ● Posición lista_anidada[2][0]: 25.5
# ● Posición lista_anidada[2][1]: 57.9
# ● Posición lista_anidada[2][2]: 30.6
# ● Posición lista_anidada[3]: False
# Imprimir la lista resultante por pantalla.

def ej_10():
    lista_anidada = [15,True,[25.5,57.9,30.6],False]
    sys('cls')
    print('\nlista_anidada: \n')
    print(green+f'{lista_anidada}')
    print(blue+'\nPulse cualquier tecla para salir', end='')
    res()
    parse_input(str)

def main_loop():
    while True:
        sys('cls')
        print('Indique con un número entre 1 o 10 que ejercicio quiere probar. Ingrese E en cualquier momento para salir')
        print('1. números del 1 al 100 que sean múltiplos de 4 \n2. Crear una lista con cinco elementos y mostrar el penúltimo \n3. Crear una lista vacía, agregar tres palabras con append e imprimir la lista. \n4. Remplazar el segundo y último valor de la lista. \n5. Analizar y explicar el programa \n6. Crear una lista con números del 10 al 30 (incluído), haciendo saltos de 5 en 5 y mostrar por pantalla los dos primeros. \n7. Reemplazar los dos valores centrales. \n8. Lista llamada "dobles". \n9. Productos comprados por diferentes clientes. \n10. Lista anidada.')
        opts = list(range(1,11))
        opt = parse_input(int,'',chr(27)+"[0;31m"+'Ingrese una opción válida', lambda x: x in opts)
        if(exit_test(opt)): return
        fx_dict = {
            1: ej_1,
            2: ej_2,
            3: ej_3,
            4: ej_4,
            5: ej_5,
            6: ej_6,
            7: ej_7,
            8: ej_8,
            9: ej_9,
            10: ej_10
        }
        fx_dict[opt]()

main_loop()