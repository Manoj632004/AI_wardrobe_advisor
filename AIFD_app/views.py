from re import template
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def get_home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
def closet(request):
    template = loader.get_template('closet.html')
    return HttpResponse(template.render())
