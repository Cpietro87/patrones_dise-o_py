class Email:
    def enviar(self, mensaje):
        print(f"Enviando email: {mensaje}")


class WhatsApp:
    def enviar(self, mensaje):
        print(f"Enviando WhatsApp: {mensaje}")


def crear_notificacion(tipo):
    if tipo == "email":
        return Email()
    elif tipo == "whatsapp":
        return WhatsApp()
    else:
        raise ValueError("Tipo no válido")


notificacion = crear_notificacion("email")
notificacion.enviar("Hola, estudiante")

notificacion2 = crear_notificacion("whatsapp")
notificacion2.enviar("Hola, estudiante")