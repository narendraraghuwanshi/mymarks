from django.shortcuts import render,get_object_or_404
from django_tables2 import RequestConfig
from Course.models import Course
from django.utils import timezone
from django.http import HttpResponseRedirect
from Medium.table import MediumTable


# list of calss
def index(request):

     mediums = MediumTable(Course.objects.all())

     RequestConfig(request, paginate={'per_page': 10}).configure(mediums)
     return render(request, 'schoolclass/index.html', {'mediums': mediums})


# create class form
def create(request):
    return render(request, 'schoolclass/create.html')

# store class

def store(request):
    if request.method == 'POST':
        data = request.POST
        sclass = Course(
            courseName= data['courseName'],
            courseSection=data['courseSection'],
            courseDescription = data['courseDescription'],
        )

        sclass.save()
        return HttpResponseRedirect('/class/')
    else:
        return HttpResponseRedirect('/class/create')




# edit class

def edit(request,id):
    classdata = Course.objects.filter(id=id).first()
    return render(request, 'schoolclass/edit.html', {'classdata': classdata})

# update classs
def update(request,id):
    if request.method == 'POST':
        data = request.POST
        update = Course.objects.get(id=id)

        update.class_name= data['class_name']
        update.class_section= data['class_section']
        update.grade_system= int(data['grade_system'])
        update.class_description= data['description']
        update.pub_date = timezone.localdate()
        update.save()
    return HttpResponseRedirect('/class/')


# delete class
def detail(request,id):
    dlt_class = Course.objects.get(id=id)
    dlt_class.delete()
    return HttpResponseRedirect('/class/')



# delete class
def delete(request,id):
    dlt_class = Course.objects.get(id=id)
    dlt_class.delete()
    return HttpResponseRedirect('/class/')

