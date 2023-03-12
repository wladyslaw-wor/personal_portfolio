from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='portfolio/images')
    url = models.URLField(blank=True)

    def __str__(self):
        return self.title

class Bio(models.Model):
    image = models.ImageField(upload_to='portfolio/images')
    text = models.CharField(max_length=100)

    def __str__(self):
        return self.text

class Link(models.Model):
    title = models.CharField(max_length=20)
    newPage = models.BooleanField(verbose_name="Open in the new tab")
    url = models.URLField()

    def __str__(self):
        return self.title

class Identic(models.Model):
    logo = models.ImageField(upload_to='portfolio/images')
    headTag = models.CharField(max_length=20, verbose_name="Head Tag")

    def __str__(self):
        return self.headTag