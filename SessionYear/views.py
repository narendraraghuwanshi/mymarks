from django.shortcuts import render,get_object_or_404
from django.shortcuts import redirect
from django_tables2 import RequestConfig
from SessionYear.models import SessionYear,SessionCourseExam, SessionCourseExamStudents
from django.http import HttpResponseRedirect
from SessionYear.table import SessionYearTable
from Exam.models import ExamCourse
from Students.models import Students
from Subject.models import ExamSubject
from django.contrib import messages
# list of Session

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request):
     sessionsyr = SessionYearTable(SessionYear.objects.filter(is_deleted=False).all())
     RequestConfig(request, paginate={'per_page': 10}).configure(sessionsyr)
     return render(request, 'session/index.html', {'session': sessionsyr})

# create Session form
def create(request):
    return render(request, 'session/create.html')

# store class
def store(request):
    if request.method == 'POST':
        data = request.POST
        sessionYr = SessionYear(
            sessionStartDate= data['sessionStartDate'],
            sessionEndDate=data['sessionEndDate'],
            sessionDescription = data['sessionDescription'],
        )
        sessionYr.save()
        messages.success(request, 'Session Create successfully.')
        return HttpResponseRedirect('/session/')
    else:
        return HttpResponseRedirect('/session/create')

# edit class
def edit(request,id):
    sessionYr = SessionYear.objects.filter(id=id).first()
    return render(request, 'session/edit.html', {'session': sessionYr})

# update classs
def update(request,id):
    if request.method == 'POST':
        data = request.POST
        print(data)
        sessionYr = SessionYear.objects.get(id=id)
        sessionYr.sessionStartDate = data['sessionStartDate']
        sessionYr.sessionEndDate = data['sessionEndDate']
        sessionYr.sessionDescription = data['sessionDescription']
        sessionYr.save()
    return HttpResponseRedirect('/session/')

# delete class
def detail(request,id):
    sessionYr = SessionYear.objects.get(id=id)
    if request.method == 'POST':
        data = request.POST
        examcourse = ExamCourse.objects.filter(id=data['exam_id']).first()
        sessioncourse = SessionCourseExam(
            courseExam_id = data['exam_id'],
            session_id      = id
        )
        sessioncourse.save()
        students    = Students.objects.filter(is_deleted=False,course_id=examcourse.course.id).all()
        subject     = ExamSubject.objects.filter(is_deleted=False,exam_id=examcourse.id)
        sessioncourse.courseExamSubject.add(*subject)
        # sessioncourse.students.add(*students)
        sessioncourse.save()
        for student in students:
            SessionCourseExamStudents(courseexam_id=sessioncourse.id, student_id=student.user_id)
        messages.success(request, 'All Data Saved successfully.')
        # return HttpResponseRedirect('/session/'+id)
        return redirect('session.detail', id=id)
    courses     =   ExamCourse.objects.filter(is_deleted=False).all()
    return render(request, 'session/detail.html', {'session': sessionYr,'courses':courses})


# delete class
def delete(request,id):
    sessionYr = SessionYear.objects.filter(id=id).first()
    sessionYr.is_deleted = True
    sessionYr.save()
    messages.success(request, 'Session Delete successfully.')
    return HttpResponseRedirect('/session/')