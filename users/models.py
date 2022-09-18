from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# OneToOneField means each argument(user) associated with one thing like Profile
# CASCADE means when we deleted the user the user profile also deleted but when we delete
# Profile the user wont be deleted. and it's one way


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')


# __str__ method help us to print the class with more details. in default it shows class.objects

    def __str__(self):
        return f'{self.user.username} Profile'
