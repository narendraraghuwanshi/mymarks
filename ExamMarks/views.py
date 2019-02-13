from django.shortcuts import render
from django.shortcuts import render,get_object_or_404
from SessionYear.models import SessionCourseExam,SessionCourseExamStudents
from ExamMarks.models import SessionExamMarks
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import json



# Create your views here.
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request, id):
    exam = SessionCourseExam.objects.filter(is_deleted=False, id=id).first()



    return render(request, 'marks/index.html',{'exam':exam})


def student(request,id,idd):
    if(request.method=='POST'):
        data = request.POST
        for datanew in data:
            if(datanew !='csrfmiddlewaretoken'):
                marks = get_object_or_404(SessionExamMarks, id=datanew)
                marks.marks = data[datanew]
                marks.save()
        return HttpResponseRedirect('/marks/%d'%id)
    exam = SessionCourseExam.objects.filter(is_deleted=False, id=id).first()
    student = SessionCourseExamStudents.objects.filter(courseexam_id=id,id=idd).first()
    return render(request, 'marks/student.html', {'exam': exam,'student':student})

def updatemarks(request):
    if request.method == 'POST':
        data = request.POST;

    for datanew in data:
        if (datanew != 'csrfmiddlewaretoken'):
            marks = get_object_or_404(SessionExamMarks, id=datanew)
            marks.marks = data[datanew]
            marks.save()
    return HttpResponse('success')



def updatemarksajax():
    return  HttpResponse('dfdfdf')


def editstudentsubjectmarks(request,id,subject ):
    # marks = get_object_or_404(SessionExamMarks, examSubject_id=subject)
    marks = SessionExamMarks.objects.filter( examSubject_id=subject)


    for mark in marks:
        print(mark.sessionStudent.student.user.first_name)
        print(mark.examSubject.subject.subjectName)


    return render(request, 'marks/subject_mark.html', {'marks':marks} )
    # return HttpResponse('ddddd')