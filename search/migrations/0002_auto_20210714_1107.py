# Generated by Django 3.2.4 on 2021-07-14 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reviewrating',
            old_name='doctor',
            new_name='review_doctor',
        ),
        migrations.RenameField(
            model_name='reviewrating',
            old_name='patient',
            new_name='review_patient',
        ),
    ]