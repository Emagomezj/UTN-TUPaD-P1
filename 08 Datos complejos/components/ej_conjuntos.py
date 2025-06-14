p1 = [1,2,3,4,5,6,7,9]
p2 = [3,5,7,8,9]

ambos = set(p1) & set(p2)
solo_uno = set(p1) ^ set(p2)
cualquiera = set(p1)|set(p2)

print(f'Ambos: {ambos}\nSolo uno: {solo_uno}\nAl menos uno de los dos: {cualquiera}')