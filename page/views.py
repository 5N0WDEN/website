from django.http import HttpResponse
from django.template import loader

def show(request):
    template = loader.get_template('online.html')
    return HttpResponse(template.render())
