from django.shortcuts import render, reverse, HttpResponse, HttpResponseRedirect
from user.models import User
# Create your views here.


def register(request):
    if request.method == 'POST':
        new_user = User(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            phone=request.POST['phone'],
            permissions=request.POST['permissions'],
        )
        new_user.save()
        return HttpResponseRedirect(reverse('user:login'))
    elif request.method == 'GET':
        template = 'user/register.html'
        return render(request, template)
    return HttpResponse('No es posible guardar!')


def login(request):
    if request.method == 'POST':
        try:
            user = User.objects.get(first_name=request.POST['first_name'], permissions=request.POST['permissions'])
        except User.DoesNotExist:
            return HttpResponse('Usuario no existe!!!')

        return HttpResponseRedirect(reverse('estate:index', kwargs={'user_pk': user.pk}))
    elif request.method == 'GET':
        template = 'user/login.html'
        return render(request, template)
    return HttpResponse('Method not allowed')
