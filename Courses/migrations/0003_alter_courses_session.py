# Generated by Django 4.1.4 on 2022-12-22 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Courses', '0002_courses_session'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='session',
            field=models.CharField(default='2020/2021', max_length=9, null=True),
        ),
    ]