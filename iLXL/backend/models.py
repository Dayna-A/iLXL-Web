from django.db import models
from datetime import date

class Member(models.Model):
    name=models.CharField(max_length= 100)
    headshot=models.ImageField(upload_to='uploads/',height_field=None, width_field=None, default='default.png')
    position = models.CharField(max_length=100)
    active_member=models.BooleanField(default=True)
    semesters_active=models.CharField(max_length=100)
    twitter_url=models.URLField(max_length=200, blank=True, null=True)
    github_url=models.URLField(max_length=200, blank=True, null=True)
    linkedin_url=models.URLField(max_length=200, blank = True, null=True)
    email=models.EmailField(max_length=254, primary_key=True, unique=True)
    website_url=models.URLField(max_length=200, blank = True, null=True)
    expected_graduation=models.CharField(max_length= 50)
    internship_availability=models.CharField(max_length= 50)
    newgrad_availability=models.CharField(max_length= 50)
    cs_interests=models.CharField(max_length= 100, blank= True, null=True)

class Collaborator(models.Model):
    name=models.CharField(max_length= 100)
    position = models.CharField(max_length=100, blank=True, null=True)
    association = models.CharField(max_length=100, blank=True, null=True)

class Project(models.Model):
    project_name=models.CharField(max_length= 100)
    repo_url=models.URLField(max_length=200)
    researchers=models.TextField(blank=True, null=True)
    description=models.TextField(blank=True, null=True)
    future_state=models.TextField(blank=True, null=True)

class Publication(models.Model):
    date_of_publication=models.DateField(default=date.today)
    reference=models.TextField()
    publication_url=models.URLField(max_length=200)
    
    class Meta:
        ordering=['-date_of_publication']

class Grant(models.Model):
    date_of_grant=models.DateField(default=date.today)
    owner=models.CharField(max_length=100)
    details=models.TextField()
    class Meta:
        ordering=['-date_of_grant']

class Event(models.Model):
    when=models.DateTimeField()
    what= models.CharField(max_length=150)
    where= models.CharField(max_length=250)
    description=models.TextField()
    class Meta:
        ordering=['-when']

class News(models.Model):
    title=models.CharField(max_length=150)
    time_posted=models.DateTimeField(auto_now_add=True)
    last_updated=models.DateTimeField(auto_now=True)
    body=models.TextField()
    related_url=models.URLField(max_length=200)
    class Meta:
        ordering=['-time_posted']
