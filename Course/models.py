from django.db import models
from Medium.models import Medium
class Course(models.Model):
    medium = models.ForeignKey(Medium,null=True, on_delete=models.CASCADE)
    courseName = models.CharField(max_length=30,null=True)
    courseSection = models.CharField(max_length=10,null=True)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)
    is_deleted = models.BooleanField(default=False)
