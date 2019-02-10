from django.shortcuts import render
from SessionYear.models import SessionCourseExam,SessionCourseExamStudents
from ExamMarks.models import SessionExamMarks
from django.http import HttpResponseRedirect
from django.http import JsonResponse
import json
from django.core.files.base import ContentFile
from django.core.files.storage import default_storage

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


def generate(request, id):
    exam = SessionCourseExam.objects.filter(is_deleted=False, id=id).first()
    student = SessionCourseExamStudents.objects.filter(courseexam_id=id, id=17).first()
    data = {'name':student.student.user.first_name+' '+student.student.user.last_name,'father_name':student.student.fatherName,'mother_name':student.student.motherName,'roll_number':student.student.rollNumber,'enrollment':student.student.enrollmentNumber,'scholarship':student.student.scholarshipNumber,'adhar':student.student.adhaarNumber,'family_id':student.student.familyId,'sssm_id':student.student.sssmId,'gender':student.student.gender,'medium':student.student.medium,'dob':student.student.dateOfBirth,'address':student.student.address,'postal':student.student.postalCode,'city':student.student.city.cityName,'state':student.student.state.stateName,'country':student.student.country.countryName,'exam_name':exam.courseExam.exam.examName}
    # path = default_storage.save('storage/file.py', ContentFile(data))
    # file = default_storage.open('storage/file_Goi4TQy.py')
    # print(file)
    return JsonResponse(data)



def calculation(request,id):
    data = {}
    exam = SessionCourseExam.objects.filter(is_deleted=False, id=id).first()
    student = SessionCourseExamStudents.objects.filter(courseexam_id=id, id=17).first()
    exec(default_storage.open('storage/file_Goi4TQy.py').read())
    return JsonResponse(data)
