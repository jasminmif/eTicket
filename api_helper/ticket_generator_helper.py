from PIL import Image
from datetime import datetime
import pyqrcode
import io
import cStringIO


def get_unique_ticket_name():
    event_id = datetime.now().strftime('%Y%m%d%H%M%S%f')
    return event_id


ticket_layout_dir = './ticket_images/ticket_layout/layout.jpg'
new_ticket = Image.open(ticket_layout_dir)


def generate_ticket(authentication_code, ticket_id, displa_image=False):
    output_format = '.jpg'
    ticket_output_dir = './ticket_images/print_tickets/'

    qr_code_height_width = 428
    qr_code_horizontal_pos = 1452
    qr_code_vertical_pos = 31

    qr_base = pyqrcode.create(authentication_code)
    buffer = io.BytesIO()
    qr_base.png(buffer, scale=4)

    qr_code_image = Image.open(cStringIO.StringIO(buffer.getvalue()))
    qr_code_image = qr_code_image.convert('RGB')
    qr_code_image = qr_code_image.resize((qr_code_height_width, qr_code_height_width))

    new_ticket.paste(qr_code_image, (qr_code_horizontal_pos, qr_code_vertical_pos))
    # full_name = '{}_{}{}'.format(ticket_id, authentication_code, output_format)
    full_name = '{}{}'.format(ticket_id, output_format)
    new_ticket.save(ticket_output_dir + full_name)

    if displa_image:
        new_ticket.show()
