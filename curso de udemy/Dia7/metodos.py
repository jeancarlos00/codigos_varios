class Programador:

    def __init__(self, lenguaje, framework):
        self.lenguaje = lenguaje
        self.framework = framework

    def aplicacion(self):
        print(f'la aplicacion que va a crear se llama: {self.framework}')

    def programacion(self):
        self.lenguaje = 'python'
        print(f'El lenguaje de programacion que se va a utilizar es: {self.lenguaje}')


ejecutable = Programador('python', 'angel miguel')

ejecutable.programacion()
ejecutable.aplicacion()


