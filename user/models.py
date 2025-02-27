from django.db import models

class MyUser(models.Model):
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    phoneNumber = models.CharField(max_length=20)
    profilePicture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    friends = models.ManyToManyField('self', related_name='friends_list', blank=True, symmetrical=False)

    def __str__(self):
        return self.username

class Driver(models.Model):
    name = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    plate_number = models.CharField(max_length=20)
    rating = models.FloatField(default=0)
    available = models.BooleanField(default=True)
    service_duration_year = models.IntegerField(default=0)
    current_longtidue = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)
    current_latitude = models.DecimalField(max_digits=9, decimal_places=6, default=0.0)

    def __str__(self):
        return self.name
