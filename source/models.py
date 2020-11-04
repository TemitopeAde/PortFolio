from django.db import models


class ContactFormData(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    mobile = models.IntegerField()
    message = models.TextField()

    def __str__(self):
        return self.first_name


class NewsLetter(models.Model):
    email = models.CharField(max_length=100)

    def __str__(self):
        return self.email