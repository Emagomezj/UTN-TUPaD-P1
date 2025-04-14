import random
from statistics import mode, median, mean 
# Instalar pwinput si no lo tienen instalado
import pwinput

# Variables globales constantes para los ejercicios
int_req = 'Por favor ingrese un número entero: '
float_req = 'Por favor ingrese un número: '
int_err = 'Por favor ingrese un dato válido. Debe ingresar un número entero'
float_err = 'Por favor ingrese un dato válido. Debe ingresar un número'
# Funciones útiles para los ejercicios
def exit_test(var):
    return str(var).lower() == 'e'
def parse_input(pars, frase, err, condition = lambda x: True):
    while True:
        try:
            var = input(frase)
            if(var == 'e' or var == 'E'):
                return var
            pars_var = pars(var)
            if(condition(pars_var)):
                return pars_var
            else:
                raise ValueError(err)
        except:
            print(err)

def edad_input(pars, frase, err):
    while True:
        try:
            var = input(frase)
            if(var == 'e' or var == 'E'):
                return var
            pars_var = pars(var)
            if(pars_var < 0):
                raise ValueError(err)
            return pars_var
        except:
            print(err)
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
            print('La opción ingresada no coincide con un comando válido. \n Ingrese un número del 1 al 10 para ejecutar los ejercicios o E para salir')

# Ejercicio 1. Escribir un programa que solicite la edad del usuario. Si el usuario es mayor de 18 años, deberá mostrar un mensaje en pantalla que diga “Es mayor de edad”. 
def es_mayor():
    edad = edad_input(int,'Por favor ingrese su edad: ', int_err)
    if(exit_test(edad)): return
    if(edad >= 18):
        print("Es mayor de edad")
    else:
        return

# Ejercicio 2. Escribir un programa que solicite su nota al usuario. Si la nota es mayor o igual a 6, deberá mostrar por pantalla un mensaje que diga “Aprobado”; en caso contrario deberá mostrar el mensaje “Desaprobado”. 

def calificacion():
    nota = parse_input(float, 'Por favor ingrese su nota: ', float_err)
    if(exit_test(nota)): return
    if(nota >= 6):
        print('Aprobado')
    else:
        print('Desaprobado')

# Ejercicio 3. Escribir un programa que permita ingresar solo números pares. Si el usuario ingresa un número par, imprimir por en pantalla el mensaje "Ha ingresado un número par"; en caso contrario, imprimir por pantalla "Por favor, ingrese un número par". Nota: investigar el uso del operador de módulo (%) en Python para evaluar si un número es par o impar. 

def par():
    while True:
        num = parse_input(int, int_req, int_err)
        if(exit_test(num)): return
        if(num % 2 == 0):
            print('Ha ingresado un número par')
            break
# Ejercicio 4. Escribir un programa que solicite al usuario su edad e imprima por pantalla a cuál de las siguientes categorías pertenece: ● Niño/a: menor de 12 años. ● Adolescente: ayor o igual que 12 años y menor que 18 años. ● Adulto/a joven: mayor o igual que 18 años y menor que 30 años. ● Adulto/a: mayor o igual que 30 años.

def etapa():
    edad = edad_input(int, 'Por favor ingrese su edad: ', int_err)
    if(exit_test(edad)): return
    if(edad < 12):
        print('Niño/a')
    elif(edad < 18):
        print('Adolescente')
    elif(edad < 30):
        print('Adulto/a joven')
    else:
        print('Adulto/a')
    
# Ejercicio 5. Escribir un programa que permita introducir contraseñas de entre 8 y 14 caracteres (incluyendo 8 y 14). Si el usuario ingresa una contraseña de longitud adecuada, imprimir por en pantalla el mensaje "Ha ingresado una contraseña correcta"; en caso contrario, imprimir por pantalla "Por favor, ingrese una contraseña de entre 8 y 14 caracteres". Nota: investigue el uso de la función len() en Python para evaluar la cantidad de elementos que tiene un iterable tal como una lista o un string. 

def password():
    while True:
        password = pwinput.pwinput(prompt='Por favor, ingrese una contraseña de entre 8 y 14 caracteres: \n')
        if(exit_test(password)): return
        if(len(password) <= 14 and len(password) >= 8):
            print('Ha ingresado una contraseña correcta')
            break

# Ejercicio 6. Escribir un programa que tome la lista numeros_aleatorios, calcule su moda, su mediana y su media y las compare para determinar si hay sesgo positivo, negativo o no hay sesgo. Imprimir el resultado por pantalla.

def statics():
    numeros_aleatorios = [random.randint(1,100) for i in range(50)]
    moda = mode(numeros_aleatorios)
    mediana = median(numeros_aleatorios)
    media = mean(numeros_aleatorios)

    if(media > mediana and mediana > moda):
        print('Sesgo positivo o a la derecha')
    elif(media < mediana and mediana < moda):
        print('Sesgo negativo o a la izquierda')
    elif(media == mediana and mediana == moda):
        print('Sin sesgo')
    else:
        print('No corresponde con un caso expuesto en la documentación para realizar el trabajo')

# Ejercicio 7. Escribir un programa que solicite una frase o palabra al usuario. Si el string ingresado termina con vocal, añadir un signo de exclamación al final e imprimir el string resultante por pantalla; en caso contrario, dejar el string tal cual lo ingresó el usuario e imprimirlo por pantalla.

