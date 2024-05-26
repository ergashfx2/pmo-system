from django.urls import path
from .views import login_view, login_confirmView, logoutView

app_name = 'hodimlar'

urlpatterns = [
    path('', login_confirmView, name='login'),
    path('login/', login_confirmView, name='login-confirm'),
    path('logout/',logoutView, name='logout'),
    # path('register/',registerView, name='register')
]
