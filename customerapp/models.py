from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=400)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip = models.IntegerField()
    email = models.EmailField(max_length=64)
    web = models.CharField(max_length=200)
    age = models.PositiveIntegerField()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)
