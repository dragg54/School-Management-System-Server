# Generated by Django 4.1.4 on 2022-12-18 08:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Teacher', '0002_remove_teacher_teacher_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher',
            name='teacher_id',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
