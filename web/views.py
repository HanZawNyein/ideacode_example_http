import json

from response import response_plain_text, response_json


def home_view(request):
    return response_plain_text(request=request, status_code=200, message=b'This is Home')


def api_view(request):
    return response_json(request, 200, message={"message": "this is from api view"})

def api_get(request):
    return response_json(request, 200, message={"message": "this is GET Request api view"})