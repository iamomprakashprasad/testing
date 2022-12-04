from django.http import HttpResponse
from django.template import loader
from django.shortcuts import redirect

# Create your views here.

def dashboard(request,username=""):
    # print(index_template.render())
    
    print("request --> ",request)
    print("username --> ",request.user)
    if request.user and not username:
        return redirect(f'/users/dashboard/{request.user}')
    else:
        user_data={"user":request.user}
        index_template=loader.get_template('users/dashboard.html')
        return HttpResponse(index_template.render(user_data))    