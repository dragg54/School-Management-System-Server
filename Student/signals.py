from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from Student.models import Student


@receiver(post_save, sender=User)
def create_student(sender, instance, created, **kwargs):
    if created:
        Student.objects.create(student_id=instance)


@receiver(post_save, sender=User)
def save_student(sender, instance, **kwargs):
    instance.student.save()
