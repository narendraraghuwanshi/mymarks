from django.shortcuts import render,get_object_or_404
from django_tables2 import RequestConfig
from Course.models import Course
from Medium.models import Medium
from Exam.models import Exam, ExamCourse
from django.utils import timezone
from django.http import HttpResponseRedirect
from .tables import CourseTable
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

# Create your views here.
@login_required(login_url='login')


# list of calss
def index(request):
    # values_list('id', 'headline')
     classes = CourseTable(Course.objects.filter(is_deleted=0))
        # print(classes)
     # classes = ClassTable(Course.objects.values_list('ID', 'class_name','class_section','grade_system'))
     RequestConfig(request, paginate={'per_page': 10}).configure(classes)
     return render(request, 'schoolclass/index.html', {'classes': classes})


# create class form
def create(request):
    medium = Medium.objects.filter(is_deleted=0).all()
    return render(request, 'schoolclass/create.html', {'medium':medium})

# store class

def store(request):
    if request.method == 'POST':
        data = request.POST
        sclass = Course(
            courseName= data['courseName'],
            courseSection=data['courseSection'],
            description = data['courseDescription'],
            medium_id = data['medium'],
        )
        sclass.save()
        messages.success(request, 'Course Created successfully.')
        return HttpResponseRedirect('/class/')
    else:
        messages.warning(request, 'Course Created unsuccessfully. Try Again')
        return HttpResponseRedirect('/class/create')



# detail class

def detail(request,id):
    if request.method == 'POST':
        data = request.POST['exam']
        examcourse = ExamCourse(
                course_id=id,
                is_deleted=False,
                exam_id= data
            )
        examcourse.save()
        messages.success(request, 'Exam Added unsuccessfully')
        return redirect('class.detail', id)
    course = Course.objects.filter(id=id).first()
    masterExams = Exam.objects.filter(is_deleted=False).all()
    courseExams = ExamCourse.objects.filter(is_deleted=False ,course_id=id).all()
    return render(request, 'schoolclass/detail.html', {'course': course, 'masterExams':masterExams,'courseExams':courseExams})


# edit class

def edit(request,id):
    classdata = Course.objects.filter(id=id).first()
    medium = Medium.objects.filter(is_deleted=0).all()
    return render(request, 'schoolclass/edit.html', {'classdata': classdata, 'medium':medium})

# update classs
def update(request,id):
    if request.method == 'POST':
        data = request.POST
        update = Course.objects.get(id=id)

        update.courseName= data['courseName']
        update.courseSection= data['courseSection']
        update.medium_id= int(data['medium'])
        update.description= data['courseDescription']
        update.created_at = timezone.localdate()
        update.save()
        messages.success(request, 'Course Update successfully.')
    return HttpResponseRedirect('/class/')


# delete class
def delete(request,id):

        course = get_object_or_404(Course, id=id)
        if request.method == "GET":
           course.is_deleted = 1
           result = course.save()
           messages.success(request, 'Course Delete successfully.')
           # messages.warning(request, 'Course Delete unsuccessfully. Try Again')

        return HttpResponseRedirect('/class/')

# template class
def template(request,id):
        exam = get_object_or_404(ExamCourse, id=id)
        return render(request, 'schoolclass/template.html', {'exam': exam})
