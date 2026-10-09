class ServicioSMS:
    def send_sms(self, mensaje):
        print(f"SMS enviado: {mensaje}")

class AdaptadorSMS:
    def __init__(self, servicio):
        self.servicio = servicio

    def enviar_mensaje(self, mensaje):
        self.servicio.send_sms(mensaje)

class Notificador:
    def __init__(self, servicio):
        self.servicio = servicio

    def notificar(self, mensaje):
        self.servicio.enviar_mensaje(mensaje)


servicio_externo = ServicioSMS()
adaptador = AdaptadorSMS(servicio_externo)

notificador = Notificador(adaptador)
notificador.notificar("Su pedido está listo")