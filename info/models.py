from django.db import models

# Create your models here.

class Pornstar(models.Model):
    image = models.FileField()
    name = models.CharField(max_length=200)
    rank = models.IntegerField()
    bio = models.TextField()
    birthday = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200, help_text="Enter a category")

    def __str__(self):
        return self.name


class UploadMedia(models.Model):
    file = models.FileField()
    title = models.CharField(max_length=200)
    duration = models.IntegerField
    category = models.ManyToManyField(Category)
    pornstar = models.ManyToManyField(Pornstar)
    date_added = models.DateField(null=True, blank=True)



