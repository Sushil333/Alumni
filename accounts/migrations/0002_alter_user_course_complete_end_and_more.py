# Generated by Django 4.0.4 on 2022-10-07 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='course_complete_end',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='course_complete_start',
            field=models.DateField(auto_now_add=True),
        ),
    ]
