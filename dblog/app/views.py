"""basic view for app"""
from django.http import HttpResponse
from django.template import loader

def index(request):
    """
    index file
    """
    index_template=loader.get_template('index.html')
    return HttpResponse(index_template.render())

def documents(request):
    """
    document editor
    """
    data={"user":request.user}
    # print(data.get("user").username)
    document_template=loader.get_template('documents/documents.html')
    return HttpResponse(document_template.render(data))
