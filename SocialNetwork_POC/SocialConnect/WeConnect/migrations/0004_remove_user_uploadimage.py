# Generated by Django 3.2.7 on 2021-09-28 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('WeConnect', '0003_alter_user_uploadimage'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='UploadImage',
        ),
    ]
