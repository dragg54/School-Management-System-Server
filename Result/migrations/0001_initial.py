# Generated by Django 4.1.4 on 2022-12-16 18:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Courses', '0001_initial'),
        ('Student', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test_score_obtainable', models.CharField(max_length=3)),
                ('test_score_obtained', models.CharField(max_length=3)),
                ('exam_score_obtainable', models.CharField(max_length=3)),
                ('exam_score_obtained', models.CharField(max_length=3)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Courses.courses')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Student.student')),
            ],
        ),
    ]