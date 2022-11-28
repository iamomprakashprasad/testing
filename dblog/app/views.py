"""basic view for app"""
from django.http import HttpResponse

def index(request):
    """
    index file
    """

    return HttpResponse("hola")
