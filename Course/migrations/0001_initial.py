# Generated by Django 2.0.5 on 2019-04-06 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Medium', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('courseName', models.CharField(max_length=30, null=True)),
                ('courseSection', models.CharField(max_length=10, null=True)),
                ('description', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('medium', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='Medium.Medium')),
            ],
        ),
    ]
