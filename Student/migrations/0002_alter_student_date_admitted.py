# Generated by Django 4.1.4 on 2022-12-19 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_admitted',
            field=models.DateField(null=True),
        ),
    ]