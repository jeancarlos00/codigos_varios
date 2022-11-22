import re


def verificar_email(email):
    patron = r'@\w+\.com'
    verificar = re.search(patron, email)
    if verificar:
        print("Ok")
    else:
        print("La dirección de email es incorrecta")


verificar_email('jeancarlosmercedescuevas@gmail.com')

##################################################################################################################################################

import re

def verificar_saludo(frase):
    dicho =r'^Hola'
    verificar = re.search(dicho,frase)
    if verificar:
        print("Ok")
    else:
        print("No has saludado")

verificar_saludo('Hola')

####################################################################################################################################################

import re


def verificar_cp(cp):
    codigo = r'\w\w\d\d\d\d'
    verificar = re.search(codigo, cp)

    if verificar:
        print("Ok")

    else:
        print("El código postal ingresado no es correcto")