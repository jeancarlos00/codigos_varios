#primer ejemplo
yanco = open('mi_archivo.txt','w')
yanco.write('Nuevo texto')
yanco.close()
yanco =open('mi_archivo.txt')
a = yanco.read()
print(a)

#segundo ejemplo
yanco = open('mi_archivo.txt','a')
yanco.write('Nuevo inicio de sesión')
yanco.close()
yanco = open('mi_archivo.txt','r')
a = yanco.read()
print(a)

#otro ejemplo
yanco = open('registro.txt','a')

registro_ultima_sesion = ["Federico", "20/12/2021", "08:17:32 hs", "Sin errores de carga"]

for m in registro_ultima_sesion:
    yanco.writelines(m + '\t')

yanco.close()

yanco = open('registro.txt', 'r')
a = yanco.read()
print(a)
yanco.close()