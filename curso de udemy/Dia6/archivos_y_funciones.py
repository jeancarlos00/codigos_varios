def abrir_leer(archivo):
    mi_archivo = open(archivo)
    yanco = mi_archivo.read()
    return yanco

#otro ejemplo
def sobrescribir(yanco):
   mi_archivo = open(yanco,'w')
   mi_archivo.write("contenido eliminado")