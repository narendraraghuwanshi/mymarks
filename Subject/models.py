# Create your models here.
from django.db import models
from django.utils.translation import ugettext_lazy as _
from Students.models import Students
# from Course.models import Course
from Exam.models import ExamCourse

class SubjectType(models.Model):
    typeName = models.CharField(max_length=100)
    is_deletet = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Subject(models.Model):
    subjectName = models.CharField(_('subjectName'), max_length=50, blank=True, null=True)
    type = models.ForeignKey(SubjectType, on_delete=models.CASCADE, blank=True, null=True)
    isGrade = models.BooleanField(default=False)
    description = models.CharField(_('description'), max_length=50, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)


class ExamSubject(models.Model):
    exam = models.ForeignKey(ExamCourse,on_delete=models.CASCADE, related_name='subjects')
    subject = models.ForeignKey(Subject,on_delete=models.CASCADE, related_name='exams')
    is_deleted = models.BooleanField(default=False)
    minMarks = models.PositiveIntegerField(null=True)
    maxMarks = models.PositiveIntegerField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

