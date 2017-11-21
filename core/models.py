from django.db import models

from django.contrib.auth.models import User
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} - {}'.format(self.id, self.title)
