from django.db import models


class Client(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    salary = models.DecimalField(max_digits=5, decimal_places=2)
    age = models.IntegerField()
    bio = models.TextField()
    photo = models.ImageField(upload_to='profile_photos', null=True, blank=True)

    def __str__(self):
        return self.first_name + ' ' + self.last_name
