#los principales operadores logicos son:
#(not)
#(and)
#(or)


texto = "Cuando algo es lo suficientemente importante, lo haces incluso si las probabilidades de que salga bien no te acompañan"
palabra1 = 'éxito'
palabra2 = 'tecnología'
mi_bool3 =  (palabra1 not in texto) and (palabra2 not in  texto)
print(mi_bool3)

#otro ejemplo
num11=36
num22=72/2
num33=48
mi_bool1=(num11>num22) or (num11<num33)
print(mi_bool1)

#otro ejemplo
num1=36
num2=72/2
num3=48
mi_bool=num1>num2<num3

print(mi_bool)