students = [input('Ingrese el nombre') for i in range(3)]
students_califications = {} 
for s in students:
    n1 = int(input('Ingrese la primer nota'))
    n2 = int(input('Ingrese la segunda nota'))
    n3 = int(input('Ingrese la tercera nota'))
    students_califications[s] = (n1,n2,n3)

for k,v in students_califications.items():
    print(f'{k}: {round((v[0] + v[1] + v[2])/3,2)}')