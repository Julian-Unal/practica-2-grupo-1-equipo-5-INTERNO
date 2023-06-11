import pickle


class Usuario:
    def __init__(self, cedula, nombre, correo):
        self.cedula = cedula
        self.nombre = nombre
        self.correo = correo
        self.ahorros = []
        self.ingresos = []
        self.retiros = []
        self.prestamos = []
        self.metas = []

    def get_nombre(self):
        return self.nombre

    def get_correo(self):
        return self.correo

    def get_cedula(self):
        return self.cedula

    def get_ahorros(self):
        return self.ahorros

    def get_ingresos(self):
        return self.ingresos

    def get_retiros(self):
        return self.retiros

    def get_prestamos(self):
        return self.prestamos

    def get_metas(self):
        return self.metas

    def set_nombre(self, nombre):
        self.nombre = nombre

    def set_correo(self, correo):
        self.correo = correo

    def set_cedula(self, cedula):
        self.cedula = cedula

    def set_ahorros(self, ahorros):
        self.ahorros = ahorros

    def set_ingresos(self, ingresos):
        self.ingresos = ingresos

    def set_retiros(self, retiros):
        self.retiros = retiros

    def set_prestamos(self, prestamos):
        self.prestamos = prestamos

    def set_metas(self, metas):
        self.metas = metas

    def nuevo_ingreso(self, ingreso):
        if ingreso.get_cuenta_destino() is not None:
            ingreso.get_cuenta_destino().depositar(ingreso.get_monto())
            self.ingresos.append(ingreso)

    def nuevo_retiro(self, retiro):
        if retiro.get_cuenta_origen() is not None:
            salida = retiro.get_cuenta_origen().retirar(retiro.get_monto())

            if salida:
                self.retiros.append(retiro)

            return salida
        else:
            if retiro.get_categoria().get_saldo() <= retiro.get_monto():
                return True
            else:
                return False

    def nuevo_ahorro(self, ahorro):
        self.ahorros.append(ahorro)

    def nueva_meta(self, meta):
        self.metas.append(meta)

    def get_dinero_cuenta(self):
        total = 0

        for ahorro in self.ahorros:
            total += ahorro.get_saldo()

        for categoria in Categoria:
            total += categoria.get_saldo()

        for meta in self.metas:
            total += meta.get_saldo()

        return total

    def nuevo_prestamo(self, prestamo, bolsillo):
        self.prestamos.append(prestamo)
        bolsillo.set_saldo(bolsillo.get_saldo() + prestamo.get_monto_prestado())

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, "wb") as archivo:
            pickle.dump(self, archivo)

    @staticmethod
    def cargar_desde_archivo(nombre_archivo):
        with open(nombre_archivo, "rb") as archivo:
            usuario = pickle.load(archivo)
        return usuario


class Categoria:
    def __init__(self):
        self.saldo = 0

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo


class Ahorro:
    def __init__(self, saldo):
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo


class Ingreso:
    def __init__(self, cuenta_destino, monto):
        self.cuenta_destino = cuenta_destino
        self.monto = monto

    def get_cuenta_destino(self):
        return self.cuenta_destino

    def get_monto(self):
        return self.monto


class Retiro:
    def __init__(self, cuenta_origen, monto, categoria):
        self.cuenta_origen = cuenta_origen
        self.monto = monto
        self.categoria = categoria

    def get_cuenta_origen(self):
        return self.cuenta_origen

    def get_monto(self):
        return self.monto

    def get_categoria(self):
        return self.categoria


class Prestamo:
    def __init__(self, monto_prestado):
        self.monto_prestado = monto_prestado

    def get_monto_prestado(self):
        return self.monto_prestado


class Meta:
    def __init__(self, saldo):
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo
