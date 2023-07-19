import json

from response import response_plain_text, response_json


def home_view(request):
    # return response_plain_text(request=request, status_code=200, message=b'This is Home')
    context = {"name": "Han"}
    return request.render_template('home.html', **context)
    # context = "<h1>Hello, Han Zaw</h1>".encode('utf-8')
    # return response_plain_text(request, 200,type='text/html',message=body.encode('utf-8'))

def about_view(request,*args,**kwargs):
    context = {"name": "Han"}
    return  request.render_template('about.html', **context)


def api_view(request, *args, **kwargs):
    return response_json(request, 200, message={"message": "this is from api view"})


def api_get(request):
    return response_json(request, 200, message={"message": "this is GET Request api view"})


def api_post(request, *args, **kwargs):
    return response_json(request, 200, message={"message": "this is GET Request api view"})
