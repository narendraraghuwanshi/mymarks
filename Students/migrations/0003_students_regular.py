# Generated by Django 2.0.5 on 2019-04-07 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Students', '0002_auto_20190407_0228'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='regular',
            field=models.IntegerField(default=0, verbose_name='regular'),
        ),
    ]
