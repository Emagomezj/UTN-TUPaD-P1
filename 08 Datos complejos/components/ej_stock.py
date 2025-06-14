prod = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

def consulta(p):
    try:
        return(f'{p}: {prod[p]} en stock')
    except:
        return'No se ha encontrado el producto'

def agregar(p,cant = 0):
    if p in prod.keys():
        prod[p] = prod[p] + cant
    else:
        prod[p] = cant
    return prod

print(consulta('Banana'))
print(agregar('Ananá', 5000))
print(agregar('Pizza', 40))