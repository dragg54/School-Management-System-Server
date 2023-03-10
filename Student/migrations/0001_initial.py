# Generated by Django 4.1.4 on 2022-12-16 18:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('student_class', models.CharField(max_length=5)),
                ('sex', models.CharField(max_length=1)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.CharField(max_length=2)),
                ('session_fee_payable', models.CharField(max_length=10)),
                ('session_fee_paid', models.CharField(max_length=10)),
                ('role', models.CharField(max_length=10)),
                ('next_of_kin', models.CharField(max_length=30)),
                ('date_admitted', models.DateField()),
                ('student_id', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
