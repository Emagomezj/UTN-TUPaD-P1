import random
import time
import numpy as np
from os import system as sys
from fx import exit_test, parse_input

# 1. Crea un programa que imprima en pantalla todos los números enteros desde 0 hasta 100 (incluyendo ambos extremos), en orden creciente, mostrando un número por línea.
def mostrar(n):
    for i in range(n+1):
        print(i)
    print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str)

# 2.Desarrolla un programa que solicite al usuario un número entero y determine la cantidad de dígitos que contiene.
def cont_dig():
    num = parse_input(int, 'Por favor ingrese un número entero: ', '')
    if(exit_test(num)):return
    num = abs(num)
    cont = 0
    if(num == 0): 
        cont = 1
    while num > 0:
        cont+= 1
        num = num // 10
    
    print(chr(27)+"[1;32m"+f'\n El número ingresado tiene {cont} dígito/s.')
    print(chr(27)+"[0m"+'')
    print(chr(27)+"[0;34m"+'Ingrese cualquier cosa para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str) 

# 3. Escribe un programa que sume todos los números enteros comprendidos entre dos valores dados por el usuario, excluyendo esos dos valores.
def suma():
    num1 = parse_input(int, 'Por favor ingrese un número entero: ',chr(27)+"[0;31m"+'Input invalido')
    if(exit_test(num1)): return
    num2 = parse_input(int, 'Por favor ingrese un número entero: ',chr(27)+"[0;31m"+'Input invalido')
    if(exit_test(num2)): return
    nums = [num1, num2]
    nums.sort()
    print(nums)
    acc = 0
    if(nums[1]-nums[0] == 1):
        acc = 0
    else:
        for i in range(nums[0]+1,nums[1]):
            acc += i
    
    print(chr(27)+"[1;32m"+f'La suma de los valores entre [{nums[0]},{nums[1]}] es: {acc}')
    print(chr(27)+"[0m"+'') 
    print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str)

# 4. Elabora un programa que permita al usuario ingresar números enteros y los sume en secuencia. El programa debe detenerse y mostrar el total acumulado cuando el usuario ingrese un 0. 

def sum_sec():
    print('Por favor ingrese números enteros. Ingrese 0 para ver el resultado o E para salir')
    num = 'initial'
    acc = 0
    while True :
        num = parse_input(int)
        if(exit_test(num)): return
        if(num == 0):
            print(chr(27)+"[1;32m"+f'Suma de los números ingresados: {acc}')
            print(chr(27)+"[0m")
            print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
            print(chr(27)+"[0m")
            parse_input(str)
            return
        else:
            acc += num
    

# 5.Crea un juego en el que el usuario deba adivinar un número aleatorio entre 0 y 9. Al final, el programa debe mostrar cuántos intentos fueron necesarios para acertar el número. 

def game():
    num = 'Initial value'
    while not exit_test(num):
        print('Por favor ingrese números hasta adivinar el número entre 1 y 9 o E para salir')
        target = random.randrange(9)
        cont = 0
        while num != target:
            num = parse_input(int)
            if(exit_test(num)): 
                print('¡Hasta la Próxima!')
                time.sleep(1)
                return
            cont += 1
        
        print(chr(27)+"[1;32m"+f'Bien hecho! Ha adivinado en {cont} intentos')
        print(chr(27)+"[0m")
        

# 6. Desarrolla un programa que imprima en pantalla todos los números pares comprendidos entre 0 y 100, en orden decreciente.

def even():
    for i in range(100, -1, -2):
        if(i>0):
            print(i, end=', ')
        else:
            print(f'{i}.')
    print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str)

def even_1():
    print(chr(27)+"[0;32m", end='')
    print(*range(100, -1, -2), sep=', ', end='.')
    print(chr(27)+"[0m")
    print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str)

# 7. Crea un programa que calcule la suma de todos los números comprendidos entre 0 y un número entero positivo indicado por el usuario.

def sum_pos():
    num = parse_input(int, 'Por favor ingrese un número entero positivo: ',chr(27)+"[0;31m"+'El número debe ser entero y positivo', lambda x: x>0)
    if(exit_test(num)): return
    acc = 0
    for i in range(num+1):
        acc += i
    print(chr(27)+"[0;32m", end='')
    print(f'La suma de todos los números desde 0 hasta el número ingresado es: {acc}', end='')
    print(chr(27)+"[0m")
    print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str)

