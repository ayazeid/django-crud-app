# Generated by Django 4.0.1 on 2022-01-31 20:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='students',
            name='name',
        ),
    ]
