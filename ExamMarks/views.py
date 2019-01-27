from django.shortcuts import render
from SessionYear.models import SessionCourseExam,SessionCourseExamStudents
from ExamMarks.models import SessionExamMarks
from django.http import HttpResponseRedirect
import json

# Create your views here.
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='login')
def index(request, id):
    exam  = SessionCourseExam.objects.filter(is_deleted=False, id=id).first()
    return render(request, 'marks/index.html',{'exam':exam})


def student(request,id,idd):
    if(request.method=='POST'):
        data = request.POST
        for k,d in data:
            print(k)
        # marks = SessionExamMarks.objects.filter(id=k,sessionStudent_id=idd).first()
        #    marks.mark = d
        #    marks.update()
        return HttpResponseRedirect('/marks/%d'%id)
    exam = SessionCourseExam.objects.filter(is_deleted=False, id=id).first()
    student = SessionCourseExamStudents.objects.filter(courseexam_id=id,id=idd).first()
    return render(request, 'marks/student.html', {'exam': exam,'student':student})