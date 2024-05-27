from django.urls import path
from .views import login_view, logoutView

app_name = 'hodimlar'

urlpatterns = [
    path('', login_view, name='login'),
    path('logout/',logoutView, name='logout'),
    # path('register/',registerView, name='register')
]
