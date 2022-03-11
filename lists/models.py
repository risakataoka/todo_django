from django.db import models

# Create your models here.


class daily(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class reminder(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class objective(models.Model):
    content = models.TextField()

    def __str__(self):
        return self.content


class done(models.Model):
    content = models.TextField()
    date_str = models.TextField()

    def __str__(self):
        return self.content
