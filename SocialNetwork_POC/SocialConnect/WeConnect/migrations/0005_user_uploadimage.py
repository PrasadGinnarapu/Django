# Generated by Django 3.2.7 on 2021-09-28 08:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('WeConnect', '0004_remove_user_uploadimage'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='UploadImage',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images'),
            preserve_default=False,
        ),
    ]
