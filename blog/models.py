#We will use sqllite to store the data and postgres for production. Django has OMR so we dont need to manage the sql directly
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    # content = models.TextField()
    content = RichTextField(blank=True, null=True)
    date_posted = models.DateTimeField(default = timezone.now) # Dont use parenthesis as we want to pass the whole function as an arg and not execute it
    author = models.ForeignKey(User,on_delete=models.CASCADE)# If the user is deleted then we also want to delete the post.
# After creating the class make migrations.To see the sql code, use python manage.py sqlmigrate blog {the file number}. eg-0001.

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk':self.pk})
