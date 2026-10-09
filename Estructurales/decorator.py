class Producto:
    def precio(self):
        return 1000

class DecoradorProducto:
    def __init__(self, producto):
        self.producto = producto

    def precio(self):
        return self.producto.precio()

class Descuento10(DecoradorProducto):
    def precio(self):
        return self.producto.precio() * 0.90

class Embalaje(DecoradorProducto):
    def precio(self):
        return self.producto.precio() + 200

producto = Producto()

producto_con_descuento = Descuento10(producto)
producto_final = Embalaje(producto_con_descuento)

print(producto_final.precio())