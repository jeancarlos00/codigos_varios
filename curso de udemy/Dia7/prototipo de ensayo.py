class Persona:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido


class Cliente(Persona):
    def __init__(self, nombre, apellido, numero_cuenta, balance=0):
        super().__init__(nombre, apellido)
        self.numero_cuenta = numero_cuenta
        self.balance = balance

        def __str__():
            return f'Cliente: {nombre} {apellido} numero de cuenta: {numero_cuenta} ${balance}'

    def depositar(self,monto_deposito):
        self.balance += monto_deposito
        print('Deposito exitoso')

    def retirar(self,monto_retiro):
        if monto_retiro > self.balance:
            self.balance -= monto_retiro

def crear_cliente():
    opcion = 0

    