def string_exercise():
    string = input('Por favor ingrese una frase o palabra: \n')
    vocales = ('a','e','i','o','u')
    if(string.lower().endswith(vocales)):
        print(string + '!')
    else:
        print(string)

def string_exercise1():
    string = input('Por favor ingrese una frase o palabra: \n')
    vocales = ['a','e','i','o','u']
    if string[-1].lower() in vocales:
        print(string + '!')
    else:
        print(string)

# Ejercicio 8. Escribir un programa que solicite al usuario que ingrese su nombre y el número 1, 2 o 3 dependiendo de la opción que desee: 
# 1. Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO. 
# 2. Si quiere su nombre en minúsculas. Por ejemplo: pedro. 
# 3. Si quiere su nombre con la primera letra mayúscula. Por ejemplo: Pedro. 
# El programa debe transformar el nombre ingresado de acuerdo a la opción seleccionada por el 
# usuario e imprimir el resultado por pantalla. Nota: investigue uso de las funciones upper(), 
# lower() y title() de Python para convertir entre mayúsculas y minúsculas.

def name():
    name = input('Por favor ingrese su nombre: ')
    if(exit_test(name)): return
    print('Ingrese: \n 1. A mayúsculas \n 2. A minúsculas \n 3. Primera letra mayúscula \n')
    opt = 0

    while not (opt in [1,2,3,'e', 'E']):
        opt = parse_input(int, '', 'Ingrese una opción válida')

    
    if(exit_test(opt)): return
    if(opt == 1):
        print(name.upper())
    elif(opt == 2):
        print(name.lower())
    else:
        print(name.title())

# Ejercicio 9. Escribir un programa que pida al usuario la magnitud de un terremoto, clasifique la magnitud en una de las siguientes categorías según la escala de Richter e imprima el resultado por pantalla.

def sismo():
    magnitud = parse_input(float, 'Por favor ingrese la magnitud del sismo: \n', float_err)
    if exit_test(magnitud): return
    if magnitud < 3:
        print('"Muy leve" (imperceptible)')
    elif magnitud < 4:
        print('"Leve" (Ligeramente perceptible)')
    elif magnitud < 5:
        print('"Moderado" (Sentido por personas pero generalmente no causa daños)')
    elif magnitud < 6:
        print('"Fuerte" (puede causar daños en estructuras débiles)')
    elif magnitud < 7:
        print('"Muy Fuerte" (puede causar daños significativos)')
    else:
        print('"Extremo" (puede causar graves daños a gran escalas)')

# Ejercicio 10.Escribir un programa que pregunte al usuario en cuál hemisferio se encuentra (N/S), qué mes del año es y qué día es. El programa deberá utilizar esa información para imprimir por pantalla si el usuario se encuentra en otoño, invierno, primavera o verano. 

def temporada():
    day = parse_input(int, 'Por favor ingrese el día con números: \n', int_err + ' mayor que cero y menor o igual que 31', lambda x: x <= 31 and x > 0 )
    if(exit_test(day)): return
    month = parse_input(int, 'Por favor ingrese el mes con números: \n', int_err + ' mayor que cero y menor o igual que 12', lambda x: x <= 12 and x > 0)
    if(exit_test(month)): return
    hem= parse_input(str, 'Por favor ingrese N si se encuentra en el hemisferio norte o S si se encuentra en el hemisferio sur: \n', 'Debe ingresar N, S para los hemisferios o E para salir', lambda x: x.lower() == 'n' or x.lower() == 's')
    if(exit_test(hem)): return
    seasons = {
        'n': {
            'Invierno': ((21,12),(20,3)),
            'Primavera': ((21,3),(20,6)),
            'Verano': ((21,6),(20,9)),
            'Otoño': ((21,9),(20,12))
        }, 
        's': {
            'Primavera': ((21,9),(20,12)),
            'Verano': ((21,12),(20,3)),
            'Otoño': ((21,3),(20,6)),
            'Invierno': ((21,6),(20,9))
        }
    }
    for season, ((d_i, m_i),(d_f,m_f)) in seasons[hem.lower()].items():
        if(month == m_i and day >= d_i) or (month == m_f and day <= d_f) or (month > m_i and month < m_f) or (m_i > m_f and (month == m_i or month < m_f)):
            print(season)
            return
    print('No se ha podido encontrar la estación')

def main_loop():
    while True:
        print('\n\n')
        print('¿Qué ejercicio desea ejecutar?')
        print('1. ¿Es mayor?')
        print('2. Aprobado-Desaprobado')
        print('3. Par')
        print('4. Etapa vital')
        print('5. Chequeo contraseña')
        print('6. Statics')
        print('7. Modificación de cadenas por condición')
        print('8. Modificación de cadenas por indicación')
        print('9. Clasifiación de sismos')
        print('10. Estación por hemisferio')
        print('Para salir presione E')

        opt = opt_input()
        if (opt == 'e' or opt == 'E'):
            return
        match opt:
            case 1: es_mayor()
            case 2: calificacion()
            case 3: par()
            case 4: etapa()
            case 5: password()
            case 6: statics()
            case 7: string_exercise()
            case 8: name()
            case 9: sismo()
            case 10: temporada()

main_loop()