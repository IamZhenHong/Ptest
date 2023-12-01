from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    background_image_path = models.CharField(max_length=255, blank=True)
    image_path = models.CharField(max_length=255, blank=True)

class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    label = models.CharField(max_length=1,default='c')

class PersonalityType(models.Model):
    name_image_path = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    description = models.TextField()
    background_image = models.CharField(max_length=255, blank=True)
    images = models.CharField(max_length=255, blank=True)
    link = models.URLField(blank=True)
    
