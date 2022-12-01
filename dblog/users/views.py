from django.http import HttpResponse
from django.template import loader

# Create your views here.

def dashboard(request,username=""):
    index_template=loader.get_template('users/dashboard.html')
    # print(index_template.render())
    user_data={"username":username}
    print("request --> ",request)
    print("username --> ",username)
    return HttpResponse(index_template.render(user_data))    