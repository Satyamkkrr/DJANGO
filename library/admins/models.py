from django.db import models
from django.contrib.auth.models import Group, User
# Create your models here.
class add_librarian(models.Model):
    user= models.OneToOneField(User, on_delete=models.CASCADE)
    address=models.CharField(max_length=256)
    contact=models.PositiveIntegerField()
    def __str__(self):
        return self.user.username
