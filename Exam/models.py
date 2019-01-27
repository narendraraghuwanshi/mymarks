from django.db import models
from Course.models import Course

# Create your models here.

class Exam(models.Model):
    # course = models.ManyToManyField(Course)
    examName = models.CharField(max_length=50, blank=True, null=True)
    # examPatrak = models.FileField(max_length=50, blank=True, null=True)
    # examResultDeclare = models.DateField(null=True)
    description = models.CharField(('description'), max_length=50, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class ExamCourse(models.Model):
    course  = models.ForeignKey(Course,on_delete=models.CASCADE, related_name='course')
    exam    = models.ForeignKey(Exam,on_delete=models.CASCADE, related_name='exam')
    examPatrak = models.FileField(max_length=50, blank=True, null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