# 8. Escribe un programa que permita al usuario ingresar 100 números enteros. Luego, el programa debe indicar cuántos de estos números son pares, cuántos son impares, cuántos son negativos y cuántos son positivos. (Nota: para probar el programa puedes usar una cantidad menor, pero debe estar preparado para procesar 100 números con un solo cambio).

def cien(n):
    nums = []
    cont = 0
    even= 0
    odd= 0
    pos = 0
    neg = 0
    zero = 0

    for i in range(n):
        sys('cls')
        print(f'Por favor ingrese {n} número/s entero/s \n Números ingresados: {cont} \n {nums} ')
        num = parse_input(int, '',chr(27)+"[;31m"+'Entrada inválida')
        if(exit_test(num)): return
        nums.append(num)
        cont += 1
        if(num == 0):
            zero +=1
        else:
            if(num > 0): 
                pos += 1
            else:
                neg += 1
            if(num % 2 == 0):
                even += 1
            else: 
                odd += 1
            
    sys('cls')
    print(f'Números ingresados: \n {nums} \n')
    print(chr(27)+"[0;32m"+f'Positivos: {pos} \nNegativos: {neg} \nPares: {even} \nImpares: {odd} \nCeros: {zero}')
    print(chr(27)+"[0m")
    print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str)

# 9. Elabora un programa que permita al usuario ingresar 100 números enteros y luego calcule la media de esos valores. (Nota: puedes probar el programa con una cantidad menor, pero debe poder procesar 100 números cambiando solo un valor)

def mean(n):
    nums = []
    cont = 0
    for i in range(n):
        sys('cls')
        print(f'Por favor ingrese {n} número/s entero/s \n Números ingresados: {cont} \n {nums} ')
        num = parse_input(int, '',chr(27)+"[;31m"+'Entrada inválida')
        if(exit_test(num)): return
        nums.append(num)
        cont += 1
    sys('cls')
    print(f'Números ingresados: \n {nums} \n')
    print(chr(27)+"[0;32m"+f'Media: {np.mean(nums)}')
    print(chr(27)+"[0m")
    print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str)

# 10. Escribe un programa que invierta el orden de los dígitos de un número ingresado por el usuario. Ejemplo: si el usuario ingresa 547, el programa debe mostrar 745.

def inverter():
    print('Por favor ingrese un número entero')
    num = parse_input(int)
    if(exit_test(num)): return
    num = str(num)
    num1 = ''
    for i in range(len(num) - 1, -1, -1):
        num1 = num1 + num[i]
    sys('cls')
    print(f'Número Ingresado: {num}')
    print(chr(27)+"[0;32m"+f'Inversión: {num1}')
    print(chr(27)+"[0m")
    print(chr(27)+"[0;34m"+'Pulse cualquier tecla para salir', end='')
    print(chr(27)+"[0m")
    parse_input(str)

# Loop principal

def main_loop():
    while True:
        sys('cls')
        print('Indique con un número entre 1 o 10 que ejercicio quiere probar. Ingrese E en cualquier momento para salir')
        print(chr(27)+"[0;34m"+'A fin de que sea más sencillo probarlos, los ejercicios que piden 100 números solo solicitarán 20. solo cambiando el argumento de 20 a 100 pediran 100.', end='')
        print(chr(27)+"[0m")
        print('1. Números del 1 al 100 \n2. Cantidad de dígitos \n3. Suma de los valores entre dos valores ingresados \n4. Suma de números ingresados \n5. Adivinanza \n6. Imprimir todos los números del 100 a 0 descendiente \n7. Suma de números entre 0 y un número introducido \n8. Clasificación de números ingresados \n9. Media de valores \n10. Inversión de dígitos')
        opts = list(range(1,11))
        opt = parse_input(int,'',chr(27)+"[0;31m"+'Ingrese una opción válida', lambda x: x in opts)
        if(exit_test(opt)): return
        match opt:
            case 1: 
                mostrar(100)
                
            case 2: 
                cont_dig()
                
            case 3: 
                suma()
                
            case 4: 
                sum_sec()
                
            case 5: 
                game()
                
            case 6: 
                even()
                
            case 7: 
                sum_pos()
                
            case 8: 
                cien(20)
                
            case 9: 
                mean(20)
                
            case 10: 
                inverter()
                


main_loop()