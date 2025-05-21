from utils.colors_fx import green
from math import pi

def informacion_personal(nombre, apellido, edad, residencia):
    green(f'Soy {nombre.capitalize()} {apellido.capitalize()}, tengo {edad} años y vivo en {residencia.capitalize()}')

def calcular_area_circulo(radio):
    area = pi*radio**2
    return area

def calcular_perimetro_circulo(radio):
    perim = 2*pi*radio
    return perim

def segundos_a_horas(segs):
    return segs // 3600

def tabla_multiplicar(n):
    for i in range(1,11):
       print(f'{n} x {i} = {n*i}') 

def operaciones_basicas(n1,n2):
    suma = n1 + n2
    resta = n1 - n2
    mult = n1*n2
    div = round(n1/n2,2) if n2 != 0 else 'No se puede dividir por cero'
    return (suma, resta, mult, div)    
    
def calcular_imc(peso, altura):
    return peso/(altura/100)**2

def celsius_a_fahrenheit(c):
    return round(c*9/5+32,2)