from django.db import models

# Create your models here.


class Medium(models.Model):
    mediumName = models.CharField(max_length=50,null=True)
    mediumDescription = models.CharField(max_length=250,null=True)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)