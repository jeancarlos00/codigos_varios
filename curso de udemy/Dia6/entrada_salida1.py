mi_archivo = open('prueba.txt')
yanco = mi_archivo.readlines()
print(yanco[2])



# con readLine(), se abre una sola linea
# con rstrip(), se quita el salto de linea
# con upper(), se pone en mayusculas
# con readLines(), se convierte en una lista 
# otro ejemplo iterando con un loop

'''for a in mi_archivo:
    print('aqui dice:' + a)'''

mi_archivo.close()