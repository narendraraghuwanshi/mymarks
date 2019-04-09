from django.db import models

# Create your models here.
from django.db import models
from random import choice
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User

class Students(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE,
        primary_key=True)
    father_name = models.CharField(_('fatherName'), max_length=50, blank=True, null=True)
    mother_name = models.CharField(_('motherName'), max_length=50, blank=True, null=True)
    role_number = models.CharField(_('rollNumber'), max_length=50, blank=True, null=True)
    enrollemnt = models.CharField(_('enrollmentNumber'), max_length=50, blank=True, null=True)
    scholership_number = models.CharField(_('scholarshipNumber'), max_length=50, blank=True, null=True)
    adhar_number = models.CharField(_('adhaarNumber'), max_length=50, blank=True, null=True)
    family_id = models.CharField(_('familyId'), max_length=50, blank=True, null=True)
    sssm_id = models.CharField(_('sssmId'), max_length=50, blank=True, null=True)
    bank_name = models.CharField(_('bankName'), max_length=50, blank=True, null=True)
    bank_ifsc = models.CharField(_('bankIfsc'), max_length=50, blank=True, null=True)
    bank_account_number = models.CharField(_('accountNumber'), max_length=50, blank=True, null=True)
    mobile_number = models.CharField(_('mobileNumber'), max_length=50, blank=True, null=True)
    gender = models.BooleanField(_('gender'), max_length=50, blank=True, null=True)
    medium = models.BooleanField(_('medium'), max_length=50, blank=True, null=True)
    dob = models.DateField(_('dataOfBirth'), max_length=50, blank=True, null=True)
    address = models.CharField(_('address'), max_length=50, blank=True, null=True)
    city = models.CharField(_('city'), max_length=50, blank=True, null=True)
    state = models.CharField(_('state'), max_length=50, blank=True, null=True)
    postal_code = models.CharField(_('postalCode'), max_length=50, blank=True, null=True)

def set_token(self):

            self.token = ''.join([choice('abcdefghijklmnopqrstuvwxyz0123456789') for i in range(15)])

# def save(self, *args, **kwargs):
#     super(Students, self).save(*args, **kwargs)
#     self.set_token()