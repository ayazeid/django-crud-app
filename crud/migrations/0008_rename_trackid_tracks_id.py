# Generated by Django 4.0.1 on 2022-02-02 11:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crud', '0007_rename_track_id_students_trackid_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tracks',
            old_name='trackid',
            new_name='id',
        ),
    ]