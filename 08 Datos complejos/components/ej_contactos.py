agenda = {}
for i in range(5):
    contact = input('Ingrese el nombre')
    cel = input('ingrese el número')
    agenda[contact] = cel

search = input('Por favor ingrese el nombre del contacto que quiere buscar')

print([(c,p) for c, p in agenda.items() if search.lower() in c.lower()])