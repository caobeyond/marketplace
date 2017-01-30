from django.http import HttpResponse,JsonResponse
from rest_framework.response import Response
from store.models import Client
import json

def AuthClient(f):
    def func_wrapper(self, request, *args, **kwargs):
        if request.session.has_key('client_code'):
            return f(self, request, *args, **kwargs)
        else:
            return HttpResponse("Not Authorized", status= 403)
    return func_wrapper
def AuthClientForFunc(f):
    def func_wrapper(request,*args, **kwargs):
        if request.session.has_key('client_code'):
            return f(request,*args, **kwargs)
        else:
            return HttpResponse("Not Authorized", status= 403)
    return func_wrapper

def CurrentUser(f):
    def func_wrapper(request,*args, **kwargs):
        client_code = request.session['client_code']
        client = Client.objects.get(code = client_code)
        request.current_user = client
        return f(request,*args, **kwargs)
    return func_wrapper

def Jsonize(SerializerClass, many=False):
    def wrap(f):
        def func_wrapper(request,*args,**kwargs):
            if request.body is not None:
                try:
                    data = json.loads(request.body)
                    request.data =  data
                except BaseException as e:
                    print(e)
            obj =  f(request,*args,**kwargs)
            serializer = SerializerClass(obj, many = many)
            return HttpResponse(json.dumps(serializer.data, ensure_ascii=False),content_type="application/json")
        return func_wrapper
    return wrap

def AllowMethod(*args):
    allowed_methods = args
    def wrap(f):
        def func_wrapper(request):
            if request.method in allowed_methods:
                return f(request)
            else:
                return HttpResponse("Bad Request", status= 400)
        return func_wrapper
    return wrap
def JSONRequest(f):
    def func_wrapper(request):
        try:
            #mport pdb;pdb.set_trace()
            data = json.loads(request.body.decode('utf-8'))
            request.data =  data
            return f(request)
        except Exception as e:
            print(e)
            return HttpResponse("Bad Request", status= 400)
    return func_wrapper
