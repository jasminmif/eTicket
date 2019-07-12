import json
from django.http import HttpResponse
from django.core.serializers.json import DjangoJSONEncoder


def Response(status='', obj={}, msg='', success=False):
    api_call = ''
    if not status or status not in http_response_codes:
        status = 500

    selected_code = http_response_codes[status]
    try:
        response_obj = {
            'success': success,
            'msg': msg,
            'type': api_call,
            'status': selected_code['status'],
            'description': selected_code['description'],
            'response_code': selected_code['description'],
            'body': obj
        }

        data = json.dumps(response_obj, cls=DjangoJSONEncoder)
        return HttpResponse(data, content_type='application/json')
    except Exception as e:
        obj = {
            'success': success,
            'msg': e.message,
            'type': api_call,
            'status': selected_code['status'],
            'description': selected_code['description'],
            'response_code': selected_code['description'],
        }
        return HttpResponse(json.dumps(obj, cls=DjangoJSONEncoder), content_type='application/json')


http_response_codes = {
    200: {
        'status': 200,
        'text': 'OK',
        'description': 'Success',
    },
    # 304: {
    #     'status': 304,
    #     # 'text': 'Not Modified',
    #     'description': 'There was no new data to return'
    # },
    400: {
        'status': 400,
        'text': 'Bad Request',
        'description': 'The request was invalid or cannot be otherwise served'
    },
    401: {  # KICK HIM OUT no valid token
        'status': 401,
        'text': 'Unauthorized',
        'description': 'Authentication credentials were missing or incorrect'
    },
    403: {
        'status': 403,
        'text': 'Forbidden',
        'description': 'The request is understood, but it has been refused or access is not allowed'
    },
    404: {
        'status': 404,
        'text': 'Not Found',
        'description': 'The URI requested is invalid or the resource requested, such as a user, does not exists'
    },
    406: {
        'status': 406,
        'text': 'Occupied',
        'description': 'Occupied Login'
    },
    500: {
        'status': 500,
        'text': 'Internal Server Error',
        'description': 'Something is broken'
    },
    # 503: {
    #     'status': 503,
    #     # 'text': 'Service Unavailable',
    #     'description': 'Servers are up, but overloaded with requests. Try again later'
    # }
}