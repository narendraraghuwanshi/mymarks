# Generated by Django 2.0.5 on 2018-12-20 17:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Students', '0002_auto_20181210_1808'),
        ('SessionYear', '0006_auto_20181220_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='SessionExamMarks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.CharField(max_length=10, null=True)),
                ('sessionExam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='marksessionexam', to='SessionYear.SessionCourseExam')),
                ('sessionStudent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='markstudent', to='Students.Students')),
            ],
        ),
    ]
