# Generated by Django 4.0.1 on 2022-01-31 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0002_remove_students_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='students',
            name='fname',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='students',
            name='lname',
            field=models.CharField(default='', max_length=30),
        ),
    ]