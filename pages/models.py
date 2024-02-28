from django.db import models
from django_project.settings import AUTH_USER_MODEL

# Create your models here.

class Page(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    cover_image = models.ImageField(upload_to='home/', blank=True, null=True)

    def __str__(self):
        return self.title
    

class TeamMember(models.Model):
    name = models.CharField(max_length=200)
    role = models.CharField(max_length=200)
    bio = models.TextField()
    image = models.ImageField(upload_to='team/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE)
    publication_date = models.DateField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)

    def __str__(self):
        return self.title
    
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    release_date = models.DateField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)

    def __str__(self):
        return self.title