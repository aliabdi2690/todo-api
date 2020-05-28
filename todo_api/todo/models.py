from django.db import models
from django.contrib.auth.models import User

class todolist(models.Model):
    name = models.CharField(max_length=250)
    is_done = models.BooleanField(default=False)
    owner = models.ForeignKey('auth.User', related_name='todos', on_delete=models.CASCADE, editable=False, null=False, blank=False)

    objects = models.Manager()