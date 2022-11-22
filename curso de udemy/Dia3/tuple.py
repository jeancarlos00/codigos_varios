#los tuple son inmutables como los string no se modifican
mi_taple = (1,2,3,)

print(mi_taple[2])

#se puede indexar los taples
print(mi_taple.index(1))


#a traves de un casting podemos convertir un taple en una lista ejemplo:

yanco = (list(mi_taple))

print(type(yanco))

#tambien los taples pueden contener taple ejemplo
yensel = (1,2,3,4,5,(0,800,4000))

print(yensel)

#asignarle valores a la variable

angel  = (1,2,3)

(x,y,z) = angel

print(x,y,z)



