# Generated by Django 4.0.1 on 2022-02-02 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0009_alter_students_trackid'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracks',
            old_name='id',
            new_name='tr_id',
        ),
    ]
