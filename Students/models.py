# Create your models here.
from django.db import models
from random import choice
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from Course.models import Course
from django.db.models.signals import post_save
from django.dispatch import receiver
# from safedelete.models import SafeDeleteModel
# from safedelete.models import NO_DELETE

class Countries(models.Model):
    countryName = models.CharField(max_length=100, blank=True, null=True)
    countrySortName = models.CharField(max_length=20, blank=True, null=True)
    countryPhoneCOde = models.CharField(max_length=10, blank=True, null=True)
    language = models.CharField(max_length=10, blank=True, null=True)
    ISO = models.CharField(max_length=100, blank=True, null=True)


class States(models.Model):
    id = models.IntegerField(primary_key=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE)
    stateName = models.CharField(max_length=100, blank=True, null=True)

class City(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.ForeignKey(States, on_delete=models.CASCADE)
    cityName = models.CharField(max_length=20, blank=True, null=True)



def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)


class Students(models.Model):
    # _safedelete_policy = NO_DELETE
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True,blank=True)
    course = models.ForeignKey(Course,null=True,blank=True,on_delete=models.CASCADE, related_name='students')
    image = models.FileField(upload_to=user_directory_path,blank=True)
    fatherName = models.CharField(_('fatherName'), max_length=50, blank=True, null=True)
    motherName = models.CharField(_('motherName'), max_length=50, blank=True, null=True)
    rollNumber = models.CharField(_('rollNumber'), max_length=50, blank=True, null=True)
    enrollmentNumber = models.CharField(_('enrollmentNumber'), max_length=50, blank=True, null=True)
    scholarshipNumber = models.CharField(_('scholarshipNumber'), max_length=50, blank=True, null=True)
    adhaarNumber = models.CharField(_('adhaarNumber'), max_length=50, blank=True, null=True)
    familyId = models.CharField(_('familyId'), max_length=50, blank=True, null=True)
    sssmId = models.CharField(_('sssmId'), max_length=50, blank=True, null=True)
    bankName = models.CharField(_('bankName'), max_length=50, blank=True, null=True)
    bankIfsc = models.CharField(_('bankIfsc'), max_length=50, blank=True, null=True)
    accountNumber = models.CharField(_('accountNumber'), max_length=50, blank=True, null=True)
    mobileNumber = models.CharField(_('mobileNumber'), max_length=50, blank=True, null=True)
    gender = models.IntegerField(_('gender'),   default=0)
    medium = models.IntegerField(_('medium'),   default=0)
    dateOfBirth = models.DateField(_('dateOfBirth'), max_length=50, blank=True, null=True)
    country = models.ForeignKey(Countries, on_delete=models.CASCADE,null=True)
    state = models.ForeignKey(States, on_delete=models.CASCADE,null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE,null=True)
    address = models.CharField(_('address'), max_length=50, blank=True, null=True)
    postalCode = models.CharField(_('postalCode'), max_length=50, blank=True, null=True)
    height      =   models.FloatField(blank=True,null=True)
    weight      =   models.FloatField(blank=True,null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

def set_token(self):

            self.token = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(15)])

def save(self, *args, **kwargs):
    super(Students, self).save(*args, **kwargs)
    self.set_token()

@receiver(post_save, sender=User)
def create_user_students(sender, instance, created, **kwargs):
    if created:
        Students.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_students(sender, instance, **kwargs):
    instance.students.save()