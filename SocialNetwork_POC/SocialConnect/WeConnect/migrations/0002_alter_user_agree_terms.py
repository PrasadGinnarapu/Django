# Generated by Django 3.2.7 on 2021-09-27 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WeConnect', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='Agree_Terms',
            field=models.BooleanField(default=False),
        ),
    ]
