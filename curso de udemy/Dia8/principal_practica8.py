import numeros_practica8


def preguntar():

    print('Bienvenido a la farmacia carmen')
    while True:
       print('[P] - Perfumeria\n[F] - Farmacia\n[C] - Cosmetica')
       try:
           mi_rubro = input('Elija su rubro: ').upper()
           ['P', 'F', 'C'].index(mi_rubro)
       except ValueError:
           print('Esa no es una opcion valida')
       else:
           break

    numeros_practica8.decorar_turnos(mi_rubro)


def inicio():

    while True:
        preguntar()
        try:
            otro_turno = input('Quieres sacar otro turno? [S] [N]: ').upper()
            ['S', 'N'].index(otro_turno)
        except ValueError:
            print('Esa no es una opcion valida')
        else:
            if otro_turno == 'N':
                print('Gracias por su visita')
                break

inicio()