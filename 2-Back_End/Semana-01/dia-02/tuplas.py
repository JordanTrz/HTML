primos = (2,3,5,7,11,13)
pares = [2,4,6,8,10]
dias = ("lunes", "martes", "miercoles", "jueves", "viernes", "sabado","domingo")

# Se utiliza una tupla cuando los valores son finitos, ejemplo los días de la semana
primos2 = list(primos)
print(primos)
print(primos2)
primos2.append(17)
print(primos)
primos = tuple(primos2)
print(primos)
primosordenados = sorted(primos,reverse=True)
print(primosordenados)
print(max(primos))
print(max(pares))
print(sum(pares))
print(sum(pares)/len(pares))