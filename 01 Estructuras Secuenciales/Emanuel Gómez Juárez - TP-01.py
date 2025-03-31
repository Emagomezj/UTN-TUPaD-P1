# Importación de módulos
import math

# Funciones utilizadas en varios ejercicios
def e_input(ingreso):
    while True:
        try:
            e = input(f'Ingrese {ingreso} por favor: ')
            if(e == 'e' or e == 'E'):
                return e
            e = int(e)
            return e
        except:
            print('Debe ingresar una cantidad válida(enteros)')

def f_input(ingreso):
    while True:
        try:
            f = input(f'Ingrese {ingreso} por favor: ')
            if(f == 'e' or f == 'E'):
                return f
            f = float(f)
            return f
        except:
            print('Debe ingresar un dato válido(Número)')

def opt_input():
    while True:
        valid_opt = [1,2,3,4,5,6,7,8,9,10]
        try:
            opt = input()
            if(opt == 'e' or opt == 'E'):
                return opt

            opt = int(opt)
            if opt in valid_opt: 

                return opt
            else:
                print('La opción ingresada no coincide con un comando válido.')
                print('Ingrese un número del 1 al 10 para ejecutar los ejercicios o E para salir')
        except:
            print('La opción ingresada no coincide con un comando válido.')
            print('Ingrese un número del 1 al 10 para ejecutar los ejercicios o E para salir')

# 1. Crear un programa que imprima por pantalla el mensaje "Hola Mundo!"
def hola_mundo():
    print('\n')
    print("Hola Mundo!")

#2. Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado. Por ejemplo: si el usuario ingresa “Marcos”, el programa debe imprimir por pantalla “Hola Marcos!”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

def hola_user():
    nombre = input('Por favor ingrese su nombre: ')

    print('\n')
    print(f'Hola {nombre}')

#3. Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados. Por ejemplo: si el usuario ingresa “Marcos”, “Pérez”, “30” y “Argentina”, el programa debe imprimir “Soy Marcos Pérez, tengo 30 años y vivo en Argentina”. Consejo: esto será más sencillo si utilizas print(f…) para realizar la impresión por pantalla. 

def presentacion():
    nombre = input('Ingrese su monbre por favor: ')
    apellido = input('Ingrese su apellido por favor: ')
    edad = input('Ingrese su edad por favor: ')
    residencia = input('Ingrese su lugar de residencia: ')

    print('\n')
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}')

#4. Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro.

def circulo():
    print('A continuación ingrese el radio o ingrese E para salir')
    def r_input():
        while True:
            try:
                r = input('Por favor ingrese el radio: ')
                if(r == 'e' or r == 'E'):
                    return r
                r = float(r)
                return r
            except:
                print('Debe ingresar un número válido')
    radio = r_input()
    if(radio == 'e' or radio == 'E'):
        return
    print('\n')
    print('Área: ', round(math.pi * radio**2,2)) 
    print('Perímetro: ', round(2*math.pi*radio,2))

#5. Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale.

def seg_hs():
    print('A continuación ingrese los segundos o E para salir')
    seg = e_input('los segundos')
    if(seg == 'e' or seg == 'E'):
        return
    hs, min = divmod(seg, 3600)
    
    print('\n')
    print(f'{seg} segundo/s equivalen a {hs} horas y {min//60} minutos')

#6. Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número.

def tabla():
    num = e_input('el número')
    if(num == 'e' or num == 'E'):
        return
    print('\n')
    print(f'Tabla del {num}')
    for i in range(11):
        print(f'{num} x {i} = {num * i} ')

#7. Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 

def operaciones():
    print('A continuación ingrese los números o ingrese E para salir')
    def get_num(ord):
        while True:
            try:
                num= input(f'Ingrese el {ord} número por favor: ')
                if(num == 'e' or num == 'E'):
                    return num
                num = int(num)
                if(num == 0):
                    print('El número no puede ser cero')
                else:
                    return num
            except ValueError:
                print('Debe ingresar un número entero')

    num1 = get_num('primer')
    if(num1 == 'e' or num1 == 'E'):
        return
    num2 = get_num('segundo')
    if(num2 == 'e' or num2 == 'E'):
        return

    print('\n')
    print(f'Suma: {num1 + num2}')
    print(f'Resta: {num1 - num2}')
    print(f'Multiplicación: {num1 * num2}')
    print(f'División: {num1 / num2}')
  
#8. Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal.

def imc():
    print('A continuación ingrese los datos o E para salir')
    kg = f_input('el peso en kg')
    if(kg == 'e' or kg == 'E'):
        return
    altura = f_input('su altura en m')
    if(altura == 'e' or altura == 'E'):
        return

    print('\n')
    print(f'IMC: {round(kg/altura**2,2)}')

#9. Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit.

def c_f():
    g = f_input('la temperatura en C° (Celsius)')
    if(g == 'e' or g == 'E'):
        return
    print('\n')
    print(f'{g}°C son {9/5 * g + 32}°F')

#10. Crear un programa que pida al usuario  3 números e imprima por pantalla el promedio de dichos números.

def promedio():
    print('A continuación ingrese los números o ingrese E para salir')
    elem = []
    def get_num_p(ord):
        while True:
            print('Números cargados:')
            print(*elem or 'Ninguno')
            try:
                num= input(f'Ingrese el {ord} número por favor: ')
                if(num == 'e' or num == 'E'):
                    return num
                num = float(num)
                elem.append(num)
                return num
            except ValueError:
                print('Debe ingresar un número')
    num1 = get_num_p('primer')
    if(num1 == 'e' or num1 == 'E'):
        return
    num2 = get_num_p('segundo')
    if(num2 == 'e' or num2 == 'E'):
        return
    num3 = get_num_p('tercer')
    if(num3 == 'e' or num3 == 'E'):
        return
    print('\n')
    print('Promedio: ', round((num1+num2+num3)/3,2))

def main_loop():
    while True:
        print('\n\n')
        print('¿Qué ejercicio desea ejecutar?')
        print('1. Hola mundo')
        print('2. Hola nombre')
        print('3. Saludo')
        print('4. Área y perímetro de un círculo')
        print('5. Segundos a Horas')
        print('6. Tabla de multiplicar')
        print('7. Operaciones aritméticas')
        print('8. IMC')
        print('9. C° a F°')
        print('10. Promedio')
        print('Para salir presione E')

        opt = opt_input()
        if (opt == 'e' or opt == 'E'):
            return
        match opt:
            case 1: hola_mundo()
            case 2: hola_user()
            case 3: presentacion()
            case 4: circulo()
            case 5: seg_hs()
            case 6: tabla()
            case 7: operaciones()
            case 8: imc()
            case 9: c_f()
            case 10: promedio()

main_loop()
