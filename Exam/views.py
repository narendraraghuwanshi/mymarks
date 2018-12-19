from django.shortcuts import render,get_object_or_404
from django_tables2 import RequestConfig
from Exam.models import Exam, ExamCourse
from Subject.models import Subject, ExamSubject
from django.utils import timezone
from django.http import HttpResponseRedirect
from .tables import ExamTable
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
@login_required(login_url='login')


# list of calss
def index(request):
    # values_list('id', 'headline')
     exams = ExamTable(Exam.objects.filter(is_deleted=0))
     # classes = ClassTable(Course.objects.values_list('ID', 'class_name','class_section','grade_system'))
     RequestConfig(request, paginate={'per_page': 10}).configure(exams)
     return render(request, 'exam/index.html', {'exams': exams})


# create class form
def create(request):
    return render(request, 'exam/create.html')

# store class

def store(request):
    if request.method == 'POST':
        data = request.POST
        exam = Exam(
            examName= data['examName'],
            # examPatrak=data['examPatrak'],
            description = data['description'],
        )

        exam.save()
        messages.success(request, 'Exam Created successfully.')
        return HttpResponseRedirect('/exam/')
    else:
        messages.warning(request, 'Exam Created unsuccessfully. Try Again')
        return HttpResponseRedirect('/Exam/create')




# edit class

def edit(request,id):
    examdata = get_object_or_404(Exam, id=id)
    return render(request, 'Exam/edit.html', {'examdata': examdata})


def detail(request,id):
    examdata = get_object_or_404(Exam, id=id)
    return render(request, 'exam/detail.html', {'examdata': examdata})


# update classs
def update(request,id):
    if request.method == 'POST':
        data = request.POST
        update = get_object_or_404(Exam, id=id)
        update.examName= data['examName']
        update.description= data['description']
        update.created_at = timezone.localdate()
        update.save()
        messages.success(request, 'Exam Update successfully.')
    return HttpResponseRedirect('/exam/')


# delete class
def delete(request,id):
        exam = get_object_or_404(Exam, id=id)
        if request.method == "GET":
           exam.is_deleted = 1
           result = exam.save()
           messages.success(request, 'Exam Delete successfully.')
           # messages.warning(request, 'Course Delete unsuccessfully. Try Again')
        return HttpResponseRedirect('/exam/')

def subject(request, id):
    if request.method == 'GET' and 'delete' in request.GET:
        examsubject = get_object_or_404(ExamSubject, id=request.GET['delete'])
        examsubject.is_deleted = True
        examsubject.save()
        messages.warning(request, 'Subject Remove Successfully.')
    if request.method == 'GET' and 'add' in request.GET:
        examsubject = ExamSubject.objects.filter(exam_id=id,subject_id=request.GET['add']).first()
        if(examsubject):
            if(examsubject.is_deleted==True):
                examsubject.is_deleted = False;
                examsubject.save()
                messages.success(request, 'Subject Added Successfully.')
            else:
                messages.warning(request, 'Subject Allready Exist.')
        else:
            ExamSubject(exam_id=id,subject_id=request.GET['add']).save()
            messages.success(request, 'Subject Added Successfully.')
        return redirect('exam.subject', id)
    if request.method == 'GET' and 'min' and 'max' and 'id' in request.GET:
        examsubject = ExamSubject.objects.filter(exam_id=id,id=request.GET['id']).first()
        print(examsubject)
        examsubject.minMarks = request.GET['min']
        examsubject.maxMarks = request.GET['max']
        examsubject.save()
        messages.success(request, 'Subject update Successfully.')
        return redirect('exam.subject', id)
    exam = get_object_or_404(ExamCourse, id=id)
    subjects = Subject.objects.filter(is_deleted=False).all()
    return render(request, 'exam/subject.html', {'exam': exam, 'masterSubjects':subjects})