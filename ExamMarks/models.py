from django.db import models
from SessionYear.models import SessionYear,SessionCourseExam,SessionCourseExamStudents
from Subject.models import ExamSubject
# Create your models here.


class SessionExamMarks(models.Model):
    # session         = models.ForeignKey(SessionYear,on_delete=models.CASCADE,related_name='markssession',blank=True,null=True)
    sessionStudent  = models.ForeignKey(SessionCourseExamStudents , on_delete=models.CASCADE , related_name='markstudent')
    # sessionExam     = models.ForeignKey(SessionCourseExam , on_delete=models.CASCADE , related_name='marksessionexam')
    examSubject     = models.ForeignKey(ExamSubject , on_delete=models.CASCADE,null=True,related_name='exam_marks')
    marks           = models.CharField(max_length=10 , null=True)