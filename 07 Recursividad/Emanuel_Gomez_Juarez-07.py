from utils.fx import clear, parse_input, finish_indication, exit_test
from utils.colors_fx import blue, green, red
from utils.exercises_fx import fact, fib, pot, dec_bin, pal, sum_dig, sm_bl, sum_val

def factorial():
    clear()
    print('Por favor ingrese un número entero positivo:')
    n = parse_input(int, '','Debe ingresar un número válido', lambda x: x >= 1)
    if(exit_test(n)): return
    for i in range(1, n+1):
        fnum = fact(i)
        blue(f'{i}!: ', '')
        green(fnum)
    finish_indication()

def fibonacci():
    clear()
    print('Por favor ingrese un número Entero mayot o igual a 0. Ingrese E para salir')
    pos= parse_input(int, '','Debe ingresar un número válido', lambda x: x >= 0)
    if(exit_test(pos)): return
    clear()
    serie= []
    for i in range(pos+1):
        serie.append(fib(i))
    blue(f'Primeras {pos} posiciones partiendo de la posición 0 son:')
    green(serie)
    finish_indication()

def potencia():
    clear()
    base= parse_input(float, 'Por favor ingrese la base: ', 'Debe ingresar un número válido')
    if(exit_test(base)): return
    exp= parse_input(int, 'Por favor ingrese el exponente entero: ', 'Debe ingresar un número válido')
    if(exit_test(exp)): return
    result = pot(base, exp)
    clear()
    green(f'{base} elevado a {exp} = {result}')
    finish_indication()

def decimal_binario():
    clear()
    num = parse_input(int, 'Por favor ingrese un número entero positivo para convertir a binario. Ingrese E para salir\n', 'Debe ingresar un número válido', lambda x: x > 0)
    if(exit_test(num)): return
    result = dec_bin(num)
    clear()
    green(f'{num} en base diez es igual a {result} en base 2')
    finish_indication()

def palindromo():
    clear()
    print('Por favor ingrese la palabra o frase a analizar. Tildes ocasionarán error, omitalas por favor')
    string = input()
    clear()
    response = 'Es un palíndromo' if pal(string.lower()) else 'No es un palíndromo'
    green(response)
    finish_indication()

def suma_digitos():
    clear()
    num = parse_input(int,'Por favor ingrese un número entero: ', 'Debe ingresar un número válido')
    if exit_test(num): return
    blue(f'La suma de los dígitos del número ingresado (','')
    green(f'{num}','')
    blue(f') es: ', '')
    green(f'{sum_dig(abs(num))}')
    finish_indication()

def suma_bloques():
    clear()
    base = parse_input(int,'Por favor ingrese la cantidad de bloques en la base: ', 'Debe ingresar una cantidad válida', lambda x: x >= 0 )
    if exit_test(base): return
    clear()
    blue('Para una pirámide de base ','')
    green(f'{base}', '')
    blue(', se requiern: ')
    green(f'{sm_bl(base)} bloques')
    finish_indication()

def contar_digito():
    clear()
    num = parse_input(int, 'Por favor ingrese un número entero. Ingrese E para salir:\n', 'Debe ingresar un número válido', lambda x: x >= 0)
    if exit_test(num): return
    val = parse_input(int, 'Por favor ingrese un dígito a buscar:\n', '', lambda x: x >= 0)
    if exit_test(val): return
    blue(f'La cantidad de veces que aparece el dígito {val} es: ','')
    green(f'{sum_val(num, val)}')
    finish_indication()
contar_digito()