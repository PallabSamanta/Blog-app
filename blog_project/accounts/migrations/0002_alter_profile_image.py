# Generated by Django 5.2.1 on 2025-05-13 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='profile_pics'),
        ),
    ]
