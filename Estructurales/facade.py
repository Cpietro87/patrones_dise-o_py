class Inventario:
    def verificar_stock(self, producto):
        print(f"Verificando stock de {producto}")
        return True

    def descontar_stock(self, producto):
        print(f"Stock actualizado: {producto}")


class Pagos:
    def procesar_pago(self, monto):
        print(f"Pago procesado: ${monto}")


class Facturacion:
    def generar_factura(self, producto, monto):
        print(f"Factura generada: {producto} - ${monto}")

class VentaFarmacia:
    def __init__(self):
        self.inventario = Inventario()
        self.pagos = Pagos()
        self.facturacion = Facturacion()

    def vender(self, producto, monto):
        if not self.inventario.verificar_stock(producto):
            print("No hay stock disponible")
            return

        self.pagos.procesar_pago(monto)
        self.inventario.descontar_stock(producto)
        self.facturacion.generar_factura(producto, monto)

venta = VentaFarmacia()

venta.vender("Paracetamol", 2500)