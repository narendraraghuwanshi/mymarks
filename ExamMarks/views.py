from django.shortcuts import render

# Create your views here.
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request, id):

    return render(request, 'marks/index.html')