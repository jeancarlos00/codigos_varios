lista_numeros = [1, 5, 8, 7, 6, 8, 2, 5, 2, 6, 4, 8, 5, 9, 8, 3, 5, 4, 2, 5, 6, 4]

suma_pares = 0
for i in lista_numeros:
    if i % 2 == 0:
     suma_pares = suma_pares + i
     print (suma_pares)


suma_impares = 0
for ii in lista_numeros:
    if ii % 2 == 1:
     suma_impares = suma_impares + ii
    print(suma_impares)

