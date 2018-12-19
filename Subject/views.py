from django.shortcuts import render,get_object_or_404
from Subject.models import Subject,SubjectType
from Subject.tables import SubjectTable
from django.http import HttpResponseRedirect
from django_tables2 import RequestConfig
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='login')
def index(request):

    subjects = SubjectTable(Subject.objects.filter(is_deleted=0))

    RequestConfig(request, paginate={'per_page': 10}).configure(subjects)
    return render(request, 'subject/index.html',{'subjects':subjects})

def create(request):
    subjectType = SubjectType.objects.all()
    return render(request, 'subject/create.html',{'subjectType':subjectType});

def store(request):
    if request.method == 'POST':
        data = request.POST
        subject = get_object_or_404(SubjectType, pk=data['type'])

        subject = Subject(
            subjectName=data['subjectName'],
            isGrade=data['isGrade'],
            type=subject,
            description=data['description'],
        )
        subject.save()
        messages.success(request, 'Subject Created successfully.')
        return HttpResponseRedirect('/subject/')
        messages.warning(request, 'Subject Created unsuccessfully. Try Again')
    else:
        return HttpResponseRedirect('/subject/create')

def detail(request):
    return render(request, 'subject/index.html');

def edit(request,id):
    subject = Subject.objects.filter(id=id).first()
    subjectType = SubjectType.objects.all()
    return render(request, 'subject/edit.html',{'subject':subject,'subjectType':subjectType})

def update(request,id):
    if request.method == 'POST':
        data = request.POST
        subject = Subject.objects.get(id=id)
        subject.subjectName= data['subjectName']
        subject.isGrade= data['isGrade']
        subject.description= data['description']
        subject.type_id = int(data['type'])
        subject.save()
        messages.success(request, 'Subject Updated successfully.')
    return HttpResponseRedirect('/subject/')


def delete(request,id):
    subject = get_object_or_404(Subject,id=id)
    if request.method =="GET":
        subject.is_deleted = 1
        subject.save()
        messages.success(request, 'Subject Delete successfully.')
    return HttpResponseRedirect('/subject/')