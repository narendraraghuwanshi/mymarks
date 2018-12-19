from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse

def index(request):
     users = User.objects.all()
     return render(request, 'users/index.html', {'users': users});



def create(request):
    return render(request, 'users/create.html');



def store(request):
    if request.method == 'POST':
        data = request.POST.get

        return HttpResponse(data)
    else:
        return HttpResponseRedirect( 'user/create' )

def  detail(request, id):
    user = User.objects.filter(id=id).first()
    return render(request, 'users/detail.html', {'user': user})

def edit(request, id):
    user = User.objects.filter(id=id).first()
    return render(request, 'users/edit.html', {'user': user})

def update(request, id):
    user = User.objects.filter(id=id).first()
    return render(request, 'users/edit.html', {'user': user})

def delete(request, id):
    user = User.objects.filter(id=id).first()
    return render(request, 'users/edit.html', {'user': user})