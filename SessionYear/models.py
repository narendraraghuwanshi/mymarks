from django.db import models
from Exam.models import ExamCourse
from Course.models import Course
from Subject.models import ExamSubject
from Students.models import Students
# Create your models here.

class SessionYear(models.Model):
    sessionStartDate     = models.DateField(null=True)
    sessionEndDate     = models.DateField(null=True)
    sessionDescription  = models.TextField(null=True)
    # courseExam         = models.ManyToManyField(ExamCourse)
    is_deleted = models.BooleanField(default=False)
    created_at          = models.DateTimeField(auto_now_add=True, null=True)
    updated_at          = models.DateTimeField(auto_now=True, null=True)

    @property
    def year(self):
        # "Returns the Year range."
        return '%s - %s' % (self.sessionStartDate.year, self.sessionEndDate.year)


class SessionCourseExam(models.Model):
    session = models.ForeignKey(SessionYear,on_delete=models.CASCADE,related_name='session')
    course = models.ForeignKey(Course,on_delete=models.CASCADE,blank=True,default=False,related_name='sessioncourse')
    courseExam = models.ForeignKey(ExamCourse,on_delete=models.CASCADE, related_name='courseExam')
    courseExamSubject      = models.ManyToManyField(ExamSubject,related_name='sessionsubject')
    # students        = models.ManyToManyField(Students) #remove because we need student result and rank column
    is_deleted = models.BooleanField(default=False)

class SessionCourseExamStudents(models.Model):
    courseexam  = models.ForeignKey(SessionCourseExam,on_delete=models.CASCADE,related_name='courseexam')
    student     = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='student')
    remark      = models.TextField(null=True)
    result      = models.CharField(max_length=250, null=True)
    rank        = models.CharField(max_length=100)
    total        = models.FloatField(null=True)
    # marks       = models.
    created_at  = models.DateTimeField(auto_now_add=True, null=True)
    updated_at  = models.DateTimeField(auto_now=True, null=True)