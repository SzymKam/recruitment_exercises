from django.db import models
from typing import Optional
from datetime import date

class UserProfile(models.Model):
    birthdate = models.DateField(blank=True, null=True)
    github_name = models.CharField(max_length=255, blank=True, null=True)


class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    profile = models.OneToOneField(UserProfile,on_delete=models.CASCADE)


def create_user_profile(first_name: str,
                        last_name: str,
                        github_name: Optional[str],
                        birthdate: Optional[date]):
    user = User.objects.create(first_name=first_name, last_name=last_name)

    if user.profile:
        user_profile = user.profile

        user_profile.github_name = github_name
        user_profile.birthdate = birthdate
        user_profile.save()

    return user

"""cant create user without profile, ist mandatory to declarate profile when creating user"""