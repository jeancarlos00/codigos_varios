from random import choice

palabras = ['frito', 'chuleta', 'jamoneta', 'pastelon']
letra_correcta = []
letra_incorrecta = []
intentos = 6
aciertos = 0
juego_terminado = False


# -------------------------------------------------


def elegir_palabra(palabras):
    palabra_elegida = choice(palabras)
    letras_unicas = len(set(palabra_elegida))
    return palabra_elegida, letras_unicas


# ----------------------------------------------------


def pedir_letra():

    letra_elegida = ''
    es_valida = False
    abecedario = 'abcdefghijklmnñopqrstuvwxyz'
    while not es_valida:
        letra_elegida = input('Elige una letra:\n').lower()
        if letra_elegida in abecedario and len(letra_elegida) == 1:
            es_valida = True
        else:
            print('No has elegido una letra correcta')

    return letra_elegida
# ----------------------------------------------------------


def mostrar_nuevo_tablero(palabra_elegida):
    lista_oculta = []

    for l in palabra_elegida:
        if l in letra_correcta:
            lista_oculta.append(l)
        else:
            lista_oculta.append('-')
    print(' '.join(lista_oculta))


# ------------------------------------------------------------

def chequear_letra(letra_elegida, palabra_oculta, vidas, coincidencias):
    fin = False

    if letra_elegida in palabra_oculta and letra_elegida not in letra_correcta:
        letra_correcta.append(letra_elegida)
        coincidencias +=1
    elif letra_elegida in palabra_oculta and letra_elegida in letra_correcta:
        print('Ya has encontrado esa letra, intenta con otra diferente')
    else:
        letra_incorrecta.append(letra_elegida)
        vidas -= 1

    if vidas == 0:
        fin = perder()
    elif coincidencias == letras_unicas:
        fin = ganar(palabra_oculta)
    return vidas, fin, coincidencias

# -------------------------------------------------------------------------


def perder():
    print('Te has quedado sin vidas')
    print('la palabra oculta era: ' + palabra)

    return True

# --------------------------------------------------------------------------


def ganar(palabra_descubierta):
    mostrar_nuevo_tablero(palabra_descubierta)
    print('Felicitaciones has encontrado la palabra')
    return True


# ----------------------------------------------------------------------------

palabra, letras_unicas = elegir_palabra(palabras)
while not juego_terminado:
    print('\n' + '*' * 20 + '\n')
    mostrar_nuevo_tablero(palabra)
    print('\n')
    print('letras incorrectas: ' + '-'.join(letra_incorrecta))
    print(f'vidas: {intentos}')
    print('\n' + '*' * 20 + '\n')
    letra = pedir_letra()
    intentos,terminado, aciertos = chequear_letra(letra,palabra,intentos,aciertos)
    juego_terminado = terminado
