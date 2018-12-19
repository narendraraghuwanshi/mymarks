# Generated by Django 2.0.5 on 2018-12-10 17:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Subject', '0002_auto_20181206_1707'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examsubject',
            name='exam',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subjects', to='Exam.ExamCourse'),
        ),
        migrations.AlterField(
            model_name='examsubject',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exams', to='Subject.Subject'),
        ),
    ]
