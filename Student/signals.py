from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from Student.models import Student


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        print("first_name:" + instance.first_name)
        Student.objects.create(student_id=instance,
                               first_name=instance.first_name,
                               last_name=instance.last_name
                               )


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.student.save()
