class Configuracion:
    _instancia = None

    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
        return cls._instancia


config1 = Configuracion()
config2 = Configuracion()

print(config1 is config2)
