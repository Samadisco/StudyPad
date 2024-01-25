from django.db import models

# Create your models here.


class Questions(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self) -> str:
        return (self.question)
    
class Kanski(models.Model):
    question = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='Kanski/', null=True, blank=True)
    chapter = models.CharField(max_length=50,blank=True, null=True)
    answer = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return (self.question)    