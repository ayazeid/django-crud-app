# Generated by Django 4.0.1 on 2022-02-02 11:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0012_alter_students_trackid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='trackid',
        ),
    ]
