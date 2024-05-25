from django.urls import path
from .views import login

app_name = 'hodimlar'

urlpatterns = [
    path('', login, name='login')
]
