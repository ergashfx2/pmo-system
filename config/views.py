from django.shortcuts import redirect, render


async def home(request):
    return render(request,'index.html')