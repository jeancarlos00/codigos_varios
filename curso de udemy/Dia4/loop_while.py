moneda = 5

while moneda > 0:
    print(f"tengo {moneda} monedas")
    moneda = moneda -1


# otro ejemplo

manzana = 's'

while manzana =='s':
   manzana = input('quieres seguir (s/n)')
else:
    print("gracias")

#otro ejemplo
nombre = input('ingrese su nombre')
for letra in nombre:
      print(letra)


#en los loop se pueden usar (continue,pass y break)


numero = 10
while numero > -1:
    print(numero)
    numero = numero - 1


#otro ejemplo
numero = 50
while numero > -1:
  print(numero)
  numero = numero -5

#otro ejemplo
lista_numeros = [4,5,8,7,6,9,8,2,4,5,7,1,9,5,6,-1,-5,6,-6,-4,-3]
for a in lista_numeros:
    if a > 0:
        print(a)
    else:
        break