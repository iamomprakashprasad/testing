from django.urls import path, include
from users import views

urlpatterns = [
    path('dashboard/<username>', view=views.dashboard, name="dashboard"),
    path('dashboard/', view=views.dashboard, name="dashboard"),
    path('accounts/',view=include("django.contrib.auth.urls"))

]
