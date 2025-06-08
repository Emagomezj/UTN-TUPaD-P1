def cuenta_regresiva(numero):
    if numero > 0:
        print(numero)
        cuenta_regresiva(numero - 1)
    else:
        print("¡Despegue!")

cuenta_regresiva(3)