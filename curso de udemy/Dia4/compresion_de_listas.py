#ejemplo de listas comprimidas
temperatura_fahrenheit = [32, 212, 275]
grados_celsius =[(grado_fahrenheit -32)*(5/9) for grado_fahrenheit in temperatura_fahrenheit]

#otro ejemplo
valores = [1, 2, 3, 4, 5, 6, 9.5]
valores_pares = [yanco for yanco in valores if yanco%2==0 ]

#otro ejemplo
valores = [1, 2, 3, 4, 5, 6, 9.5]

valores_cuadrado = [valor ** 2 for valor in valores]