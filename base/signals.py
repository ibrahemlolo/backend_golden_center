from django.db.models.signals import post_save, pre_save
from django.contrib.auth.models import User

from django.dispatch import receiver

def updateUser(sender, instance, **kwargs):
     user = instance
     if user.email and (user.first_name != user.profile.name or user.email != user.profile.email):
         profile = user.profile
         profile.name = user.first_name
         profile.email = user.email
         profile.save()
#     if created:
#         Profile.objects.create(
#             user=instance,
#             name=instance.first_name,
#             email=instance.email,
#         )

pre_save.connect(updateUser, sender=User)