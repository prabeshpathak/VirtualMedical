# Generated by Django 3.2.4 on 2021-07-18 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacy', '0003_alter_pharmacy_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pharmacy',
            name='photo',
            field=models.ImageField(blank=True, default='profile/default_pharmacy.jpg', upload_to='pharmacy/'),
        ),
    ]