from utils.colors_fx import blue, green, red
from utils.fx import parse_input, exit_test, clear, finish_indication
import utils.exercises_fx as ef

# 1. Crear una función llamada imprimir_hola_mundo que imprima por pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.

def ej_1():
    clear()
    green('\nHola Mundo')
    finish_indication()

# 2. Crear una función llamada saludar_usuario(nombre) que reciba como parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta función desde el programa principal solicitando el nombre al usuario. 

def ej_2():
    clear()
    name = parse_input(str,'Por favor ingrese su nombre: \n', 'Por favor ingrese un nombre válido', lambda x: len(x) > 1)
    clear()
    green(f'\nHola {name.capitalize()}!')
    finish_indication()

# 3. Crear una función llamada informacion_personal(nombre, apellido, edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar a esta función con los valores ingresados.

def ej_3():
    clear()
    name = parse_input(str,'Por favor ingrese su nombre: \n', 'Por favor ingrese un nombre válido', lambda x: len(x) > 1)
    if exit_test(name): return
    surname = parse_input(str,'Por favor ingrese su apellido: \n', 'Por favor ingrese un apellido válido', lambda x: len(x) > 1)
    if exit_test(surname): return
    age = parse_input(int,'Por favor ingrese su edad: \n', 'Por favor ingrese una edad válida', lambda x: x >= 0)
    if exit_test(age): return
    res = parse_input(str, 'Por favor ingrese su lugar de residencia: \n', lambda x: len(x) > 1)
    if exit_test(res): return
    clear()
    ef.informacion_personal(name, surname, age, res)
    finish_indication()

# 4. Crear dos funciones: calcular_area_circulo(radio) que reciba el radio como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar el radio al usuario y llamar ambas funciones para mostrar los resultados.

def ej_4():
    clear()
    rad = parse_input(float, 'Por favor ingrese el radio: ', 'Entrada no válida')
    if exit_test(rad): return
    area = ef.calcular_area_circulo(rad)
    perim = ef.calcular_perimetro_circulo(rad)
    clear()
    print('Area: ', end='')
    green(f'{area:.2f}')
    print('Perímetro: ', end='')
    green(f'{perim:.2f}')
    finish_indication()


# 5. Crear una función llamada segundos_a_horas(segundos) que reciba una cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. Solicitar al usuario los segundos y mostrar el resultado usando esta función.

def ej_5():
    clear()
    seg = parse_input(int, 'Por favor ingrese la cantidad de segundos a convertir: ', 'Entrada inválida, debe ser un valor entero y positivo', lambda x: x >= 0)
    if exit_test(seg): return
    hs = ef.segundos_a_horas(seg)
    clear()
    green(f'{seg} segundos', '')
    print(f' equivalen a: ',end = '')
    green(f'{hs} hs')
    finish_indication()

# 6. Crear una función llamada tabla_multiplicar(numero) que reciba un número como parámetro y imprima la tabla de multiplicar de ese número del 1 al 10. Pedir al usuario el número y llamar a la función.

def ej_6():
    clear()
    num = parse_input(int,'Por favor ingrese el número: ', 'Debe ingresar un número entero y positivo', lambda x: x>0 )
    if exit_test(num): return
    clear()
    ef.tabla_multiplicar(num)
    finish_indication()

# 7. Crear una función llamada operaciones_basicas(a, b) que reciba dos números como parámetros y devuelva una tupla con el resultado de sumarlos, restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.

def ej_7():
    clear()
    num1 = parse_input(int, 'Por favot ingrese el primer número: ')
    if exit_test(num1): return
    num2 = parse_input(int, 'Por favot ingrese el segundo número: ')
    if exit_test(num2): return
    tup = ef.operaciones_basicas(num1,num2)
    clear()
    green(f'Suma: {tup[0]}\nResta: {tup[1]}\nMultiplicación: {tup[2]}\nDivisión: {tup[3]}')
    finish_indication()

# 8. Crear una función llamada calcular_imc(peso, altura) que reciba el peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.

def ej_8():
    clear()
    peso = parse_input(int,'Por favor ingrese su peso en kg:\n', 'Debe ingresar un numero positivo', lambda x: x>0)
    if exit_test(peso): return
    altura = parse_input(int, 'Por favor ingrese su altura en cm:\n', 'Debe ingresar un numero positivo', lambda x: x>0)
    if exit_test(altura): return
    imc = round(ef.calcular_imc(peso,altura),2)
    clear()
    green(f'IMC: {imc}')
    finish_indication()

# 9. Crear una función llamada celsius_a_fahrenheit(celsius) que reciba una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.

def ej_9():
    clear()
    celsius= parse_input(float, 'Por favor ingrese la temperatura en C°: ', 'Debe ingresar un número')
    if exit_test(celsius): return
    f = ef.celsius_a_fahrenheit(celsius)
    clear()
    green(f'{celsius}°Centígrados => {f}° Farenheit')
    finish_indication()

# 10. Crear una función llamada calcular_promedio(a, b, c) que reciba tres números como parámetros y devuelva el promedio de ellos. Solicitar los números al usuario y mostrar el resultado usando esta función.

def ej_10(n = 3):
    nums = []
    for i in range(n):
        clear()
        blue(f'Números ingresados: {', '.join(str(n) for n in nums)}')
        num = parse_input(float, f'Por favor ingrese el {i+1} número:\n', 'Debe ingresar un número - ingrese E para salir -')
        if exit_test(num): return
        nums.append(num)
    clear()
    blue(f'Números ingresados: {', '.join(map(str, nums))}')
    green(f'Promedio: {sum(nums)/n}')
    finish_indication()

def main_loop():
    while True:
        clear()
        print('Indique con un número entre 1 o 10 que ejercicio quiere probar. Ingrese E en cualquier momento para salir')
        print('1. Hola Mundo \n2. Saludar \n3. Información Personal \n4. Área y Perímetro del Círculo \n5. Segundos a Horas \n6. Tablas de Multiplicar \n7. Operaciones Básicas \n8. Calcular IMC \n9. Celsius a Farenheit \n10. Calcular Promedio')
        opts = list(range(1,11))
        opt = parse_input(int,'','Ingrese una opción válida', lambda x: x in opts)
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

