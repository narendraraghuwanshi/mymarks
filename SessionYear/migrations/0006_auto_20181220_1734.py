# Generated by Django 2.0.5 on 2018-12-20 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SessionYear', '0005_auto_20181216_2029'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sessionexammarks',
            name='sessionStudent',
        ),
        migrations.AddField(
            model_name='sessioncourseexamstudents',
            name='total',
            field=models.FloatField(null=True),
        ),
        migrations.DeleteModel(
            name='SessionExamMarks',
        ),
    ]