# Generated by Django 4.0.1 on 2022-02-02 11:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0017_students_trackid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='trackid',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='crud.tracks'),
        ),
    ]
