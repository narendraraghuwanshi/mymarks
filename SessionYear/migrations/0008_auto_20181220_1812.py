# Generated by Django 2.0.5 on 2018-12-20 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SessionYear', '0007_sessioncourseexam_is_deleted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sessioncourseexam',
            name='courseExamSubject',
            field=models.ManyToManyField(related_name='sessionsubject', to='Subject.ExamSubject'),
        ),
    ]