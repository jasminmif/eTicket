from django.shortcuts import render
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from api_helper import JResponse as JR
from django.views.decorators.csrf import csrf_exempt
from ticket import models as TCK
import random, string
from api_helper import ticket_generator_helper
import uuid

@csrf_exempt
def scan_ticket(request):
    ticket_uuid = request.POST.get('ticketUUID')

    try:
        if ticket_uuid:
            try:
                ticket = TCK.Ticket.objects.get(uuid_code = ticket_uuid)
                if ticket.used:
                    return JR.Response(200, '', 'Ticket is already Scanned / Used', False)
                ticket.used = True
                ticket.save()

            except TCK.Ticket.DoesNotExist:
                return JR.Response(400, '', 'Invalid Ticket UUID number')

            return JR.Response(200, '', 'Ticket Validated', True)
    except Exception as e:
        return JR.Response(500, '', e.message)

@csrf_exempt
def main_view(request):
    c = {}
    c.update(csrf(request))
    return render_to_response('main.html', c)

def get_uuid_code():
    x = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(16))
    return x


@csrf_exempt
def add_ticket_uuid(request):
    try:
        number_of_tickets = int(request.POST.get('numberOfTickets'))

        for loop in range(1, number_of_tickets + 1):
            new_ticket = TCK.Ticket()
            new_ticket.uuid_code = get_uuid_code()
            new_ticket.save()

        return JR.Response(200, '', 'Successfully created {} tickets UUIDs'.format(number_of_tickets), True)
    except Exception as e:
        return JR.Response(500, '', e.message)


@csrf_exempt
def generate_ticket_images(request):
    try:
        tickets_arr = TCK.Ticket.objects.filter(printed=False)

        for ticket in tickets_arr:
            ticket_generator_helper.generate_ticket(ticket.uuid_code, ticket.id)
            ticket.printed = True
            ticket.save()

        return JR.Response(200, '', 'Successfully genrated Ticket Images for Print', True)
    except Exception as e:
        return JR.Response(500, '', e.message)


