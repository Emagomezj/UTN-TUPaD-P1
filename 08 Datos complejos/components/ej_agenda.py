agenda = {('lunes',10): 'Reunion', ('martes', 9): 'Plaza'}

def consulta(dia, hora):
    try:
        print(agenda[(dia, hora)])
    except:
        print('No se ha encontrado')
    
consulta('martes', 9)