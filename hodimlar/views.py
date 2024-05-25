from django.contrib.auth import authenticate
from django.shortcuts import render, redirect
from .forms import UserLoginForm
from .models import User


async def login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = await authenticate(request,username,password)
            if user is None:
                try:
                    user = User.objects.get(username=username)
                    user = authenticate(request, username=user.username, password=password)
                except User.DoesNotExist:
                    user = None

            if user is not None:
                await login(request,user)
                return redirect('home')
    else:
        form = UserLoginForm()
        return render(request,'login.html',context={'form':form})

    return render(request,'login.html')