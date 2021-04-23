
from django.http import HttpResponseForbidden

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_active:
            return self.get_response(request)
        return HttpResponseForbidden("you aren't allowed to be here")