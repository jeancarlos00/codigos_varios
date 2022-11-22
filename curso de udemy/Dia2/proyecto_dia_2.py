#este proyecto calcula el 13% de las ventas de los vendedores

print('Saludos!')

nombre = input('ingrese su nombre: \n')
ventas = input('ingrese el monto de las ventas: \n')
ventas = int(ventas)
resultado = (ventas * 13 /100)
resultado = (round(resultado))

print (f'{nombre} su ganancia correspondiente a este mes es:  {resultado} pesos')