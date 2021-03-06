# Generated by Django 2.0.5 on 2019-04-06 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SessionCourseExam',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_deleted', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SessionCourseExamStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark', models.TextField(null=True)),
                ('result', models.CharField(max_length=250, null=True)),
                ('rank', models.CharField(max_length=100)),
                ('total', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('courseexam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courseexam', to='SessionYear.SessionCourseExam')),
            ],
        ),
        migrations.CreateModel(
            name='SessionYear',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sessionStartDate', models.DateField(null=True)),
                ('sessionEndDate', models.DateField(null=True)),
                ('sessionDescription', models.TextField(null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
