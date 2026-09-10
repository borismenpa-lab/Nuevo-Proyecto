from django.http import HttpResponse
from .pila import Ticket


def demo_ticket(request):
    ticket = Ticket(numero="TCK-001")
    resultado = f"Ticket {ticket.numero} creado en estado: {ticket.estado_actual}<br>"

    ticket.cambiar_estado("En progreso")
    resultado += f"Cambio de estado -> {ticket.estado_actual}<br>"

    ticket.cambiar_estado("Resuelto")
    resultado += f"Cambio de estado -> {ticket.estado_actual}<br>"

    estado_final = ticket.deshacer_ultimo_cambio()
    resultado += f"Deshacer último cambio -> {estado_final}<br>"

    return HttpResponse(resultado)

   # cambio-2 (prueba de stash)