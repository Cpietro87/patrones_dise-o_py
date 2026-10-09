# Builder

class Medicamento:
    def __init__(
        self, nombre, precio, laboratorio,
        presentacion, dosis, descripcion
    ):
        self.nombre = nombre
        self.precio = precio
        self.laboratorio = laboratorio
        self.presentacion = presentacion
        self.dosis = dosis
        self.descripcion = descripcion


medicamento = Medicamento(
    nombre="Paracetamol",
    precio=10.0,
    laboratorio="Laboratorio XYZ",
    presentacion="Tabletas",
    dosis="500 mg",
    descripcion="Analgésico y antipirético"
)

class Medicamento:
    def __init__(self):
        self.nombre = None
        self.precio = None
        self.laboratorio = None
        self.presentacion = None
        self.dosis = None

    def mostrar(self):
        print("Nombre:", self.nombre)
        print("Precio:", self.precio)
        print("Laboratorio:", self.laboratorio)
        print("Presentación:", self.presentacion)
        print("Dosis:", self.dosis)

class MedicamentoBuilder:
    def __init__(self):
        self.medicamento = Medicamento()

    def con_nombre(self, nombre):
        self.medicamento.nombre = nombre
        return self

    def con_precio(self, precio):
        self.medicamento.precio = precio
        return self

    def con_laboratorio(self, laboratorio):
        self.medicamento.laboratorio = laboratorio
        return self

    def con_presentacion(self, presentacion):
        self.medicamento.presentacion = presentacion
        return self

    def con_dosis(self, dosis):
        self.medicamento.dosis = dosis
        return self

    def build(self):
        return self.medicamento

builder = MedicamentoBuilder()

medicamento = (
    builder
    .con_nombre("Paracetamol")
    .con_precio(2500)
    .con_laboratorio("Laboratorio A")
    .con_presentacion("Comprimidos")
    .con_dosis("500 mg")
    .build()
)

medicamento.mostrar()

medicamento1 = (
    MedicamentoBuilder()
    .con_nombre("Paracetamol")
    .con_precio(2500)
    .con_presentacion("Comprimidos")
    .build()
)

medicamento2 = (
    MedicamentoBuilder()
    .con_nombre("Ibuprofeno")
    .con_precio(3200)
    .con_presentacion("Cápsulas")
    .build()
)

medicamento1.mostrar()

print("----------")

medicamento2.mostrar()