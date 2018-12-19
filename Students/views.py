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
from tablib import Dataset
from django.core.files.storage import FileSystemStorage
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
            excel = request.FILES['excel']
            dataset = Dataset()
            import_data = dataset.load(excel.read())
            student = Students()
            result = student.import_data(dataset, dry_run=True)  # Test the data import

            if not result.has_errors():
                student.import_data(dataset, dry_run=False)  # Actually import now

            print(excelData)

    return render(request, 'students/excel.html')


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
