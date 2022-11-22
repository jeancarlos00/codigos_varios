from collections import Counter

numeros = [8,6,6,6,6,8,6,9,3,2,1,1,0,4,7,]
print(Counter(numeros))


#############################################################
#otro ejemplo

print(Counter('misisipi'))

#######################################################################
#otro ejemplo

frase = 'al pan pan y al vino vino'
print(Counter(frase.split()))
#########################################################################
#otro ejemplo
serie = Counter([1,1,1,1,1,1,1,1,1,1,1,1,9,9,9,9,9,6,5,6,5,8,7])
print(serie.most_common(1))
####################################################################################
#otro ejemplo


print(list(serie))

##############################################################################################################################
from collections import defaultdict

mi_dic = defaultdict(lambda: 'nada')
mi_dic ['uno']= 'verde'
print(mi_dic['dos'])

#####################################################################################################


from collections import defaultdict

mi_diccionario = defaultdict(lambda : "Valor no hallado")

mi_diccionario ['edad'] = 44