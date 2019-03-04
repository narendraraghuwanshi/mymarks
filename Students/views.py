from django.shortcuts import render
from django.contrib.auth.models import User
from Students.models import Students,Countries,States,City
from Course.models import Course
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .tables import StudentsTable
from django_tables2 import RequestConfig
from Medium.models import Medium
from django.contrib import messages
from django.core.files.storage import FileSystemStorage
import django_excel
import os

# Create your views here.
@login_required(login_url='login')


def index(request):
    students = StudentsTable(Students.objects.filter(is_deleted=False).all())
    RequestConfig(request, paginate={'per_page': 10}).configure(students)
    return render(request, 'students/index.html',{'students': students});

def create(request):
    mediums = Medium.objects.all()
    countries = Countries.objects.all()
    states   = States.objects.filter(country_id=101).all()
    courses = Course.objects.all()
    return render(request, 'students/create.html',{'mediums':mediums,'countries':countries,'states':states,'courses':courses})

def store(request):
    if request.method == 'POST':
        data = request.POST
        user = User(
            first_name=data['first_name'],
            last_name=data['last_name'],
            username = data['rollNumber'],
            # email = data['email'],
            is_superuser = False,
            is_staff    = False,
            is_active    = True,
            # is_student  = True
        )
        user.save()
        user.students.fatherName = data['fatherName']
        user.students.motherName = data['motherName']
        user.students.rollNumber = data['rollNumber']
        user.students.enrollmentNumber = data['enrollmentNumber']
        user.students.scholarshipNumber = data['scholarshipNumber']
        user.students.adhaarNumber = data['adhaarNumber']
        user.students.familyId = data['familyId']
        user.students.sssmId = data['sssmId']
        user.students.bankName = data['bankName']
        user.students.bankIfsc = data['bankIfsc']
        user.students.accountNumber = data['accountNumber']
        user.students.mobileNumber = data['mobileNumber']
        user.students.gender = data['gender']
        user.students.medium = data['medium']
        user.students.dateOfBirth = data['dateOfBirth']
        user.students.address = data['address']
        user.students.city_id = data['city']
        user.students.state_id = data['state']
        user.students.country_id = data['country']
        user.students.postalCode = data['postalCode']
        print(data['course'])
        user.students.course_id = data['course']
        user.is_student = True
        if len(request.FILES) != 0:
            path = 'static/upload/profile/' + str(user.id) + '/'
            if not os.path.exists(path):
                os.mkdir(path)

            file = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(path + file.name, file)
            user.students.image = filename
        user.save()
        messages.success(request, 'Student create successfully.')
        return HttpResponseRedirect('/students/')
    else:
        messages.warning(request, 'Student not created! Please contact to admin.')
        return HttpResponseRedirect('/students/create')

def detail(request):
    return render(request, 'students/index.html')

def edit(request,id):
    student = Students.objects.filter(user_id=id).first()
    mediums = Medium.objects.all()
    countries = Countries.objects.all()
    states   = States.objects.filter(country_id=student.country_id).all()
    cities   = City.objects.filter(state_id=student.state_id).all()
    courses = Course.objects.all()
    return render(request, 'students/edit.html',{'student':student,'mediums':mediums,'countries':countries,'states':states,'cities':cities,'courses':courses});

def update(request,id):
    if request.method == 'POST':
        data = request.POST
        user = User.objects.get(id=id)
        user.first_name=data['first_name']
        user.last_name=data['last_name']
        user.students.fatherName = data['fatherName']
        user.students.motherName = data['motherName']
        user.students.rollNumber = data['rollNumber']
        user.students.enrollmentNumber = data['enrollmentNumber']
        user.students.scholarshipNumber = data['scholarshipNumber']
        user.students.adhaarNumber = data['adhaarNumber']
        user.students.familyId = data['familyId']
        user.students.sssmId = data['sssmId']
        user.students.bankName = data['bankName']
        user.students.bankIfsc = data['bankIfsc']
        user.students.accountNumber = data['accountNumber']
        user.students.mobileNumber = data['mobileNumber']
        user.students.gender = data['gender']
        user.students.medium = data['medium']
        user.students.dateOfBirth = data['dateOfBirth']
        user.students.address = data['address']
        user.students.country_id = data['country']
        user.students.state_id = data['state']
        user.students.city_id = data['city']
        user.students.postalCode = data['postalCode']
        user.students.course_id = data['course']

        if len(request.FILES) != 0:
            path = 'static/upload/profile/'+str(user.id)+'/'
            if not os.path.exists(path):
                os.mkdir(path)
            file = request.FILES['image']
            fs = FileSystemStorage()
            filename = fs.save(path+file.name, file)
            user.students.image = filename
        user.save()
    messages.success(request, 'Student update successfully.')
    return HttpResponseRedirect('/students/')

def delete(request,id):
    student = Students.objects.get(user_id=id)
    student.is_deleted = True
    if student.save():
        messages.success(request, 'Student Delete successfully.')
        return HttpResponseRedirect('/students/')
    else:
        messages.warning(request, 'Student Delete unsuccessfully. Try Again')
        return HttpResponseRedirect('/students/')

def excel(request):
    if request.method == 'POST':
        if len(request.FILES) != 0:
            exceldata = django_excel.ExcelMixin.get_array(request.FILES['excel'])


            exceldata.pop(0)
            for data in exceldata:
                user = User(
                    first_name=data[0],
                    last_name=data[1],
                    username=data[4],
                    # email = data['email'],
                    is_superuser=False,
                    is_staff=False,
                    is_active=True,
                    # is_student  = True
                )
                user.save()
                user.students.fatherName = data[2]
                user.students.motherName = data[3]
                user.students.rollNumber = data[4]
                user.students.enrollmentNumber = data[5]
                user.students.scholarshipNumber = data[6]
                user.students.adhaarNumber = data[7]
                user.students.familyId = data[8]
                user.students.sssmId = data[9]
                user.students.bankName = data[10]
                user.students.bankIfsc = data[11]
                user.students.accountNumber = data[12]
                user.students.mobileNumber = data[13]
                user.students.gender = data[14]
                user.students.medium = data[15]
                user.students.dateOfBirth = data[16]
                user.students.address = data[17]
                user.students.country_id = data[18]
                user.students.state_id = data[19]
                user.students.city_id = data[20]
                user.students.postalCode = data[21]
                user.students.course_id = data[22]
                user.is_student = True
                user.save()

    mediums = Medium.objects.all()
    countries = Countries.objects.all()
    states = States.objects.filter(country_id=101).all()
    courses = Course.objects.all()
    return render(request, 'students/excel.html', {'mediums':mediums,'countries':countries,'states':states,'courses':courses})


def countries(request):
    countryId = request.GET['country']
    if countryId:
        states = States.objects.filter(country_id=request.GET['country'])
        return render(request, 'students/statesdropdown.html', {'states': states})

def states(request):
    stateId = request.GET['states']
    if stateId:
        cities = City.objects.filter(state_id=request.GET['states'])
        return render(request, 'students/citiesdropdown.html', {'cities': cities})
