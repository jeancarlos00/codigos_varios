# comprimir archivos

'''import zipfile

mi_zip = zipfile.ZipFile('archivos_comprimidos.zip', 'w')

mi_zip.write('historia_python.txt')
mi_zip.write('historia_python1.txt')

mi_zip.close()'''

#############################################################################################################################
# descomprimir archivos

'''import zipfile

mi_zip_abierto = zipfile.ZipFile('archivos_comprimidos.zip', 'r')

mi_zip_abierto.extractall()'''

#############################################################################################################################
# comprimir usando shutil

'''
import shutil

carpeta_origen = 'C:\\Users\\Jean Carlos\\Desktop\\carpeta_superior_practica_python'

carpeta_destino = 'todo_comprimido'

shutil.make_archive(carpeta_destino, 'zip', carpeta_origen)'''

#############################################################################################################################
# descomprimir con shutil

'''
import shutil

shutil.unpack_archive('todo_comprimido.zip', 'extraccion_terminada')'''
